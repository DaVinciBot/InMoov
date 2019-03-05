#!/usr/bin/env python

import os
import datetime

class AddOn:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_date = datetime.datetime.now().isoformat()
        self.token = os.urandom(32).encode('hex')