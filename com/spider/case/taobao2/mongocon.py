import pymongo

class mongocon:
    def __init__(self,url,name,pwd,database):
        self.url = url
        self.name = name
        self.pwd = pwd
        self.database = database
        self.db = pymongo.MongoClient(url)[database]

    def insert_many(self,collection,coll_name):
        self.db[coll_name].insert_many(collection)

    def insert_one(self,one,coll_name):
        self.db[coll_name].insert_one(one)


