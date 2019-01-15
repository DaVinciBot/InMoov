#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy,time,json
from std_msgs.msg import String

#Les callback
def callback(msg):
        rospy.loginfo('Move request received : ' + msg.data)

#Les subscribers
rospy.Subscriber('master_topic', String, callback)

#Le code
def Master():
	rospy.init_node('master_node', anonymous=True)
	rospy.loginfo("[MASTER] Démarrage de ROS...")

if __name__ == '__main__':
	try:
		Master()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
