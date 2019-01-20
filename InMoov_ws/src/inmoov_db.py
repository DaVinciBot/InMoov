#!/usr/bin/env python

import json
import datetime

from pymongo import MongoClient

def connect_to_db():
    client = MongoClient('mongodb://localhost:27017/')

    db = client.inmoov

    return db

def get_all_users():
    db = connect_to_db()

    return db.users.find({})

def is_token_exists(token):
    db = connect_to_db()

    if db.users.find_one({"token": token}):
        return True

    else:
        return False

def print_all_users():
    for user in get_all_users():
        print user


#print_all_users()

#print is_token_exists("424ccf1fe53adeeb01953d09818a5a717f3f17a0221d5bc5c03cad68ee1c6881")


