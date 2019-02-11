#!/usr/bin/python3
#-*- coding: utf-8 -*-

import rospy,time,json
from std_msgs.msg import String

#Les callback
def dispatcher_callback(msg):
        rospy.loginfo('[Dispatcher] Move request : ' + msg.data)

#Les subscribers
rospy.Subscriber('dispatcher_topic', String, dispatcher_callback)

if __name__ == '__main__':
	try:
		rospy.init_node('dispatcher_node', anonymous=True)
		rospy.loginfo("[Dispatcher] Starting ...")
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
