#!/usr/bin/python
#! -*- coding: utf-8 -*-

import sys, string, datetime, time
import Db, utente, DomaRisp

#try:
# import pygtk
#  #tell pyGTK, if possible, that we want GTKv2
# pygtk.require("2.0")
#except:
#  #Some distributions come with GTK2, but not pyGTK
#  pass

#try:
#  import gtk
#  import gtk.glade
#except:
#  print "You need to install pyGTK or GTKv2 ",
#  print "or set your PYTHONPATH correctly."
#  print "try: export PYTHONPATH=",
#  print "/usr/local/lib/python2.2/site-packages/"
#  sys.exit(1)

#now we have both gtk and gtk.glade imported
#Also, we know we are running GTK v2

# *************************************
# funzioni
# *************************************

def listarisposteid(iddomanda):
	print "\n\nLISTA RISPOSTE PRESENTI NELLA DOMANDA CON ID: "+str(iddomanda)
	lista=DR1.lista_risposte_xid(iddomanda)
	risposteid = []
	if len(lista) == 0:
		print "nessuna risposta presente"
	else:
		for a in lista:
			risposteid.append(a[0])
			print a[1]+ " id: " +str(a[0])
	return risposteid

def listadomandeid(idmateria, materia):
	print "\n\nLISTA DOMANDE PRESENTI PER MATERIA: "+materia
	lista=DR1.lista_domande_xid(idmateria)
	domandeid = []
	if len(lista) == 0:
		print "nessuna domanda presente"
	else:
		for a in lista:
			domandeid.append(a[0])
			print a[1]+ " id: " +str(a[0])
	return domandeid

def listamaterie():
	print "\n\nLISTA MATERIE PRESENTI:"
	lista=DR1.lista_materie()
	materie = []
	if len(lista) == 0:
		print "nessuna materia presente"
	else:
		for a in lista:
			materie.append(a[0])
			print a[0]+ " id: " +str(a[1])
	return materie

def caricamaterid():
	lista=DR1.lista_materie()
	materid = []
	if len(lista) > 0:
		for a in lista:
			materid.append(a[1])
	return materid

def listautenti():
	print "\n\nLISTA UTENTI:"
	lista=user.lista_utenti()
	if len(lista) == 0:
		print "nessun utente presente"
	else:
		cont=1
		for row in lista:
			print str(cont) + " " +row[0]+ "      id:" +str(row[1]) 
			cont=cont+1
	return lista

def sceltamenu(opzioni):
	err = False
	while not err:
		try:
			scelta= input("Opzione: ")
		except:
			errormessag("hai digitato una opzione non valida!.")		
			continue
		if not scelta in opzioni:
			errormessag("hai digitato una opzione non valida!.")
		err = True
	return scelta
		
def rispsino(s):
		risp=""
		while risp != 'S' and risp != 'N':
			risp=raw_input(s+" S/N: ")
			risp= risp.upper()
		return risp
def errormessag(errmsg):
		print errmsg
		print "////////////////////////////////////"
		time.sleep(3)
def continua():
		x = raw_input('premi un tasto qualunque per continuare')

# *************************************
# Programma principale
# *************************************

# Connessione a database MYsql
hostname = 'localhost'
db = 'quiz'
db_user = 'root'
db_passwd = 'red'
db1 = Db.Db(hostname,db_user,db_passwd,db)
db1.connection_on()

# Inizializzazione oggetto Domande/risposte
DR1 = DomaRisp.DomaRisp(db1)

# login
autenticato = False
while autenticato == False:
	
	#richiesta iniziale
	user_new=rispsino("Sei un utente già registrato") 
	
	if user_new=="S":
	#login utente già registrato
		user_name   = raw_input("Scrivi il tuo nome utente: ")
		user_passwd = raw_input("Scrivi password: ")
		user	 	= utente.utente(db1, user_name)
		RispFun    	= user.controlla_password(user_passwd)
		autenticato = RispFun[0]
		msg         = RispFun[1]
		print msg
	else:
		#Registrazione nuovo utente
		while autenticato == False:
			# richiesta utente
			user_name= raw_input("Registra il nome utente: ")
			user	 = utente.utente(db1, user_name)
			RispFun	 = user.nuovo_utente(user_name)
			risp	 = RispFun[0]
			msg      = RispFun[1]
			if risp == False:
				print msg
				continue		# ritorno al while
						
			# richiesta password
			user_passwd  =""
			user_passwd1 =""
			while user_passwd != user_passwd1 or len(user_passwd) == 0:
				user_passwd = raw_input("Registra la password: ")
				user_passwd1= raw_input("Ripeti la password  : ")
				if user_passwd != user_passwd1:
					print 'Le due password sono diverse'
				if len(user_passwd) == 0:
					print 'Inserire una password valida'
			
			# registrazione utente
			RispFun     = user.inserisci_utente(user_passwd)
			err         = RispFun[0]
			msg         = RispFun[1]
			print msg
			autenticato = not(err)

 # Scelta amministratore
if user_name.lower() == 'admin':
	user_admin = True
else:
	user_admin = False

# messaggio di benvenuto
if user_admin:
	print "Benvenuto amministratore"
