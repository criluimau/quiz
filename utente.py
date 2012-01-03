#!/usr/bin/python
#! -*- coding: utf-8 -*-

class utente:

	def __init__(self, db, n):
		self.__name	  = n
		self.__passwd = ""
		self.db1 = db
		
	def inserisci_utente(self,s):
		self.__passwd = s
		err=self.db1.insert("utente (login, pass) VALUES('"+self.__name+"','"+self.__passwd+"')")
		return err
		
	def controlla_utente(self,s):
		self.__name = s
		select= self.db1.select("*","utente WHERE login='"+self.__name+"'")
		if len(select) > 0:
			valido=True
		else:
			valido=False
		return valido
		
	def controlla_password(self,s):
		self.__passwd = s
		select= self.db1.select("*","utente WHERE login='"+self.__name+"' AND pass='"+self.__passwd+"'")
		if len(select) > 0:
			valido=True
		else:
			valido=False
		return valido

