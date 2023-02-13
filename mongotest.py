import pymongo
client = pymongo.MongoClient("mongodb+srv://bhendareh:21102000@cluster0.s5yjzww.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name": "harshu" ,
    "email": 'bhendareh@gmail.com'
    ,"no": 8624023659
}

db1 = client['mongotest']
coll = db1["test1"]
coll.insert_one(d)