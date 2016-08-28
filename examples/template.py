#!/usr/local/bin/python3

__author__ = 'Dunham, Martinear, Richardson, Traglia'
__status__ = 'Experimental'

import sys
from PyQt5.QtWidgets import *

class PoissonBarrel(QWidget):

	def __init__(self):

		super().__init__()
		self.initUI()

	def initUI(self):

		self.setWindowTitle('PossionBarrel - The Statistical Analyzer')
		self.showMaximized()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	pb = PoissonBarrel()
	sys.exit(app.exec_()) 
