#!/usr/bin/python
#! -*- coding: utf-8 -*-
import Db, string, DomaRisp, datetime

import sys
try:
 import pygtk
  #tell pyGTK, if possible, that we want GTKv2
 pygtk.require("2.0")
except:
  #Some distributions come with GTK2, but not pyGTK
  pass

try:
  import gtk
  import gtk.glade
except:
  print "You need to install pyGTK or GTKv2 ",
  print "or set your PYTHONPATH correctly."
  print "try: export PYTHONPATH=",
  print "/usr/local/lib/python2.2/site-packages/"
  sys.exit(1)

#now we have both gtk and gtk.glade imported
#Also, we know we are running GTK v2

hostname = 'localhost'
db = 'quiz'
db_user = 'root'
db_passwd = 'pippo'

db1 = Db.Db(hostname,db_user,db_passwd,db)
db1.connection_on()


DR1 = DomaRisp.DomaRisp(hostname,db_user,db_passwd,db)

# login
entra=True
while entra:
	
	user_new=""
	while user_new != 'S' and user_new != 'N':
		user_new=raw_input("Sei un utente già registrato: S/N: ")
		if user_new == 's':
			user_new = 'S'
		if user_new == 'n':
			user_new = 'N'

	
	if user_new=="S":
	#login utente
		user_name= raw_input("Scrivi il tuo nome utente: ")
		user_passwd= raw_input("Scrivi password: ")

		select= db1.select("*","utente WHERE login='"+user_name+"' AND pass='"+user_passwd+"'")

		if len(select) > 0:
			print "Connesso..."
			entra=False
		else:
			print "Utente o Password errata!"
	else:
	#Registrazione nuovo utente

	
	
	
		user_ok = True
		while user_ok:
			user_name= raw_input("Registra il nome utente: ")
			user_passwd=""
			user_passwd1="a"
			while user_passwd != user_passwd1:
				user_passwd=  raw_input("Registra la password: ")
				user_passwd1= raw_input("Ripeti la password  : ")
			if 	user_name != "" or user_passwd != "":
				select= db1.select("*","utente WHERE login='"+user_name+"'")
				if len(select) == 0:
					# utente valido
					err=db1.insert("utente (login, pass) VALUES('"+user_name+"','"+user_passwd+"')")
					if not err:
						entra   = False
						user_ok = False
						print "Registrazione effettuata con successo, sei ora connesso"
					else:
						print 'Registrazione non riuscita'
				else:
					print "Utente già presente! Inserire altro nome utente"
			else:
				print "i campi sono vuoti! \nRiprova..."
				
 
if user_name == 'Admin':
	user_admin = True
else:
	user_admin = False

# messaggio di benvenuto
if user_admin:
	print "Benvenuto amministratore"
else:
	print "Benvenuto utente "+user_name+" al quiz. \nIn bocca al lupo"

