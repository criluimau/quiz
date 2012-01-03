#!/usr/bin/python
# -*- coding: utf-8 -*-,

import sys, utente

try:  
	import pygtk
	pygtk.require("2.0")  
except:  
	pass  
try:  
	import gtk  
	import gtk.glade  
except:  
	print("GTK Not Availible")
	sys.exit(1)

class login:
	wTree = None

	def __init__( self, db):
		self.window = ""
		self.__cambio_window("windowMain")
		self.db	= db
		dic = {
		"on_ButtonAccedi_clicked" : self.accedi,
		"on_ButtonNuovo_clicked" : self.insuser,
		"on_windowMain_destroy" : self.quit,
		"on_ButtonAccedi1_clicked" : self.quit,
		"on_windowUser_destroy" : self.accedi,
		}
		self.wTree.signal_autoconnect( dic )		
		gtk.main()
		
	def __cambio_window(self, s):
		if self.window != s:
			self.window= s			
			self.wTree 	= gtk.glade.XML( "login.glade", self.window )
			
	def accedi(self, widget):
		self.__cambio_window("windowMain")			
		self.user_name   = self.wTree.get_widget("user_name").get_text()
		self.user_passwd = self.wTree.get_widget("user_passwd").get_text()
		if self.user_name == "" or self.user_passwd == "":
			self.wTree.get_widget("hboxWarning").show()
			self.wTree.get_widget("messages").set_text("inserire utente e password")
		else:
			user	 	= utente.utente(self.db, self.user_name)
			autenticato	= user.controlla_password(self.user_passwd)
			if autenticato == False:
				self.wTree.get_widget("hboxWarning").show()
				self.wTree.get_widget("messages").set_text("utente o password errata")
			else:
				self.wTree.get_widget("hboxWarning").hide()
				self.wTree.get_widget("messages").set_text("utente connesso")		

	def insuser(self, widget):
		self.__cambio_window("windowUser")
		self.user_name   = self.wTree.get_widget("user_name1").get_text()
		self.user_passwd = self.wTree.get_widget("user_passwd1").get_text()
		user	 	= utente.utente(self.db, self.user_name)
		autenticato	= user.controlla_password(self.user_passwd)
		print autenticato, self.user_name, self.user_passwd
		if autenticato == False:
			self.wTree.get_widget("hboxWarning1").show()
			self.wTree.get_widget("messages1").set_text("ins.utente da fare")
		else:
			self.wTree.get_widget("hboxWarning1").show()
			self.wTree.get_widget("messages1").set_text("ins.utente da fare")

	def quit(self, widget):
		sys.exit(0)
