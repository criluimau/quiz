#!/usr/bin/python
# -*- coding: utf-8 -*-,

import sys

try:  
	import pygtk
	pygtk.require("2.0")
	import gtk
except:  
	print("gtk o pygtk Not Availible")
	sys.exit(1)

class quizadmin:
	wTree 		= None
	FinePgm     = False
	Scelta 		= 0
	Opzione		= 0

	def __init__( self):
		
		# dizionario dei segnali
		dic = {
		"on_menuitem2_Lista_activate":		self.menu11,
		"on_menuitem2_Cancella_activate":	self.menu12,
		"on_menuitem3_Inserisci_activate":	self.menu21,
		"on_menuitem3_Modifica_activate":	self.menu22,
		"on_menuitem3_Cancella_activate":	self.menu23,
		"on_menuitem4_Inserisci_activate":	self.menu31,
		"on_menuitem4_Cancella_activate":	self.menu32,
		"on_menuitem5_utente_activate":		self.menu41,
		"on_mainWindow_destroy" : 			self.esci,
		}

		self.gladefile = "quizadmin.glade" 
		# Il collegamento al file XML
		self.wTree = gtk.Builder()
		self.wTree.add_from_file(self.gladefile)
		# intercetta i segnali
		self.wTree.connect_signals(dic)

	def menu11(self,widget):		
		self.Scelta  = 1
		self.Opzione = 1
		# =============================
		# testi per widget gtktextview
		# inizializzo textview
		#textview = gtk.TextView()
		#textview=self.gladefile.get_widget(Testo1)
		# puntatore del buffer
		#textbuffer = gtk.TextBuffer()
		# emetto a video
		#textbuffer.set_text('Scriviamo qualcosa all\'interno della TextView')
		#risp=raw_input(" un tasto qualsiasi per continuare ")
		# =============================
		self.fine(widget)

	def menu12(self,widget):
		self.Scelta  = 1
		self.Opzione = 2
		self.fine(widget)

	def menu21(self,widget):
		self.Scelta  = 2
		self.Opzione = 1
		self.fine(widget)

	def menu22(self,widget):
		self.Scelta  = 2
		self.Opzione = 2
		self.fine(widget)
		
	def menu23(self,widget):
		self.Scelta  = 2
		self.Opzione = 3
		self.fine(widget)

	def menu31(self,widget):
		self.Scelta  = 3
		self.Opzione = 1
		self.fine(widget)

	def menu32(self,widget):
		self.Scelta  = 3
		self.Opzione = 2
		self.fine(widget)

	def menu41(self,widget):
		self.Scelta  = 4
		self.Opzione = 1
		self.fine(widget)
	
	def main(self):
		gtk.main()
		RispFun= []
		RispFun.append(self.FinePgm)
		RispFun.append(self.Scelta)
		RispFun.append(self.Opzione)
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
		self.wTree.get_object("mainWindow").destroy()
		self.esci(widget)



