# -*- coding:utf-8 -*-
#@InnerAc
#calPerson.py
"""
When you already run calValue.py, you can run the program.
It is used to build up the info of node.
"""
import sqlite3
import math
import re

conn = None

def getInt(s):
	return int(float(s[0:-1]) * 1000)

def init(path):
	global conn
	conn = sqlite3.connect(path)

def insert(url,name,size):
	global conn
	try:
		sqlInsert = "INSERT INTO node \
		(url,name,size) \
		 VALUES ('{}','{}','{}')".format(url,name,size)
		conn.execute(sqlInsert);
	except:
		pass
def select():
	global conn
	cursor = conn.execute("SELECT url, name, star,follower FROM person")
	i = 0
	for row in cursor:
		url = row[0]
		name = row[1]
		star = row[2]
		follower = row[3]
		
		# print url,name,star,follower
		
		if follower > 1000:
			follower = getInt(follower)
		if star > 1000:
			star = getInt(star)
		size = int(math.ceil(math.log(follower+1) + math.log(star+1)+1))
		if size < 0:
			size = 1
		insert(url,name,size)
		# print url,name,size
		if i%100 == 0:
			print i
			conn.commit()
			print i
		i += 1
def close():
	global conn
	conn.commit()
	conn.close()	
def start():
	init("person.db")
	select()
	close()
	
if __name__ == '__main__':
	start()