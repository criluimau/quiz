#!/usr/bin/python
#! -*- coding: utf-8 -*-

import Db, random


class DomaRisp:
	
	def __init__(self,hostname,db_user,db_passwd,dbname):
		self.hostname = hostname
		self.dbname = dbname
		self.dbpasswd = db_passwd
		self.dbuser = db_user

	def domanda(self, numero,materia):
		db1 = Db.Db(self.hostname,self.dbuser,self.dbpasswd,self.dbname)
		db1.connection_on()
		DR   = []
		key  = []
		key1 = []
		records = db1.select("*","domande WHERE argomento_id='"+str(materia)+"'")
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
		
		db1.connection_off()
		return DR
	
	def risposta(self, id_domanda):
		db1 = Db.Db(self.hostname,self.dbuser,self.dbpasswd,self.dbname)
		db1.connection_on()
		records = db1.select("*","risposte WHERE id_domanda='"+str(id_domanda)+"'")
		db1.connection_off()
		return records
