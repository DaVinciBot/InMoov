#!/usr/bin/env python

#db.addons.createIndex({ "name" : 1 }, { unique : true })

from pymongo import MongoClient, errors

import json

from addon.addon import AddOn
from control.control import Control

class InMoov_DB:
    def __init__(self):
        self.connect_to_db()

    def connect_to_db(self):
        client = MongoClient('mongodb://localhost:27017/')

        db = client.inmoov

        self.addons = db.addons
        self.controls = db.controls

    def create_addon(self, name, email):
        addon = AddOn(name, email)

        collection = self.addons

        try:
            collection.insert(addon.__dict__)
            return self.get_addon_token(name)
        except errors.DuplicateKeyError as e:
            print(e)

    def create_control(self, control_json, addon):
        control = Control(control_json, addon)

        collection = self.controls

        try:
            collection.insert(control.__dict__)
        except errors.DuplicateKeyError as e:
            print(e)

    def get_addon(self, name):
        collection = self.addons

        return collection.find_one({"name": name})

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
            print(addon)


#InMoov_DB().create_control({}, AddOn("Hello_World_2", "test").__dict__)