#!/usr/bin/env python

import os
import glob
import json

import rospkg
import roslib; roslib.load_manifest('inmoov')

from utils.json_utils import *

#####################
# ROBOT CONFIG
# read json config files
# store all servos infos
# get all control node ("control": 1)
# get all monitor node for websockets purpose ("monitor": 1)
# store all publishers
#####################

class Config:
    def __init__(self):
        self.pkg = rospkg.get_ros_paths()[1]
        self.control_json = {}
        self.paths = []
        self.load_config_files()
        self.create_control_json()

    def load_config_files(self):
        for file in glob.glob(self.pkg + "/inmoov/config/robot/*.json"):
            json_file = open(file, "r")
            js = json.load(json_file)
            self.paths += (Path_Finder(js).path)

    def create_control_json(self):
        for path in self.paths:
            self.control_json = Path_Generator(self.control_json, path).json

    def get_control_json(self):
        return self.control_json

    def get_topics(self):
        return self.paths