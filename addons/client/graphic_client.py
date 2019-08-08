#!/usr/bin/python3

from tkinter import *
import requests, json, os

S = requests.Session()
protocol = ''
host = ''
port = ''
api_token = ''

class MainGUI():
	def __init__(self, master):
		self.master = master
		master.geometry('1000x500')
		master.title("InMoov Application v1.0")

		self.menubar = Menu(master)
		self.menubar.add_command(label="Connect", command=self.connect_popup)
		self.menubar.add_separator()
		self.menubar.add_command(label="Disconnect", state="disabled",command=self.disconnect)
		self.menubar.add_separator()
		self.menubar.add_command(label="Exit", command=self.exit)

		master.configure(menu=self.menubar)

		self.message_label = Label(master, text="Please connect to InMoov first !")
		self.error_label = Label(master, text="")
		self.head_left_button = Button(master, state="disabled", text="Turn head left", command=lambda: self.move_inmoov({'part' : 'head', 'move' : 'turn_left'}))
		self.head_right_button = Button(master, state="disabled", text="Turn head right", command=lambda: self.move_inmoov({'part' : 'head', 'move' : 'turn_right'}))

		self.message_label.pack()
		self.error_label.pack()
		self.head_left_button.pack(side="left")
		self.head_right_button.pack(side="right")

	def move_inmoov(self, arg):
		print("Request : " + str(arg))
		arg['api_token'] = api_token
		url = protocol + "://" + host + ":" + port + "/api"
		r = requests.post(url, json={"api_token": api_token, "move" : "turn_left", "part" : "head"})
		print(r.text)
		try:
			ret = json.loads(r.text)
			print("Response : " + str(ret['msg']))
			self.error_label['text'] = ""
		except:
			self.error_label['text'] = "Error while connecting. Please verify your connection parameters"
			print("Error while connecting. Please verify your connection parameters")

	def connect_popup(self):

		self.popup = Toplevel(self.master)
		self.label = Label(self.popup, text='Connect').grid(row=0,column=1)
		self.label2 = Label(self.popup, text='Protocol').grid(row=1,column=0)
		self.label3 = Label(self.popup, text='Host').grid(row=2,column=0)

		self.label4 = Label(self.popup, text='Port').grid(row=3,column=0)

		self.B1 = Button(self.popup, text="Okay", command = self.connect).grid(row=4,column=0)
		self.B2 = Button(self.popup, text="Cancel", command = self.popup.destroy).grid(row=4,column=1)	

		self.entry1 = Entry(self.popup).grid(row=1,column=1)
		self.entry2 = Entry(self.popup).grid(row=2,column=1)
		self.entry3 = Entry(self.popup).grid(row=3,column=1)
		self.entry1.pack()
		self.entry2.pack()
		self.entry3.pack()
		self.B1.pack()
		self.B2.pack()
		self.entry1.focus_set()



	def connect(self):
		if self.popup:
			self.menubar.entryconfig("Disconnect" ,state = "normal")
			self.menubar.entryconfig("Connect" ,state = "disabled")
			self.head_left_button['state'] = "normal"
			self.head_right_button['state'] = "normal"
			self.message_label['text'] = "You can select actions by clicking buttons below"
			protocol = self.entry1.get()
			host = self.entry2.get()
			port = self.entry3.get()
			print("Connected ! Protocol : %s, Host : %s, Port : %s" % (protocol, host, port))
			self.popup.destroy()
		else:
			print("Connexion failed !")

	def disconnect(self):
		self.menubar.entryconfig("Disconnect" ,state = "disabled")
		self.menubar.entryconfig("Connect" ,state = "normal")
		self.head_left_button['state'] = "disabled"
		self.head_right_button['state'] = "disabled"
		
		protocol = ""
		host = ""
		port = ""

		self.message_label['text'] = "Please connect to InMoov first !"
		print("Disconnected !")

	def exit(self):
		print("Exiting...")
		exit()

if __name__ == '__main__':
	window = Tk()
	my_gui = MainGUI(window)
	window.mainloop()


