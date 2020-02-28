# import json
# import pymongo
# import codecs
# from pymongo import MongoClient
# #
# #
# connection = pymongo.MongoClient('localhost', 27017)
# database = connection['mydb_12']
# collection = database['mycoll_12']
# print("Database Connected")
# f = open("invoicefile.json", "w")
# #with codecs.open('C:\Users\user\Desktop\ImageExtraction\gwbdata_mining\gwbdata_mining\code\invoices-output.json') as f:
# file_data = json.load(f)
# collection.insert_one(file_data)
# # # connection.close()
# #
# #
# # # connection = pymongo.MongoClient('localhost', 27017)
# # # database = connection['mydb_09']
# # # collection = database['mycoll_09']
# # # print("Database Connected")
# # #
# # # def insert_data(data1):
# # #     documnet = collection.insert_one(data1)
# # #     return documnet.inserted_id
# # #
# # # data1 = 'invoices-output.json'
# # # insert_data(data1)
# #
# # #this is code
# # connection = pymongo.MongoClient('localhost', 27017)
# # database = connection['mydb_10']
# # collection = database['mycoll_10']
# # # cursor = collection.find({})
# # file = open(r"C:\Users\user\Desktop\ImageExtraction\gwbdata_mining\gwbdata_mining\code\invoices-output.json", "w", encoding="utf-8")
# # for document in cursor:
# #     file.write(json.dumps(document))
# #     file.write(',')
# # file.write(']')
# # print("Database Connected")
# # #end here
# #
# # # def insert_data(data1):
# # #     document = collection.insert_one(data1)
# # #     print('One post: {0}'.format(collection.inserted_id))
# # #     return document.inserted_id
# #
# #
# #     # data1 = data
# #     # insert_data(data1)
# # #
# # #
# # #
# # #
# # #
# #
# # # import json
# # # import pymongo
# # # from pymongo import MongoClient
# # #
# # # if __name__ == '__main__':
# #
# # # connection = pymongo.MongoClient('localhost', 27017)
# # # database = connection['mydb_10']
# # # collection = database['mycoll_10']
# # # print("Database Connected")
# # # cursor = collection.find({})
# # # file = open("collection.json", "w")
# # # file.write('[')
# # # for document in cursor:
# # #     file.write(json.dumps(document))
# # #     file.write(',')
# # # file.write(']')
# #
# #
# # # def writeToJSONFile(collection):
# # #     cursor = collection.find({})
# # #
# # #     file = open("collection.json", "w")
# # #     file.write('[')
# # #
# # #     qnt_cursor = 0
# # #     for document in cursor:
# # #         qnt_cursor += 1
# # #         num_max = cursor.count()
# # #         if (num_max == 1):
# # #             file.write(json.dumps(document, indent=4, default=json_util.default))
# # #         elif (num_max >= 1 and qnt_cursor <= num_max - 1):
# # #             file.write(json.dumps(document, indent=4, default=json_util.default))
# # #             file.write(',')
# # #         elif (qnt_cursor == num_max):
# # #             file.write(json.dumps(document, indent=4, default=json_util.default))
# # #     file.write(']')
# # #     return file
# #
