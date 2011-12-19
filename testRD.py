#!/usr/bin/python
#! -*- coding: utf-8 -*-

import Db, DomaRisp, datetime
hostname = 'localhost'
db = 'quiz'
db_user = 'root'

# VARIABILI VARIABILI VARIABILI
db_passwd = 'pippo'
user_name = 'luigi'

db1 = Db.Db(hostname,db_user,db_passwd,db)
db1.connection_on()

DR1 = DomaRisp.DomaRisp(hostname,db_user,db_passwd,db)

# preparazione questionario
maxDomande = 3
oggi       = datetime.datetime.today()
oggi       = oggi.date()
oggi       = str(oggi)
record     = db1.select("*", "utente WHERE login='"+user_name+"'")
utenteid   = record[0][0]
convalida  = "0"

materia=5

inserisco = db1.insert("questionario (data,utente_id,nr_max_domande,convalida) VALUES ('"+oggi+"',"+str(utenteid)+","+str(maxDomande)+","+convalida+")")
id_quest  = db1.select("max(id)","questionario WHERE utente_id='"+str(utenteid)+"'")

# estrazione domande da dizionario
D = DR1.domanda(maxDomande,materia)

# estrazione risposte alle domande e scrittura schede
for n in D:
	id_domanda = n[0]
	R = DR1.risposta(id_domanda)
	for nrrisp in R:
		inserisco = db1.insert("scheda (domanda_id,risposta_ok,id_utente,id_questionario,id_risposta) VALUES ("+str(id_domanda)+","+str(nrrisp[2])+","+str(utenteid)+","+str(id_quest[0][0])+","+str(nrrisp[0])+")")
	for s in D:
		print s[1]
		id_domanda = s[0]
		R = DR1.risposta(id_domanda)
		risposte = []
		a=0
		for s1 in R:
			risposte.append(s1[0])
			print "n° ", a, " ", s1[3] 
			a=a+1
		risposta = raw_input('Inserisci il n della risposta esatta: ')
		db1.update("scheda SET risposta_ute='1' WHERE id="+str(s1[int(risposta)]))
		
		
db1.connection_off()
