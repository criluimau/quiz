#!/usr/bin/python
#! -*- coding: utf-8 -*-

class utente:

	def __init__(self, db, n):
		self.__id		= 0
		self.__name		= n
		self.__passwd	= ""
		self.db1 		= db
				
	def inserisci_utente(self,s):
		self.__passwd = s
		RispFun = []
		err=self.db1.insert("utente (login, pass) VALUES('"+self.__name+"','"+self.__passwd+"')")
		if not err:
			msg = "Registrazione effettuata con successo, sei ora connesso"
		else:
			msg = "Registrazione non riuscita"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun

	def cancella_utente(self,s):
		utente = s
		RispFun = []
		err=self.db1.delete("utente WHERE login='"+utente+"'")
		if not err:
			msg = "l'utente," +utente+ " è stato cancellato correttamente"
		else:
			msg = "ERRORE: l'utente: " +utente+ " NON è stato cancellato"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun

		
	def controlla_utente(self,s):
		utente = s
		RispFun = []
		select=self.db1.select("*","utente WHERE login='"+utente+"'")
		if len(select) > 0:
			valido=True
			msg   = "Utente registrato"
		else:
			valido=False
			msg   = "Utente non registrato"
		RispFun.append(valido)
		RispFun.append(msg)
		return RispFun

	def nuovo_utente(self,s):
		utente = s
		RispFun = []
		select=self.db1.select("*","utente WHERE login='"+utente+"'")
		if len(select) > 0:
			valido=False
			msg   = "Nome utente già utilizzato, inserisci altro nome"
		else:
			valido=True
			msg   = "Utente non registrato"
		RispFun.append(valido)
		RispFun.append(msg)
		return RispFun
		
	def controlla_password(self,s):
		self.__passwd = s
		RispFun = []
		select=self.db1.select("*","utente WHERE login='"+self.__name+"' AND pass='"+self.__passwd+"'")
		if len(select) > 0:
			valido=True
			msg   = "Connesso..."
		else:
			valido=False
			msg   = "Utente o Password errata!"
		RispFun.append(valido)
		RispFun.append(msg)
		return RispFun
		
	def lista_utenti(self):
		lista = ""
		lista=self.db1.select("login, id","utente")
		return lista