# menù iniziale amministratore
fine = False
scelta = 0
while user_admin and fine == False and scelta == 0:
	
	print "Scegli un'operazione: "
	print "1 - Visualizza la lista degli utenti"
	print "2 - Cancella utente"
	print "3 - Crea un nuovo questionario"
	print "4 - Modifica questionario"
	print "5 - Cancella questionario"
	print "6 - Crea domande"
	print "7 - Cancella domande"

	
	
	scelta= input("Scrivi il numero: ")
	
	while scelta==1:
		print "\n\nLISTA UTENTI:"
		a=db1.select("login, id","utente")
		cont=0
		print a
		for row in a:
			print str(cont) + " " +row[0]+ " " +str(row[1]) 
			cont=cont+1
		back = raw_input('Vuoi tornare al menu principale? s - n')
		if back == "s" or back == "S":
			scelta = 0
	while scelta==2:
		print "\n\nLISTA UTENTI:"
		a=db1.select("login, id","utente")
		for row in a:
			print str(row[1])+" "+row[0] 
		del_user = raw_input('per favore inserisci il nome utente che si desidera cancellare: ')
		a = db1.delete("utente WHERE login='"+del_user+"'")
		b = db1.select("*","utente WHERE login='"+del_user+"'")
		if a == b:
			print("l'utente," +del_user+ "è stato cancellato correttamente")
			back = raw_input('Vuoi tornare al menu principale? s - n')
			if back == "s" or back == "S":
				scelta = 0
		else:
			print("il nome utente che si è immesso è errato o non esistente")
			riprova = raw_input('Vuoi riprovare? s/n')
			if riprova == "s" or riprova == "S":
				scelta == 2
	while scelta==3:
			select= db1.select("argomento,id" ,"materia")
			materie = []
			for a in select:
				materie.append(a[0])
				print a[0]+ " " +str(a[1]) 
			nome_materia= raw_input("Inserisci una Materia: ")
			if nome_materia in materie:
				print "errore, materia già presente"
				c = raw_input('vuoi continuare o uscire s|n: ')
				if c == "n" or c == "N":
					scelta = 0
				else:
					scelta = 3
			else:
				inserisco = db1.insert("materia (argomento) VALUES ('"+nome_materia+"')")
				print "Materia inserita correttamente"
				
				back = raw_input('Vuoi inserire un altra materia? s - n: ')
				if back == "s" or back == "S":
					scelta = 3
				else:
					scelta = 0
	while scelta==4:
			select= db1.select("argomento,id" ,"materia")
			materie = []
			for a in select:
				materie.append(a[0])
				print a[0]+ " " +str(a[1])
			nome_materia=raw_input('per favore inserisci la materia da modificare: ')
			if nome_materia in materie:
				nuovo_nome=raw_input("Inserisci il nuovo nome: ")
				if nuovo_nome not in materie and len(nuovo_nome) != 0:
					db1.update("materia SET argomento='"+nuovo_nome+"' WHERE argomento='"+nome_materia+"';")	
					b = raw_input('Ok, operazione eseguita con successo, Vuoi modificare un altra materia? S|N: ')
					if b == "S" or b == "s":
						scelta = 4
					else:
						scelta = 0
						b = "0"
				else:
					print "Il nome della materia da modifare è inesistente o è già stato modificato in precedenza, per favore controlla nuovamente"
					scelta = 4
			else:
				scelta = 0
	while scelta==5:
			select= db1.select("argomento,id" ,"materia")
			materie = []
			for a in select:
				materie.append(a[0])
				print a[0]+ " " +str(a[1])
			del_materia = raw_input('per favore inserisci il nome utente che si desidera cancellare: ')
			if del_materia in materie:
				db1.delete("materia WHERE argomento='"+del_materia+"'")
				print("la materia," +del_materia+ "è stata cancellata correttamente")
				back = raw_input('Vuoi tornare al menu principale? s - n: ')
				if back == "s" or back == "S":
					scelta = 0
			else:
				print("il nome della materia che si è immesso è errato o non esistente")
				riprova = raw_input('Vuoi riprovare? s/n')
				if riprova == "s" or riprova == "S":
					scelta = 5
				if riprova != "s" or riprova != "S":
					scelta = 0
	while scelta==6:
			select= db1.select("argomento,id" ,"materia")
			materie = []
			for a in select:
				materie.append(a[1])
				print a[1]," " ,a[0]	
			id_argomento= input("Inserisci id della materia dove vuoi aggiungere la domanda")
			if id_argomento in materie:
				print "ok, hai selezionato la materia", id_argomento
				testo_domanda = raw_input("Inserisci adesso il testo della domanda")
				difficolta= input('per favore inserisci la difficolta della domanda in una scala da 1 a 10')
				if len(testo_domanda) > 10 and difficolta in range(1,10):
					db1.insert("domande (testo, argomento_id ,difficolta) VALUES('"+testo_domanda+"','"+str(id_argomento)+"','"+str(difficolta)+"')")
					intero= True
					while intero:
						n = raw_input('inserisci il numero delle risposte da assegnare alla domanda')
						try:
							n = int(n)
						except:
							n = 3
						if type(n) is int:
							intero=False
										
					id_domanda = db1.select("id", "domande WHERE testo='"+testo_domanda+"'")
					reg_domanda = id_domanda[0][0]
					for p in range(0,n):
						controllo = 0
						while controllo == 0:
							risposta_domanda= raw_input('inserisci la risposta alla domanda')
							valore= input('La risposta inserita è vera o falsa? 1|0')
							if valore == 1 or valore == 0:							
								db1.insert("risposte (id_domanda, testo, valore) VALUES ('"+str(reg_domanda)+"','"+risposta_domanda+"','"+str(valore)+"')")
								controllo = 1
								print "Risposta inserita correttamente"
					print "hai inserito tutte le risposte e la domanda è stata registrata correttamente"
				c = raw_input('"s" per inserire una nuova domanda? o "n" uscire s|n')
				if c == "s" or c == "S":
					scelta = 6
				else:
					scelta = 0
	while scelta==7:
			select= db1.select("id,argomento" ,"materia")
			materie = []
			for a in select:
				materie.append(a[0])
				print str(a[0])+ " " +str(a[1])
			materia = input("A quale id argomento corrisponde la domanda\e che vuoi cancellare? ")
			if materia in materie:
					select= db1.select("id,testo" ,"domande WHERE argomento_id="+str(materia))			
					domande = []
					for a in select:
						domande.append(a[0])
						print str(a[0])+ " " +str(a[1])
					del_domanda = input('per favore inserisci l\'id della domanda da cancellare ')
					if del_domanda in domande:
						db1.delete("domande WHERE id='"+str(del_domanda)+"'")
						print("la domanda, con id " +str(del_domanda)+ " è stata cancellata correttamente")
						back = raw_input('Vuoi tornare al menu principale? s - n: ')
						if back == "s" or back == "S":
							scelta = 0
						if back != "s" or back != "S":
							scelta = 7
					else:
						print("il nome della materia che si è immesso è errato o non esistente")
						riprova = raw_input('Vuoi riprovare? s/n')
						if riprova == "s" or riprova == "S":
							scelta = 7
						if riprova != "s" or riprova != "S":
							scelta = 0
					
