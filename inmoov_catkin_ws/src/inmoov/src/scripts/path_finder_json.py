#!/usr/bin/env python

import json
import rospy
import rospkg

import roslib; roslib.load_manifest('robot')

from std_msgs.msg import Int16

class Load_Configs:
    def __init__(self):
        self.config_files = []
        self.topics = []

    def list_to_string(self, liste, split_key):
        string = ""

        for key in liste:
            string += split_key + key

        return string
    
    def create_topics_from_config(self, config, path):
        for key, value in config.items():
            if "control" in config.keys() and path:
                self.topics.append(self.list_to_string(path, "/"))
                break

            if isinstance(value, dict):
                path.append(key)
                self.create_topics_from_config(config[key], path)

        if path:
            path.pop() 

    def create_all_topics(self):
        for config_file in self.config_files:
            config = json.load(open(config_file))
            self.create_topics_from_config(config, [])

    def get_topics(self):
        return self.topics


class Dispatcher:
    def __init__(self, topics=[]):
        self.control_file = None
        self.control_json = {}

        self.topics = topics

    def update_control_json_from_topic(self, json, topic, index):
        if index < len(topic):
            if topic[index] == "angle":
                json["angle"] = 0
                return
            
            if topic[index] in json.keys():
                self.update_control_json_from_topic(json[topic[index]], topic, index + 1)
            else:
                json[topic[index]] = {}
                self.update_control_json_from_topic(json, topic, index)

    def get_control_json(self):
        print self.topics
        for topic in self.topics:
            liste = topic.split("/")
            self.update_control_json_from_topic(self.control_json, liste, 1)

        return self.control_json

    def write_control_json(self):
        self.get_control_json()
        self.control_file.write(json.dumps(self.control_json, indent=4))

    def dispatch(self):
        rospy.init_node("test")
        while not rospy.is_shutdown():
            for topic in self.topics:
                pub = rospy.Publisher(topic, Int16, queue_size=10)
                pub.publish(Int16(0))


pkg = rospkg.get_ros_paths()[1]

configs = Load_Configs()
configs.config_files.append(pkg + "/robot/config/robot/head.json")
configs.config_files.append(pkg + "/robot/config/robot/arm.json")

configs.create_all_topics()

dispatcher = Dispatcher(configs.get_topics())
dispatcher.control_file = open("./src/robot/config/robot/control.json", "w")

dispatcher.write_control_json()

dispatcher.dispatch()