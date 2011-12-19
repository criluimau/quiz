
class User:
	
	def __init__(self, db, username, password):
		
		self.db = db
		self.useranme = username
		self.password = password
		
	def salva(self):
		select = self.db.select("*","utente WHERE login='"+self.username+"'")
		if len(select) == 0:
			err = self.db.insert("utente (login, pass) VALUES('"+self.username+"','"+self.password+"')")
			return 1
		return 0
		
	def trova(self, s):
		
