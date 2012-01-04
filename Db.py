#!/usr/bin/python
#! -*- coding: utf-8 -*-

class Db:
	
		import MySQLdb
		
		def __init__(self,hostname,user,passwd,dbname):
				
			self.__hostname = hostname
			self.__dbname = dbname
			self.__passwd = passwd
			self.__user = user
			
		
		def connection_on(self):
			
			self.conn = Db.MySQLdb.connect(self.__hostname,self.__user,self.__passwd,self.__dbname)
			self.cursor = self.conn.cursor()

		def connection_off(self):
			
			self.conn.close()
			
		def select(self,campo,s):
			sql = "SELECT "+campo+" FROM "+s
			#print sql
			results=""
			try:

				self.cursor.execute(sql)
				results = self.cursor.fetchall()
					
				self.conn.commit()

			except:
				
				self.conn.rollback()
				
			return results
		
		#for row in results:
		#	campo1= row[0]
		#	campo2= row[1]
		
		
		def insert(self,i):
			sql = "INSERT INTO "+i
			#print sql
			try:
				self.cursor.execute(sql)
				self.conn.commit()
				self.err = False
				
			except:
				self.conn.rollback()
				self.err = True
				print "ERRORE DI INSERIMENTO!"
			return self.err
			
		
		def delete(self,d):
			
			sql ="DELETE FROM "+d
			#print sql
			try:
				self.cursor.execute(sql)
				self.conn.commit()
				self.err = False
			except:
				self.conn.rollback()
				print "ERRORE CANCELLAZIONE!"
				self.err = True
			return self.err
				
		def update(self,u):
			
			sql = "UPDATE "+u
			#print sql

			try:
				self.cursor.execute(sql)
				self.conn.commit()
				self.err = False
			except:
				self.conn.rollback()
				print "ERRORE DI MODIFICA!"
				self.err = True
			return self.err
		