if user_name != "Admin":
	
	print "Benvenuto al programma Quiz+, avrai ora la possibilità di verificare le tue competenze e scoprire se hai studiato!!"
	select= db1.select("argomento,id" ,"materia")
	materie = []
	for a in select:
			materie.append(a[1])
			print a[1]," " ,a[0]	
	materia= input("Inserisci id della materia del questionario")
	if materia in materie:
		print "ok, hai selezionato la materia", materia, "il quiz sta per cominciare"
				# preparazione questionario
		maxDomande = 10
		oggi       = datetime.datetime.today()
		oggi       = oggi.date()
		oggi       = str(oggi)
		record     = db1.select("*", "utente WHERE login='"+user_name+"'")
		utenteid   = record[0][0]
		convalida  = "0"

		inserisco = db1.insert("questionario (data,utente_id,nr_max_domande,convalida) VALUES ('"+oggi+"',"+str(utenteid)+","+str(maxDomande)+","+convalida+")")
		id_quest  = db1.select("max(id)","questionario WHERE utente_id='"+str(utenteid)+"'")

			# estrazione domande da dizionario
		D = DR1.domanda(maxDomande,materia)		

			# estrazione risposte alle domande e scrittura schede
		for n in D:
			id_domanda = n[0]
			R = DR1.risposta(id_domanda)
			for nrrisp in R:
				inserisco = db1.insert("scheda (domanda_id,risposta_ok,id_utente,id_questionario,id_risposta,risposta_ute) VALUES ("+str(id_domanda)+","+str(nrrisp[2])+","+str(utenteid)+","+str(id_quest[0][0])+","+str(nrrisp[0])+","+str(0)+")")
			
		#richiesta delle risposte all'utente
		for s in D:
			print s[1]
			id_domanda = s[0]
			R = DR1.risposta(id_domanda)
			
			risposte = []
			key_risp = []
			a=0
			for s1 in R:
				risposte.append(s1[0])
				print "n° ", a, " ", s1[3] 
				a=a+1
				RQ  = db1.select("*","scheda WHERE id_questionario="+str(id_quest[0][0])+" and domanda_id = "+str(id_domanda)+" and id_risposta= "+str(s1[0])+"")
				key_risp.append(RQ[0])
			
			risposta = -1
			while risposta not in range (0,a):
				risposta = raw_input('Inserisci il n della risposta esatta: ')
				try:
					risposta = int(risposta)
				except:
					risposta = -1

			db1.update("scheda SET risposta_ute=1 WHERE id_risposta='"+str(risposte[risposta])+"' AND id="+str(key_risp[risposta][0]))
						
			 #	err=db1.insert("utente (login, pass) VALUES('"+user_name+"','"+user_passwd+"')")
			

# giudizione finale
	id_questionario=id_quest[0][0]	
	record     = db1.select("domanda_id, id_risposta, risposta_ute, risposta_ok", "scheda WHERE id_questionario='"+str(id_questionario)+"' group by domanda_id, id_risposta, risposta_ute, risposta_ok")
	
	domande  = 0
	risp_err = 0
	risp_ok  = 0
	start    = -1
	err   = 0
	ok    = 0

	for s in record:
		if start != s[0]:
			start = s[0]
			domande = domande + 1
			if err > 0:
				risp_err = risp_err+1
			if ok  > 0 and err == 0:
				risp_ok  = risp_ok+1
			err = 0
			ok  = 0
		if s[2] != s[3]:
			err = err+1
		else:
			ok  = ok+1
	if err > 0:
		risp_err = risp_err+1
	if ok  > 0 and err == 0:
		risp_ok  = risp_ok+1

	if domande > 0:
		perc = 1.0 * risp_ok/domande * 100.0

		giudizio = "Sei grande!"
		if perc < 90:
			giudizio = "ottimo"
		if perc < 80:
			giudizio = "distinto"
		if perc < 70:
			giudizio = "sufficiente"
		if perc < 60:
			giudizio = "insufficiente"
		if perc < 50:
			giudizio = "scarso"
		if perc < 30:
			giudizio = "Studia!"
											
		print "domande fatte  ", domande
		print "risposta ok    ", risp_ok
		print "risposte errate", risp_err
		print "Giudizio finale", giudizio

		
# verifica bis



#	record= db1.select("risposte.valore", "scheda, risposte WHERE scheda.id_questionario='"+str(id_questionario)+"' AND scheda.id_utente='"+str(utenteid)+"' AND scheda.risposta_ok=risposte.valore AND ")
#	a=0
#	for i in record:
#		if i[0] == 1:
#			a=a+i[0]
#	if a > 0:
#		print "hai risposto bene!"
#	else:
#		print "bocciato" 

	
#inserisco="utente(login,pass) VALUES ('minni','123456');"
#db1.insert(inserisco)
#s="utente WHERE id=3"
#db1.delete(s)

#db1.update("utente SET login='nnn' WHERE id=4;")



#print select




db1.connection_off()




