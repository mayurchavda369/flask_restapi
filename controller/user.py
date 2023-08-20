from app import app
from model.usermodel import usermodel
from model.token_auth import authmodel
from flask import request,send_file
from datetime import datetime


obj=usermodel()
auth=authmodel()

@app.route("/user")
@auth.token_auth("/user")
def user():
    return obj.user_model()
@app.route("/user/add", methods=["POST"])
def add():
    return obj.add_model(request.form)
@app.route("/user/update", methods=["PUT"])
def update():
    return obj.update_model(request.form)

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete(id):
    return obj.delete_model(id)
@app.route("/user/patch/<id>", methods=["PATCH"])
def patch(id):
    return obj.patch_model(request.form,id)
@app.route("/user/limit/<limit>/page/<page>", methods=["GET"])
def pagination(limit,page):
    return obj.pagination_model(limit,page)
@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def uploadfile(uid):
    # print(request.files)
    file=request.files["avatar"]
   
    uniquefilename=str(datetime.now().timestamp()).replace(".","")
    print(str(file.filename).split("."))
    filenamenew=str(file.filename).split(".")
    ext=filenamenew[len(filenamenew)-1]
    finalfilepath=f"upload/{uniquefilename}.{ext}"
    file.save(finalfilepath)
    return obj.uploadfile_model(uid,finalfilepath)
@app.route("/user/<filename>")
def getavatar(filename):
    return send_file(f"upload/{filename}")
@app.route("/user/login",methods=["POST"])
def login():
    #request.form
    return obj.login_model(request.form)

    

# import sys
# import time
# from bs4 import BeautifulSoup
# import requests

# try:
#     page=requests.get("https://www.linkedin.com/feed/")
# except:
#     error_type, error_obj, error_info = sys.exc_info()      
#     print ('ERROR FOR LINK:',url)                          
#     print (error_type, 'Line:', error_info.tb_lineno)     
                                                 
# time.sleep(2)   
# soup=BeautifulSoup(page.text,'html.parser')
# links=soup.find_all('div',attrs={'class':'t-sans t-16 t-black t-bold mb1 break-words'})