else:
	print "Benvenuto utente "+user_name+" al quiz. \nIn bocca al lupo"

# ===============================
# menù iniziale amministratore
# ===============================

while user_admin:
	menuutente = False
	print "\n=========================================="
	print "         MENU' PRINCIPALE"
 	print "\nScegli un'operazione: "
	print "1 - Gestione utenti"
	print "2 - Gestione materie"
	print "3 - Gestione domande"
	print "4 - Gestione questionari"
	print ""
	print "9 - Fine"
	print "=========================================="	
	opzioni = (1,2,3,4,9)
	scelta = sceltamenu(opzioni)
	if scelta == 9:
		db1.connection_off()
		sys.exit(0)

	while scelta == 1:	
		print "\n=========================================="
		print "         MENU' GESTIONE UTENTE"
		print "\nScegli un'operazione: "
		print "1 - Visualizza la lista degli utenti"
		print "2 - Cancella utente"
		print ""
		print "8 - Ritorna al menù principale"
		print "9 - Fine"
		print "=========================================="
		opzioni = (1,2,8,9)
		scelta1 = sceltamenu(opzioni)
		
		if scelta1==1:
			listautenti()
			continua()
			
		while scelta1==2:
			lista = listautenti()
			risp = False
			while risp == False:
				del_user = raw_input('per favore inserisci il nome utente che si desidera cancellare: ')
				for a1 in lista:
					if del_user == a1[0]:
						risp = True
						break					
				if risp == False:
					print("il nome utente che si è immesso è errato o non esistente")
			RispFun  = user.cancella_utente(del_user)
			err      = RispFun[0]
			msg      = RispFun[1]
			print msg

			risp = rispsino("Vuoi continuare?")
			if risp == 'N':
				break
			
		if scelta1 == 8:
			break
		if scelta1 == 9:
			db1.connection_off()
			sys.exit(0)

	while scelta == 2:	
		print "\n=========================================="
		print "         MENU' GESTIONE MATERIE"
		print "\nScegli un'operazione: "
		print "1 - Crea un nuova materia"
		print "2 - Modifica materia"
		print "3 - Cancella materia"
		print ""
		print "8 - Ritorna al menù principale"
		print "9 - Fine"
		print "=========================================="
		opzioni = (1,2,3,8,9)
		scelta2 = sceltamenu(opzioni)

		while scelta2==1:
			materie=listamaterie()
			nome_materia= raw_input("Inserisci una Materia: ")
			if nome_materia in materie:
				print "errore, materia già presente"
			else:
				RispFun     = DR1.inserisci_materia(nome_materia)
				err         = RispFun[0]
				msg         = RispFun[1]
				print msg

			risp = user_new=rispsino("Vuoi continuare?") 
			if risp == "N":
				break
								
		while scelta2==2:
			materie=listamaterie()
			nome_materia=raw_input('Inserisci la materia da modificare: ')
			if nome_materia in materie:
				nuovo_nome=raw_input("Inserisci il nuovo nome: ")
				if nuovo_nome not in materie and len(nuovo_nome) != 0:
					RispFun     = DR1.modifica_materia(nome_materia, nuovo_nome)
					err         = RispFun[0]
					msg         = RispFun[1]
					print msg
				else:
					print "Il nome della nuova materia esiste già o non è stata immessa"				
			else:
				print "Il nome della materia da modificare è inesistente o è già stato modificato in precedenza, per favore controlla nuovamente"
				
			risp = user_new=rispsino("Vuoi continuare?") 
			if risp == "N":
				break
						
		while scelta2==3:
			materie=listamaterie()
			del_materia = raw_input('Inserisci il nome della materia che si desidera cancellare: ')
			if del_materia in materie:
				RispFun     = DR1.cancella_materia(del_materia)
				err         = RispFun[0]
				msg         = RispFun[1]
				print msg
			else:
				print("il nome della materia che si è immesso è errato o non esistente")

			risp = user_new=rispsino("Vuoi continuare?") 
			if risp == "N":
				break
		 
		if scelta2 == 8:
			break
		if scelta2 == 9:
			db1.connection_off()
			sys.exit(0)
		
	while scelta == 3:	
		print "\n=========================================="
		print "         MENU' GESTIONE DOMANDE"
		print "\nScegli un'operazione: "
		print "1 - Crea domande"
		print "2 - Cancella domande e risposte"
		print ""
		print "8 - Ritorna al menù principale"
		print "9 - Fine"
		print "=========================================="
		opzioni = (1,2,8,9)
		scelta3 = sceltamenu(opzioni)
		
		while scelta3==1:
			materie=listamaterie()
			materid=caricamaterid()
			print "Inserisci 0 per uscire"
			risp = False
			while risp == False:
				try:
					id_argomento= input("Inserisci id della materia dove vuoi aggiungere la domanda ")			
				except:
					print "Inserisci un id della materia valido"
					continue
				if id_argomento == 0:
					break
				if id_argomento in materid:
					risp = True
				else:
					print("L'id materia immesso è errato o non esistente")
			if id_argomento == 0:
				break
			id =  materid.index(id_argomento)
			print "ok, hai selezionato la materia", materie[id], "id:", id_argomento
			testo_domanda = ""
			difficolta = 0
			while len(testo_domanda) < 10 or difficolta not in range(1,10):
				testo_domanda = raw_input("Inserisci adesso il testo della domanda ")
				try:
					difficolta= input('per favore inserisci la difficolta della domanda in una scala da 1 a 10 ')
				except:
					continue
			count = 0
			risp = 'S'
			verofalso = False
			while risp == 'S' or not verofalso or count < 2:
				print "inserisci almeno 2 risposte di cui una vera"
				risposta_domanda=""
				valore=2
				while len(risposta_domanda) < 5:
					risposta_domanda= raw_input('inserisci la risposta alla domanda: '+testo_domanda+' ')
				while valore !=0 and valore !=1:
					try:
						valore= input('La risposta inserita è vera o falsa? 1|0 ')
					except:
						continue
				if valore == 1:
					verofalso = True
				count = count+1
				# inserisce domanda
				if count == 1:
					RispFun = DR1.inserisci_domanda(testo_domanda,id_argomento,difficolta)
					err     = RispFun[0]
					msg     = RispFun[1]
				if count == 1 and err==True:
					print msg
					continua()
					break
				# recupera id domanda
				lista = DR1.recuperaid_domanda(testo_domanda,id_argomento)
				id_domanda = lista[0][0]
				# inserisci risposta
				RispFun = DR1.inserisci_risposta(id_domanda,risposta_domanda,valore)
				err     = RispFun[0]
				msg     = RispFun[1]					
				if err==True:
					print msg
					continua()
				if verofalso and count >= 2:
					risp = rispsino("Vuoi continuare ad inserire risposte?")
			risp = rispsino("Vuoi continuare ad inserire domande?")
			if risp == "N":
				break
					
		while scelta3==2:
			materieid=caricamaterid()
			materie=listamaterie()
			print "Inserisci 0 per uscire"
			# richiesta id materia
			risp = False
			while risp == False:
				try:
					idmateria = input("A quale id argomento corrisponde la domanda\e che vuoi cancellare? ")
				except:
					print "inserisce un ID argomento valido"
					continue
				if idmateria == 0:
					break
				if idmateria in materieid:
					risp=True
				else:
					print "L'ID argomento inserito non esiste"
			if idmateria == 0:
					break
			# richiesta id domanda
			materia = materie[materieid.index(idmateria)]
			domandeid=listadomandeid(idmateria, materia)
			print "Inserisci 0 per uscire"
			if len(domandeid) == 0:
				print "Non ci sono domande per l'argomento scelto"
				continue	# non ci sono domande, riprendo da capo
			risp = False
			while risp == False:
				try:
					iddomanda = input("A quale id domanda corrisponde la domanda che vuoi cancellare? ")
				except:
					print "inserisce un ID domanda valido"
					continue
				if iddomanda == 0:
					break					
				if iddomanda in domandeid:
					risp=True
				else:
					print "L'ID domanda inserito non esiste"
			if iddomanda == 0:
				break					

			# richiesta id risposta
			uscita = 'N'
			while uscita == 'N':
				rispostaid=listarisposteid(iddomanda)
				print "Inserisci 0 per uscire"
				# cancella domanda in assenza di risposte
				if len(rispostaid) == 0:
					print "cancello domanda in assenza di risposte"
					RispFun = DR1.cancella_domanda(iddomanda)
					err     = RispFun[0]
					msg     = RispFun[1]					
					print msg
					break				
				risp = False
				while risp == False:
					try:
						idrisposta = input("A quale id risposta corrisponde la risposta che vuoi cancellare? ")
					except:
						print "inserisce un ID risposta valido"
						continue
					if idrisposta == 0:
						break
					if idrisposta in rispostaid:
						risp=True
					else:
						print "L'ID risposta inserito non esiste"
				if idrisposta == 0:
						break
				# cancella risposta
				RispFun = DR1.cancella_risposta(idrisposta)
				err     = RispFun[0]
				msg     = RispFun[1]				
				if err==True:
					print msg
					continua()
				uscita=rispsino("Vuoi continuare a cancellare risposte?")

			risp = rispsino("Vuoi continuare a cancellare altre domande/risposte?")
			if risp == "N":
				break

		if scelta3 == 8:
			break
		if scelta3 == 9:
			db1.connection_off()
			sys.exit(0)

	while scelta == 4:	
		print "\n=========================================="
		print "         MENU' GESTIONE QUESTIONARI"
		print "\nScegli un'operazione: "
		print "1 - vai a menù utente"
		print ""
		print "8 - Ritorna al menù principale"
		print "9 - Fine"
		print "=========================================="
		opzioni = (1,8,9)
		scelta4 = sceltamenu(opzioni)
		
		if scelta4 == 1:
			menuutente = True
			break
		if scelta4 == 8:
			break
		if scelta4 == 9:
			db1.connection_off()
			sys.exit(0)
	if menuutente == True:
		break		# passo a menù utente
		


# ===============================
# menù iniziale utente
# ===============================

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

		
db1.connection_off()
sys.exit(0)



