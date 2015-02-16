#!usr/bin/python

"""
    flag_color.py
    Patrick Niewold / 02/2015
    uses QtGui.QColor as superclass
    includes a method that chooses random color
    this method gives a random value to these methods:
    self.setRed(), self.setGreen() and self.setBlue()
"""

from PyQt4 import QtGui
from random import randrange


class FlagColor(QtGui.QColor):
    def __init__(self):
        super(FlagColor, self).__init__()
        self.randomcolor()

    def randomcolor(self):
        self.setRed(randrange(0, 256))
        self.setGreen(randrange(0, 256))
        self.setBlue(randrange(0, 256))
        
