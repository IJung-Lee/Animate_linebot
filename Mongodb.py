import os
import datetime
import urllib.parse
from pymongo import MongoClient

# Authentication Database認證資料庫
aniDB='user_db'

# DB  connection
def constructor_ani():
    client = MongoClient(os.environ["MONGODB_URI"])
    # client = MongoClient("mongodb+srv://myuser:love812118@anitest.ql5k4.mongodb.net/user_db?retryWrites=true&w=majority")
    db = client[aniDB]
    return db

#新增收藏
def insert_ani(uid, name):   
    db = constructor_ani()
    collect = db[uid]
    x = collect.find_one({"favorite_ani":name})
    if x == None:
        content = collect.insert_one({"favorite_ani":name})
    return name + "收藏了就要好好追完哦"

#刪除收藏
def delete_ani(uid, name):   
    db = constructor_ani()
    collect = db[uid]
    x = collect.find_one({"favorite_ani":name})
    if x != None:
        collect.delete_one({"favorite_ani":name})
    return "收藏了就別拋棄我啦"

#查詢動畫是否有收藏
def find_ani(uid, name):     
    db = constructor_ani()
    collect = db[uid]
    x = collect.find_one({"favorite_ani":name})
    if x != None:
        return True
    else:
        return False

#列出收藏清單
def show_ani(uid):
    MyAni = []
    db = constructor_ani()
    collect = db[uid]
    mydoc = collect.find()
    for x in mydoc:
        l=list(x.values())
        MyAni.append(l[1])
    return MyAni


# if __name__ == "__main__":
#     client = MongoClient("mongodb+srv://myuser:love812118@anitest.ql5k4.mongodb.net/user_db?retryWrites=true&w=majority")
#     # client = MongoClient("mongodb+srv://myuser:love812118@anitest.ql5k4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#     db = client[aniDB]
#     dblist = client.list_database_names()
#     if "user_db" in dblist:
#         print("数据库已存在！")