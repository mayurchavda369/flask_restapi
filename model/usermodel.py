import mysql.connector
from flask import make_response
from datetime import datetime,timedelta
from config.config import dbconfig
import jwt
import json


class usermodel():
    def __init__(self):
        #connection establishment code
        try:
           self.con=mysql.connector.connect(host=dbconfig["host"],user=dbconfig["user"],password=dbconfig["password"],database=dbconfig["database"])
           self.con.autocommit=True
           self.cur=self.con.cursor(dictionary=True)
           print("connection successfully")
        except:
            print("some error")

    def user_model(self):
            #query execution code
            # read operation
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            res= make_response({"payload":result},200)
            res.headers['Access-Controll-Allow-Origin-']="*"
            return res 
        else:
            return make_response({"message": "no data found" },204)
        
    def add_model(self,data):
            #query execution code
            # create operation
        self.cur.execute(f"INSERT INTO users (name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        # print(data["email"])
        return make_response({"message":"user create successfully"},201)
    
    def update_model(self,data):
            #query execution code
            # update operation
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id='{data['id']}' ")
        if self.cur.rowcount>0:
            return make_response({"message":"data update successfully"},200)
        else:
            return make_response({"message":"no data updated"},204)
        
    def delete_model(self,id):
            #query execution code
            # delete operation
        self.cur.execute(f" DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"data deleted successfully"},410)
        else:
            return make_response({"message":"no data delete"},204)
    
    def patch_model(self,data,id):
            #query execution code
            #patch operation (update part)
            qry="UPDATE users SET "
            #print(data)
            for key in data:
                # print(key)
                qry+= f"{key}='{data[key]}'," 
            qry= qry[:-1] + f" WHERE id={id}"
                # print(f"{key}={data[key]}")
            # print(qry)
            #UPDATE users SET col=val,col=val WHERE id={id}
            #return qry
            self.cur.execute(qry)
            if self.cur.rowcount>0:
                return make_response({"message":"data update successfully"},200)
            else:
                return make_response({"message":"no data updated"},204)
            
    def pagination_model(self,limit,page):
        #start=(page*limit)-limit
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        qry=f"SELECT * FROM users LIMIT {start},{limit}"

        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            res= make_response({"payload":result,"page no":page,"limit":limit},200)
            return res 
        else:
            return make_response({"message": "no data found" },204)
    def uploadfile_model(self,uid,filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid} ")
        if self.cur.rowcount>0:
            return make_response({"message":"file uploaded successfully"},200)
        else:
            return make_response({"message":"no data updated"},204)
    def login_model(self,data):
        self.cur.execute(f"SELECT id,name,email,phone,avatar,role_id FROM users WHERE email='{data['email']}' and password='{data['password']}' ")
        result=self.cur.fetchall()
        userdata=str(result[0])
        exp_time=datetime.now()+timedelta(minutes=15)
        exp_epoch_time=int(exp_time.timestamp())
        payload={
            "payload": userdata,
            "exp":exp_epoch_time
        }
        jwt_token=jwt.encode(payload,"mayur",algorithm="HS256")
        return make_response({"token":jwt_token},200)




            
                
        
    
    
        