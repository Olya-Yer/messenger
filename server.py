import socket
from threading import Thread, Lock
import Tkinter
class Server:
	def __init__(self, port, host):
		self.server = socket.socket()
		self.server.bind((port, host))
		mutex = Lock()
		self.m = mutex
		self.run()
	def run(self):
		while True:
		    self.server.listen(10)
		    conn, addr = self.server.accept();
		    t = Thread(target =
			    self.conversation,args=(conn,addr))
		    t.start()
	def conversation(self,conn,addr):
		message_list = self.create_frame(addr, conn)
		
		t = Thread(target =
			    self.recive,args=(conn,message_list))
		
		t.start()

		Tkinter.mainloop()

	
	def recive(self,conn, message_list):
		while True:
		    message = conn.recv(1024)
		    message_list.insert(Tkinter.END,message)
	
	def send(self,input_server, message_list, conn):
		message = input_server.get();
		conn.send(message)
		message_list.insert(Tkinter.END,message)


 	def create_frame(self, name, conn):
		top = Tkinter.Tk()
		top.title(name)
		frame = Tkinter.Frame(top)
	    	input_server = Tkinter.StringVar()
	    	scrollbar = Tkinter.Scrollbar(frame)
	    	message_list = Tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
	    	scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
	    	message_list.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
	    	message_list.pack()
	    	frame.pack()
	    	
	    	entry_field = Tkinter.Entry(top, textvariable=input_server)
		#entry_field.bind("<Return>", self.send)
	    	entry_field.pack()
		send_button = Tkinter.Button(top, text="Send", command= lambda :
				self.send(input_server, message_list, conn))
	    	send_button.pack()
	    	
		return message_list
   

s = Server('172.17.8.111',9991);
