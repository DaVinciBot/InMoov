#!/usr/bin/env python
#coding: utf-8

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

        self.config = Config()
	#initialisation du control_json par defaut avec des 0
        self.control_json = self.config.get_control_json()
        self.topics = self.config.get_topics()
        self.data = []
        self.load_data()

        self.client = actionlib.SimpleActionClient('inmoov', RobotControlAction)

        self.goal = RobotControlGoal()

        self.client.wait_for_server()
#	print('test_init')


    def get_control_json(self):
        return self.control_json

    def update_control_json(self, new_control_json):
        print(new_control_json)
        self.control_json = new_control_json
        self.load_data()

    def send_goal(self, addon_emetteur):

        self.db.create_control(self.control_json, addon_emetteur)

        self.goal.topics = self.topics
        self.goal.data = self.data

        self.client.send_goal(self.goal)

        self.client.wait_for_result()
        return self.client.get_result()

    #methode de test
    def send_goal_from_file(self):
	#control json d'exemple pour tester
        self.control_json = Reader(self.config.pkg + "/inmoov/control/inmoov_control.json").js
        self.load_data()
        self.send_goal("test")

    #associé a la methode de test
    def load_data(self):
        for i in range(0, len(self.topics)):
            data = Value_Finder(self.control_json, self.topics[i]).value
            msg = UInt8(data)
            self.data.insert(i, msg)

if __name__ == '__main__':
    rospy.init_node('test')
    print('test3')
    inmoov = InMoov_Controller_Client()
    print('test')
    inmoov.send_goal_from_file()
    print('test2')
    rospy.spin()
