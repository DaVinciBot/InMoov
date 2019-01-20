#!/usr/bin/env python

#db.addons.createIndex({ "name" : 1 }, { unique : true })

from pymongo import MongoClient, errors

from addon import AddOn

class InMoov_DB:
    def __init__(self):
        self.connect_to_db()

    def connect_to_db(self):
        client = MongoClient('mongodb://localhost:27017/')

        db = client.inmoov

        self.addons = db.addons

    def create_addon(self, name, email):
        addon = AddOn(name, email)

        collection = self.addons

        try:
            collection.insert(addon.__dict__)
            return self.get_addon_token(name)
        except errors.DuplicateKeyError as e:
            print e

    def get_addon_token(self, name):
        collection = self.addons

        return collection.find_one({"name": name}, {"token": 1, "_id": 0})

    def get_all_addons(self):
        return self.addons.find({})

    def is_addon_token_exists(self, token):
        if self.addons.find_one({"token": token}):
            return True
        else:
            return False

    def print_all_addons(self):
        for addon in self.get_all_addons():
            print addon