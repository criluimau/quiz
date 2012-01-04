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
		
	def recuperaid_quest(self,id_utente):
		lista=self.db1.select("max(id)","questionario WHERE utente_id='"+str(id_utente)+"'")
		id_quest   = lista[0][0]
		return id_quest

	def riempi_quest(self,id_domanda, nrrisp, id_utente, id_quest, id_risposta, rispostaok):
		RispFun = []
		err=self.db1.insert("scheda (domanda_id,risposta,id_utente,id_questionario,id_risposta,risposta_ok,risposta_ute) VALUES ("+str(id_domanda)+",'"+str(nrrisp)+"',"+str(id_utente)+","+str(id_quest)+","+str(id_risposta)+","+str(rispostaok)+","+str(0)+")")
		if not err:
			msg = "Questionario riempito correttamente"
		else:
			msg = "ERRORE: questionario NON riempito"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
		
	def recuperaid_scheda(self, id_quest, id_domanda, id_risp):
		lista=self.db1.select("*","scheda WHERE id_questionario="+str(id_quest)+" and domanda_id = "+str(id_domanda)+" and id_risposta= "+str(id_risp)+"")
		id_scheda   = lista[0][0]
		return id_scheda
		
	def aggiorna_scheda(self, risposta, id_scheda):
		RispFun = []
		err=self.db1.update("scheda SET risposta_ute=1 WHERE id_risposta='"+str(risposta)+"' AND id="+str(id_scheda)+"")
		if not err:
			msg = "Scheda inserita correttamente"
		else:
			msg = "ERRORE: scheda NON inserita"
		RispFun.append(err)
		RispFun.append(msg)			
		return RispFun
		
	def dati_quest(self,id_quest):
		lista=self.db1.select("domanda_id, id_risposta, risposta_ute, risposta_ok", "scheda WHERE id_questionario='"+str(id_quest)+"' group by domanda_id, id_risposta, risposta_ute, risposta_ok")
		return lista


