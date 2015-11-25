#encoding=utf-8
#@InnerAc
#start.py
import getPage
import threading
import time
from Queue import Queue

all_set = set()
queue = Queue()

def crawle():
	while(~queue.empty()):
		try:
			name = queue.get()
			nexts = getPage.start(name)
			nexts = nexts - all_set
			all_set.update(nexts)
			nexts = list(nexts)
			for n in nexts:
				queue.put(n)
		except:
			print 'Error!!'
			
		time.sleep(0.01)
	print 'close'


if __name__ == '__main__':
	name1 = 'innerac'
	name2 = 'sunzequn'
	name3 = 'jetmuffin'
	all_set = set([name1,name2,name3])
	queue.put(name1)
	queue.put(name2)
	queue.put(name3)

	ts = []
	
	# sql.createTable()
	
	for i in range(100):
		t = threading.Thread(target=crawle)
		ts.append(t)
	for t in ts:
		t.setDaemon(True)
		t.start()
	t.join()
