#! /usr/bin/env python
# -*- coding: utf-8 -*-

from roslab import *
import datetime
import time
import json
import edit_faster as editf
import edit_pipeline as editp

if __name__ == '__main__':	
	## การตั้งชื่อ node ##
	node = Node(node="??????")	
	## การดึงค่า config ต่างๆมาใช้งาน ##

	json_config = node.load(filename="config_train.yaml")

	number = json_config["number"]
	Path = json_config["Path"]

	editf.edit_faster(number,Path)
	
	editp.edit_pipeline(number,Path)

	

	
























