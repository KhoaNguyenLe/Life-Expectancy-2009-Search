import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)

db = client["data"]
col = db["life_expectancy"]
col.delete_many({}) 

with open('data.json') as file:
    data = json.load(file)
    for i in data["data"]:
        reldata = {}
        reldata["state"] = i[8]
        reldata["gender"] = i[9]
        reldata["le"] = float(i[10])
        col.insert_one(reldata)
client.close()