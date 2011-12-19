#!/usr/bin/env python
#
# Small test to demonstrate glade.XML.signal_autoconnect on an instance
#
 
import pygtk
pygtk.require('2.0')

import gtk, gtk.glade

class Bottoncino:
	
	def __init__(self,n):
		self.n = n
		xml = gtk.glade.XML('interface1.glade')
		xml.signal_autoconnect(self)
		print self.n

	def click_b1(self, button):
		print 'Click ... creo istanza n. '+str(self.n+1)
		b = Bottoncino(self.n+1)
		

test = Bottoncino(1)
gtk.main()
