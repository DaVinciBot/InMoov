#!/usr/bin/env python

import string, random
import datetime

class AddOn:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_date = datetime.datetime.now().isoformat()
        self.token = ''.join(random.choice(string.letters + string.digits) for _ in range(64))
