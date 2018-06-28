import Queue
import time
import threading as thr

global c
c = 10


class sub_thread(thr.Thread):
	def __init__(self,function_name):
		thr.Thread.__init__(self)
		self.function = function_name
	def run(self):
		print "\nstarting function %s \n"%(self.function.__name__)
		self.function(c)
		print "\nfinished function %s \n"%(self.function.__name__)

def f1(c):
	while c:
		time.sleep(0.1)
		print "this is function %s , counter = %s \n"%(f1.__name__,c)
		c -=1
def f2(c):
	t3 = sub_thread(f3)
	t3.start()
	t3.join()
	while c:
		print "this is function %s , counter = %s \n"%(f2.__name__,c)
		time.sleep(0.1)
		c -=1
def f3(c):
	while c:
#		time.sleep(0.1)
		print "this is function %s , counter = %s \n"%(f3.__name__,c)
		c-=1

tlock = thr.Lock()

t1 = sub_thread(f1)
t2 = sub_thread(f2)

t1.start()
t2.start()
t1.join()
t2.join()
print "suppose this is main\n"
