#!/usr/bin/env python

#import sys
#sys.path.append('~/Documents/dvb_ws/DaVinciBot-InMoov/inmoov_catkin_ws/src/inmoov/src/scripts')

import rospy
import roslib; roslib.load_manifest('inmoov')

import json

from std_msgs.msg import UInt8

import actionlib
from inmoov.msg import *

from configs.configs import Config
from utils.json_utils import Value_Finder, Reader

from inmoov_db.inmoov_db import InMoov_DB
from addon.addon import AddOn
from control.control import Control

class InMoov_Controller_Client:
    def __init__(self):
        self.db = InMoov_DB()

        self.addon = self.db.get_addon('Hello_World')

        self.config = Config()
        self.control_json = self.config.get_control_json()
        self.topics = self.config.get_topics()
        self.data = []
        self.load_data()

        self.client = actionlib.SimpleActionClient('inmoov', RobotControlAction)
        self.goal = RobotControlGoal()

        self.client.wait_for_server()

    def send_goal(self):

        self.db.create_control(self.control_json, self.addon)

        self.goal.topics = self.topics
        self.goal.data = self.data

        self.client.send_goal(self.goal)

        self.client.wait_for_result()
        
        return self.client.get_result()

    def send_goal_from_file(self):
        self.control_json = Reader(self.config.pkg + "/inmoov/control/inmoov_control.json").js
        self.load_data()
        self.send_goal()

    def load_data(self):
        for i in range(0, len(self.topics)):
            data = Value_Finder(self.control_json, self.topics[i]).value
            msg = UInt8(data)
            self.data.insert(i, msg)

rospy.init_node('test')

inmoov = InMoov_Controller_Client()

inmoov.send_goal_from_file()

rospy.spin()