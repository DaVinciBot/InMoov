#!/usr/bin/env python

import datetime
from addon import AddOn

class Control:
    def __init__(self, control_json, addon):
        self.control_json = control_json
        self.addon = addon
        self.date = datetime.datetime.now().isoformat()