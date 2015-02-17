#!/usr/bin/python
#country.py
#Roos Vermeulen
#Patrick Niewold

import flag_color

class Country:
	
	def __init__(self, name):
		self.name = name
		self.flag = flag_color.FlagColor()

	def __str__(self):
		return "Hello from " + str(self.name)

def createCountries():
	source = open("countries_list.txt","r")
	countrieslist = []
	for line in source:
		line.strip()
		country = Country(line)
		countrieslist.append(country)
	return countrieslist
