#!/usr/bin/python
#flag_ui.py
#Roos Vermeulen
#Patrick Niewold

from PyQt4 import QtGui
import country
import flag_color
import sys

class Flag_UI(QtGui.QWidget):
	
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle("Country Flag")
		self.initUI()
		
	def initUI(self):
		
		self.col = QtGui.QColor(0, 0, 0)
		
		#Create Layout
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		
		#Create Combobox
		self.combobox = QtGui.QComboBox(self)
		self.combobox.addItems(country.Country.createCountries(self))
		self.combobox.setCurrentIndex(0)
		self.combobox.currentIndexChanged.connect(self.updateCountry)
		
		grid.addWidget(self.combobox, 1, 0)
		
		self.flag = QtGui.QFrame(self)
		self.flag.setFixedSize(250, 100)
		self.flag.setStyleSheet("QFrame { background-color: %s}" % self.col.name())
		
		grid.addWidget(self.flag, 3, 0)
	
	def updateCountry(self):
		self.col = flag_color.FlagColor.randomcolor(self.col)
		self.flag.setStyleSheet("QFrame { background-color: %s}" % self.col.name())
		
		
def main():
    app = QtGui.QApplication(sys.argv)
    window = Flag_UI()
    window.show()
    sys.exit(app.exec_())	

if __name__ == '__main__':
	main()
