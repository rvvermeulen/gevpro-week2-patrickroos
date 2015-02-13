#!/usr/bin/python
#country.py
#Roos Vermeulen
#Patrick Niewold

class Country:
	
	def __init__(self, name):
		self.name = name

	def __str__(self):
		print("Hello from " + self.name)
