#!/usr/bin/python
#flag_ui.py
#Roos Vermeulen
#Patrick Niewold

from PyQt4 import QtGui
import country
import sys

class Flag_UI(QtGui.QWidget):
	
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setGeometry(250, 200, 350, 50)
		self.setWindowTitle("Country Flag")
		self.initUI()
		
	def initUI(self):
		#Create Menu
		namelist = self.createnamelist()
		self.menulist = QtGui.QComboBox(self)
		self.menulist.addItems(namelist)
		
		#Starts self.setcountry
		self.setcountry()
		self.menulist.currentIndexChanged.connect(self.setcountry)
		
		#Create Layout
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		grid.addWidget(self.menulist, 0, 0)
		
	def setcountry(self):
		selectedname = self.menulist.currentText()
		selectedcountry = country.Country(selectedname)
		
	def createnamelist(self):
		source = open("countries_list.txt","r")
		namelist = []
		for line in source:
			line = line.strip()
			namelist.append(line)
		return namelist
		
		

def main():
    app = QtGui.QApplication(sys.argv)
    window = Flag_UI()
    window.show()
    sys.exit(app.exec_())	

if __name__ == '__main__':
	main()
