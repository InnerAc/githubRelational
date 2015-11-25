# -*- coding:utf-8 -*-
#@InnerAc
#calValue.py
"""
When you already run calData.py, you can run the program.
It is used to build up the weight of relationship.
"""
import sqlite3
import re

conn = None

def init(path):
	global conn
	conn = sqlite3.connect(path)
	
def createTable():
	global conn

	   
def insert(one,two,n):
	global conn
	try:
		sqlInsert = "INSERT INTO value \
		(name_one,name_two,value) \
		 VALUES ('{}','{}','{}')".format(one,two,n)
		conn.execute(sqlInsert);
	except:
		pass
def select():
	global conn
	cursor = conn.execute("SELECT name_one, name_two FROM link")
	i = 0
	for row in cursor:
		one = row[0]
		two = row[1]
		# print one,two
		sqls = "SELECT friend FROM person WHERE url='{}'".format(one)
		one_n = conn.execute(sqls)
		for x in one_n:
			one_f = re.split(',',x[0])
		sqls = "SELECT friend FROM person WHERE url='{}'".format(two)
		one_n = conn.execute(sqls)
		for x in one_n:
			two_f = re.split(',',x[0]) 
		n = len(set(one_f) & set(two_f))
		# print n
		insert(one,two,n+1)
		if i%100 ==0:
			conn.commit()
			if i == 500:
				break;
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