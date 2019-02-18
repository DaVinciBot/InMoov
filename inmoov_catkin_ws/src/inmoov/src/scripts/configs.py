#!/usr/bin/env python

import os
import glob
import json

import rospkg
import roslib; roslib.load_manifest('inmoov')

from json_utils import *

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
            self.paths += (Path_Finder_Json(js).path)

    def create_control_json(self):
        for path in self.paths:
            self.control_json = Path_Generator_Json(self.control_json, path).json

    def get_control_json(self):
        return self.control_json

    def get_topics(self):
        return self.paths

#print Config().get_control_json()

#Json_Writer(Config().get_control_json(), pkg + "/inmoov/config/robot/inmoov_control.json")
#print Value_Finder_Json(Config().get_control_json(), "/robot/head/mouth/servo/angle").value