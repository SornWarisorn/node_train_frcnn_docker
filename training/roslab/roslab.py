#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
import rospy
from std_msgs.msg import String
import cv2
import yaml
import json
import base64
from PIL import Image
import numpy as np


class Node():

    def __init__(self,node):
        self.node = node
        self._on_loop = None
        self.idx = 0
        self.folders_load = False
        

    def connect(self):
        #if self.folders_load == True:
            rospy.init_node(self.node)

    def forever_loop(self,hz=10):
        rate = rospy.Rate(hz)
        while not rospy.is_shutdown():
            self.on_loop()
            rate.sleep()

    @property
    def on_loop(self):
        return self._on_loop

    @on_loop.setter
    def on_loop(self, func):
        self._on_loop = func



    class message():
        def __init__(self,obj=None):
            if obj != None:
                self.obj_node = obj['node']
                self.obj_topic = obj['topic']
            else:
                self.obj_node = ""
                self.obj_topic = ""

            self.key = []
            self.value = []



            self.syntax = {}
            self.result = {}




        def KeyValue(self,key,value):
            self.key.append(key)
            self.value.append(value)
            self.result = dict(zip(self.key,self.value))
            self.syntax ={
                            'from_to' :{
                                    'obj_node': str(self.obj_node) , 
                                    'obj_topic' :  str(self.obj_topic)
                            },
                            'result':[ self.result]

            }
            return self.syntax







            





    class Publisher():
	
        def __init__(self,topic,node_name,queue_size):
             self.pub = rospy.Publisher(topic, String,queue_size=queue_size)
             self.topic = topic
             self.node_name = node_name

        def send(self,msg):
             msgs = {
                 'node':self.node_name,
                 'topic':self.topic,
                 'msg':[
                          msg
                 ]
                    }
             json_msg = json.dumps(msgs)
             self.pub.publish(String(json_msg))




    class Subscriber():
	
         def callback(self,msg,idx):
             ja = json.loads(msg.data)
             self.on_callback(ja,idx)

         def __init__(self,topic,node_name,idx):
             self.idx = idx
             self.sub = rospy.Subscriber(topic, String, self.callback,self.idx)
             self.topic = topic
             self.node_name = node_name
             self._on_callback = None

         @property
         def on_callback(self):
             return self._on_callback

         @on_callback.setter
         def on_callback(self, func):
             self._on_callback = func



    def publish(self,topic,queue_size=1):
        #if not rospy.is_shutdown():
        pub = self.Publisher(topic, self.node,queue_size)
        return pub


    def subscriber(self,topic):
        #if not rospy.is_shutdown():
        sub = self.Subscriber(topic, self.node,self.idx)
        self.idx = self.idx + 1
        return sub


    def load(self,filename):
        with open(os.path.join("../","config",filename),'r') as reads:
             yaml_object = yaml.load(reads)
            
             j = json.dumps(yaml_object)
        self.folders_load = True
        ja = json.loads(j)
        return ja

    def load_yaml(self,filename):
		#yaml = YAML()
        with open(os.path.join("../","config",filename),'r') as reads:
             code = yaml.load(reads)
        return code	
		

    
