# -*- coding:utf-8 -*-
#@InnerAc
#getNum.py
"""
By this program, you can specify the number of edges to get the JSON file.
"""
import sqlite3
import math
import json
import re
from Queue import Queue

conn = None
node_set = set()
link_set = set()
queue = Queue()

def init(path):
	global conn
	conn = sqlite3.connect(path)
def getNodes():
	global conn
	nodes = {}
	for node in node_set:
		print node
		try:
			cursor = conn.execute("SELECT url, name, size FROM node WHERE url='{}'".format(node))
			for row in cursor:
				url = row[0]
				name = row[1]
				size = row[2]
				nodes[url] = {"name":name,"size":size}
		except:
			print 'no'
	return nodes
	
def split(one,two):
	return one+'#'+two
def getLinks(maxn):
	global conn
	edges = []
	while(~queue.empty()):
		name = queue.get()
		# print name
		try:
			cursor = conn.execute("SELECT name_one,name_two,value FROM value WHERE name_one = '{}'".format(name))
			for row in cursor:
				one = row[0]
				two = row[1]
				value = row[2]
				if split(one,two) not in link_set:
					link_set.add(split(one,two))
					if two not in node_set:
						queue.put(two)
						node_set.add(two)
					edges.append({"source": one,"target": two,"weight": value})
		except:
			print 'no'
		
		try:
			cursor = conn.execute("SELECT name_one,name_two,value FROM value WHERE name_two = '{}'".format(name))
			for row in cursor:
				one = row[0]
				two = row[1]
				value = row[2]
				if split(one,two) not in link_set:
					link_set.add(split(one,two))
					if one not in node_set:
						queue.put(one)
						node_set.add(one)
					edges.append({"source": one,"target": two,"weight": value})
		except:
			print 'no'
		print len(node_set)
		if(len(node_set) > maxn):
			break;
	return edges
	
def remove(edges):
	new_edges = []
	for edge in edges:
		if edge['source'] in node_set and edge['target'] in node_set:
			new_edges.append(edge)
	return new_edges
	
def getNewLink(nodes):
	edges = []
	for node in nodes:
		try:
			cursor = conn.execute("SELECT name_one,name_two,value FROM value WHERE name_one = '{}'".format(node))
			for row in cursor:
				one = row[0]
				two = row[1]
				value = row[2]
				if split(one,two) not in link_set and two in nodes:
					link_set.add(split(one,two))
					edges.append({"source": one,"target": two,"weight": value})
		except:
			print 'no'
		
		try:
			cursor = conn.execute("SELECT name_one,name_two,value FROM value WHERE name_two = '{}'".format(node))
			for row in cursor:
				one = row[0]
				two = row[1]
				value = row[2]
				if split(one,two) not in link_set and one in nodes:
					link_set.add(split(one,two))
					edges.append({"source": one,"target": two,"weight": value})
		except:
			print 'no'
	return edges
def close():
	global conn
	conn.close()	
	
def write(info):
	f = open('info.json','w')
	f.write(json.dumps(info))
	f.close()
	
def start():
	init("person.db")
	name = 'innerac'
	queue.put(name)
	node_set.add(name)
	info = {}
	edges = getLinks(1000)
	print 'edges'
	nodes = getNodes()
	link_set.clear()
	edges = getNewLink(nodes)
	# edges = remove(edges)
	info["nodes"] = nodes
	info["edges"] = edges
	write(info)
	close()
if __name__ == '__main__':
	start()
