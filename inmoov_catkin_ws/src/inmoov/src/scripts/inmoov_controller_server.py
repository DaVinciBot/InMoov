#!/usr/bin/env python

import rospy
import roslib;

from std_msgs.msg import UInt8

import actionlib

from inmoov.msg import *

class RobotControl(object):
    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, RobotControlAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

        self.feedback = RobotControlFeedback()
        self.result = RobotControlResult()
      
    def execute_cb(self, goal):
        self.topics = goal.topics
        self.data = goal.data

        for i in range(0, len(self.topics)):
            print("Publishing : " + self.topics[i] + " => " + str(self.data[i]))
            pub = rospy.Publisher(self.topics[i], UInt8, queue_size=10)
            pub.publish(self.data[i])
            rospy.sleep(0.1)

        self._as.set_succeeded(self.result)
        
if __name__ == '__main__':
    rospy.init_node('inmoov_controller_server')
    print("Starting controller action server")
    server = RobotControl(rospy.get_name())
    rospy.spin()

