# -*- coding:utf-8 -*-
#@InnerAc
#create tables of database.You should run the program first
import sqlite3

conn = None

def init(path):
	global conn
	conn = sqlite3.connect(path)
	
def createTable():
	global conn
	conn.execute('''
		CREATE TABLE person(
		url	TEXT PRIMARY	KEY		NOT NULL,
		name			TEXT	NOT NULL,
		organization	TEXT,
		location		TEXT,
		mail			TEXT,
		link			TEXT,
		clock			TEXT,
		star			INT,
		following		INT,
		follower		INT,
		friend			TEXT
		);
	   ''')
	conn.execute('''
		CREATE TABLE link(
		name_one		TEXT	NOT NULL,
		name_two		TEXT	NOT NULL,
		value			INT,
		primary key (name_one,name_two)
		);
	   ''')
	conn.execute('''
		CREATE TABLE node(
		url	TEXT PRIMARY	KEY		NOT NULL,
		name			TEXT	NOT NULL,
		size			INT
		);
	   ''')
	conn.execute('''
		CREATE TABLE value(
		name_one		TEXT	NOT NULL,
		name_two		TEXT	NOT NULL,
		value			INT,
		primary key (name_one,name_two)
		);
	   ''')	
if __name__ == '__main__':
	init("person.db")
	createTable()