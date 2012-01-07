#!/usr/bin/python
# -*- coding: utf-8 -*-,

import sys, utente

try:  
	import gtk, pygtk
except:  
	print("gtk o pygtk Not Availible")
	sys.exit(1)

class login:
	wTree 		= None
	FinePgm 	= False
	UserName 	= None

	def __init__( self, db):
		self.db	= db

		# dizionario dei segnali
		dic = {
		"on_ButtonConferma_clicked":	self.accedi,
		"on_ButtonNuovo_clicked" : 		self.newuser,
		"on_ButtonEsci_clicked" : 		self.esci,
		"on_WindowLogin_destroy" : 		self.esci,
		}

		self.gladefile = "login.glade" 
		self.previousWindow = ""
		# Il collegamento al file XML
		self.wTree = gtk.Builder()
		self.wTree.add_from_file(self.gladefile)
		# Utilizzo finestra
		self.CambioWindow("WindowLogin", "Login")
		# intercetta i segnali
		self.wTree.connect_signals(dic)
		
	def CambioWindow(self, Tree, TreeBox ):
		if Tree == "WindowLogin":
			self.wTree.get_object("WindowLogin").set_sensitive(1)
			self.wTree.get_object("WindowLogin").set_visible(1)
			self.wTree.get_object("hboxWarning").set_visible(0)
			if TreeBox == "Login":
				self.wTree.get_object("hbox3").set_visible(0)
				self.wTree.get_object("hbox5").set_visible(1)
			else:
				self.wTree.get_object("hbox3").set_visible(1)
				self.wTree.get_object("hbox5").set_visible(0)

		if self.previousWindow != Tree:
			self.previousWindow= Tree	
			self.currentWindow = self.wTree.get_object(Tree)

		self.currentWindow.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.currentWindow.set_default_size(210, 60)
		self.currentWindow.show()
			
	def accedi(self, widget):
		self.CambioWindow("WindowLogin", "Login")
		self.UserName   = self.wTree.get_object("UserName").get_text()
		self.Password   = self.wTree.get_object("Password").get_text()
		autenticato     = self.autenticati()
		if self.FinePgm:
			self.esci(widget)
		elif autenticato:
			self.fine(widget)
	
	def newuser(self, widget):
		self.CambioWindow("WindowLogin", "NewUser")
		self.UserName    = self.wTree.get_object("UserName").get_text()
		self.Password    = self.wTree.get_object("Password").get_text()
		self.PasswordNew = self.wTree.get_object("PasswordNew").get_text()
		while len(self.UserName == 0):
			self.wTree.get_object("hboxWarning").show()
			self.wTree.get_object("MsgWarning").set_text("Inserisci un nome utente valido")
		while len(self.Password) == 0:
			self.wTree.get_object("hboxWarning").show()
			self.wTree.get_object("MsgWarning").set_text("Inserisci una password valida")
		while self.Password != self.PasswordNew or len(self.Password) == 0:
			self.wTree.get_object("hboxWarning").show()
			self.wTree.get_object("MsgWarning").set_text("le due password sono diverse")

		autenticato      = self.autenticati()
		print autenticato, self.FinePgm
		if self.FinePgm:
			self.esci(widget)
		elif autenticato:
			self.fine(widget)

	def autenticati(self):
		autenticato = False
		if self.UserName == "" or self.Password == "":
			self.wTree.get_object("hboxWarning").show()
			self.wTree.get_object("MsgWarning").set_text("inserire utente e password")
		else:
			user	 	= utente.utente(self.db, self.UserName)
			RispFun 	= user.controlla_password(self.Password)
			autenticato = RispFun[0]
			msg         = RispFun[1]
			if not autenticato:
				self.wTree.get_object("hboxWarning").show()
				self.wTree.get_object("MsgWarning").set_text("utente o password errata")
			else:
				self.wTree.get_object("hboxWarning").hide()
				self.wTree.get_object("MsgWarning").set_text("utente connesso")
		return autenticato	

	def main(self):
		gtk.main()
		RispFun = []
		RispFun.append(self.FinePgm)
		RispFun.append(self.UserName)
		return RispFun		

	def esci(self, widget):
		if self.FinePgm == "forced":
			self.FinePgm = "forced1"
		elif self.FinePgm == "forced1":
			self.FinePgm = False
		else:
			self.FinePgm = True
		gtk.main_quit()	
		
	def fine(self, widget):	
		self.FinePgm = "forced"
		self.wTree.get_object("WindowLogin").destroy()
		self.esci(widget)
	
