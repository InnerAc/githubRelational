# -*- coding:utf-8 -*-
#@InnerAc
#getNum.py
"""
By this program, you can get the JSON file of nodes and edges.
"""
import sqlite3
import math
import json
import re

conn = None

def init(path):
	global conn
	conn = sqlite3.connect(path)
def getNodes():
	global conn
	cursor = conn.execute("SELECT url, name, size FROM node")
	nodes = {}
	i = 0;
	for row in cursor:
		url = row[0]
		name = row[1]
		size = row[2]
		nodes[url] = {"name":name,"size":size}
		i += 1
		if(i == 50):
			break;
		# if i == 10:
		# 	break;
	return nodes
def getLinks(nodes):
	global conn
	cursor = conn.execute("SELECT name_one,name_two,value FROM value")
	edges = []
	i = 0;
	for row in cursor:
		one = row[0]
		two = row[1]
		value = row[2]
		if one in nodes or two in nodes:
			edges.append({"source": one,"target": two,"weight": value})
		# i += 1
		# if i == 10:
			# break;
	return edges
def close():
	global conn
	conn.close()	
if __name__ == '__main__':
	init("person.db")
	info = {}
	nodes = getNodes()
	edges = getLinks(nodes)
	info["nodes"] = nodes
	info["edges"] = edges
	f = open('info.json','w')
	f.write(json.dumps(info))
	f.close()
	close()
