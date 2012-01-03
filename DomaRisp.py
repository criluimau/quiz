#!/usr/bin/python
#! -*- coding: utf-8 -*-

import random

class DomaRisp:
	
	def __init__(self, db):
		self.db1 = db

	def domanda(self, numero,materia):
		DR   = []
		key  = []
		key1 = []
		records = self.db1.select("*","domande WHERE argomento_id='"+str(materia)+"'")
		lengh = len(records)
		for s in records:
			key.append(s[0])
			key1.append(s[0])
		random.shuffle(key)
		if numero > lengh:
			numero = lengh
			print "Ci sono solo "+str(lengh)+" domande"
		for count in range(0, numero):
			val = key[count]
			i = key1.index(val)
			DR.append(records[i])
		return DR
	
	def risposta(self, id_domanda):
		records = self.db1.select("*","risposte WHERE id_domanda='"+str(id_domanda)+"'")
		return records

	def lista_materie(self):
		lista = ""
		lista=self.db1.select("argomento,id" ,"materia")
		return lista
		
	def inserisci_materia(self,materia):
		RispFun = []
		err=self.db1.insert("materia (argomento) VALUES ('"+materia+"')")
		if not err:
			msg = "Materia "+materia+" inserita correttamente"
		else:
			msg = "ERRORE: Materia "+materia+" NON inserita"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
