import socket
from threading import Thread
import sys
import Tkinter
class Client:
	def __init__(self,port,host):
		self.client = socket.socket();
		self.client.connect((port,host))
		self.run()

	def run(self):
		    t = Thread(target =
			    self.recive)
		    t.start()

		    self.create_frame("Server")
		    Tkinter.mainloop()
	
	def send(self):
		message = self.input.get();
		self.client.send(message)
		show = "me : " + message
		self.message_list.insert(Tkinter.END, show)
		self.input.set("")

	def recive(self):
		while True:
		    message = self.client.recv(1024)
		    show = "server : " + message
		    self.message_list.insert(Tkinter.END, show)

	
	def create_frame(self,name):
		top = Tkinter.Tk()
		top.title(name)
		self.frame = Tkinter.Frame(top)
	    	self.input = Tkinter.StringVar()
	    	scrollbar = Tkinter.Scrollbar(self.frame)
	    	self.message_list = Tkinter.Listbox(self.frame, height=15, width=50, yscrollcommand=scrollbar.set)
	    	scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
	    	self.message_list.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
	    	self.message_list.pack()
	    	self.frame.pack()
	    	
	    	entry_field = Tkinter.Entry(top, textvariable=self.input)
		#entry_field.bind("<Return>", self.send)
	    	entry_field.pack()
	    	send_button = Tkinter.Button(top, text="Send", command=self.send)
	    	send_button.pack()
	    	


c1 = Client('172.17.8.111',9991)
