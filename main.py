# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 01:38:30 2019

@author: HP
"""

import sys
from welome import welcome
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QLabel,QMainWindow
from PyQt5.uic import loadUi
import PyQt5







wel=welcome 

welcome.show()

#pyuic5 -x "E:\study materials\database project\league_summer.ui" -o "E:\study materials\database project\league_summery.py"