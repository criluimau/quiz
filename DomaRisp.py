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
	
	def modifica_materia(self,materia, nuovo_nome):
		RispFun = []
		err=self.db1.update("materia SET argomento='"+nuovo_nome+"' WHERE argomento='"+materia+"';")
		if not err:
			msg = "Materia "+materia+" cambiata in "+nuovo_nome+" correttamente"
		else:
			msg = "ERRORE: Materia "+materia+" NON cambiata in "+nuovo_nome
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
	
	def cancella_materia(self,materia):
		RispFun = []
		err=self.db1.delete("materia WHERE argomento='"+materia+"'")
		if not err:
			msg = "Materia "+materia+" cancellata correttamente"
		else:
			msg = "ERRORE: Materia "+materia+" NON cancellata"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun

	def inserisci_domanda(self,testo_domanda,id_argomento,difficolta):
		RispFun = []
		err=self.db1.insert("domande (testo, argomento_id ,difficolta) VALUES('"+testo_domanda+"','"+str(id_argomento)+"','"+str(difficolta)+"')")
		if not err:
			msg = "Domanda "+testo_domanda+" inserita correttamente"
		else:
			msg = "ERRORE: inserimento domanda "+testo_domanda
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
		
	def recuperaid_domanda(self,testo_domanda,id_argomento):
		lista=self.db1.select("id", "domande WHERE testo='"+testo_domanda+"' AND id='"+str(id_argomento)+"'")
		return lista
		
	def inserisci_risposta(self,id_domanda,risposta_domanda,valore):
		RispFun = []
		err=self.db1.insert("risposte (id_domanda, testo, valore) VALUES ('"+str(id_domanda)+"','"+risposta_domanda+"','"+str(valore)+"')")
		if not err:
			msg = "Risposta "+risposta_domanda+" inserita correttamente"
		else:
			msg = "ERRORE: inserimento risposta domanda "+risposta_domanda
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
