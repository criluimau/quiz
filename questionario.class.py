
class Domanda:
	
	def __init__(self, domanda):
		
		self.domanda = domanda
		self.risposte = []
		
	def aggiungi_risposta(self, risposta, punti)
	
		r = Risposta(risposta, punti)
		self.risposte.append(r)
		
class Risposta:
	
	def __init__(self, risposta, punti):
		
		self.risposta = risposta
		self.punti = punti 
		
	def salva(self):
		... query ...
		
		self.id = ID RECORD
		return id
