# -*- coding:utf-8 -*-
#@InnerAc
#calData.py
"""
When you run start.py or do not want to continue to climb, the first should run the program.
It is used to build up the relationship.
"""
import sqlite3
import re

conn = None

def init(path):
	global conn
	conn = sqlite3.connect(path)
	   
def insert(one,two):
	global conn
	try:
		sqlInsert = "INSERT INTO link \
		(name_one,name_two,value) \
		 VALUES ('{}','{}','{}')".format(one,two,1)
		conn.execute(sqlInsert);
		conn.commit()
	except:
		pass
def select():
	global conn
	cursor = conn.execute("SELECT url, friend From person")
	i = 0
	for row in cursor:
		if i%100 == 0:
			print i
		i += 1
		one = row[0]
		if len(row[1]) > 0:
			names = re.split(',',row[1])
			for name in names:
				if cmp(one,name) > 0:
					insert(name,one)
				else:
					insert(one,name)
def close():
	global conn
	conn.close()	
def start():
	init("person.db")
	select()
	close()
	
if __name__ == '__main__':
	start()