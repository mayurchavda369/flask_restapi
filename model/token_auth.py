import mysql.connector
from flask import make_response
from flask import request
import jwt
import re
import json

class authmodel():
    def __init__(self):
        #connection establishment code
        try:
           self.con=mysql.connector.connect(host="localhost",user="root",password="mayur369",database="flask_pro")
           self.con.autocommit=True
           self.cur=self.con.cursor(dictionary=True)
           print("connection successfully")
        except:
            print("some error")
        
    def token_auth(self,endpoint):
        def inner1(func):
            def inner2(*args):
                authorization=request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$",authorization,flags=0):
                    token=authorization.split(" ")[1]
                    # print(token)
                    # print(jwt.decode(token,"mayur",algorithms="HS256"))
                    jwt_decoded=jwt.decode(token,"mayur",algorithms="HS256")

                    return func(*args)
                else:
                    return make_response({"ERROR:TOKEN IS INVALID"},401)
        
            return inner2
        return inner1