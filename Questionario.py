#!/usr/bin/python
#! -*- coding: utf-8 -*-

import random

class Questionario:
	
	def __init__(self, db):
		self.db1 = db

	def inserisci_quest(self,oggi,id_utente,maxDomande):
		convalida = "0"
		RispFun = []
		err=self.db1.insert("questionario (data,utente_id,nr_max_domande,convalida) VALUES ('"+oggi+"',"+str(id_utente)+","+str(maxDomande)+","+convalida+")")
		if not err:
			msg = "Questionario inserito correttamente"
		else:
			msg = "ERRORE: questionario NON inserito"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
