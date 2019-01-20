#!/usr/bin/env python

import json
import datetime

import os

from inmoov_db import connect_to_db
from pymongo import errors

class User:
    def __init__(self):
        self.first_name = "update"
        self.last_name = ""
        self.email = ""
        self.starting_date = datetime.datetime.now().isoformat()
        self.end_date = self.starting_date 
        self.token = os.urandom(32).encode('hex')

    def get_collection(self):
        db = connect_to_db()

        return db.users

    def post(self):
        collection = self.get_collection()

        try:
            collection.insert(self.__dict__)
            return True
        except errors.DuplicateKeyError as e:
            print e
        else:
            return False


    def get_token(self):
        collection = self.get_collection()

        return collection.find_one({"email": self.email}, {"token": 1, "_id": 0})

def create_user(first_name, last_name, email):
    user = User()

    user.first_name = first_name
    user.last_name = last_name
    user.email = email

    if user.post():
        return user.get_token()

    else:
        return "Problem inserting"

print create_user("Florian", "Quibel", "florian.quibel27@gmail.com")