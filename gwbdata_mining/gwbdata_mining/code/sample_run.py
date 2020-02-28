import json
from pymongo import MongoClient

def insert_mongo():
    client = MongoClient('localhost', 27017)
    db = client['Greenway_DB1']
    collection_data = db['Greenway_Data1']
    with open(r"C:\Users\user\Desktop\ImageExtraction\gwbdata_mining\gwbdata_mining\code\invoices-output.json") as f:
        file_data = json.load(f)
    # if pymongo < 3.0, use insert()
    #collection_currency.insert(file_data)
    # if pymongo >= 3.0 use insert_one() for inserting one document
    #collection_data.insert_one(file_data)
    # if pymongo >= 3.0 use insert_many() for inserting many documents
    collection_data.insert_many(file_data)
    client.close()