# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study materials\database project\league_summer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from point_table_of_league import leg_tbl
global lg_nm
lg_nm="empty"
global app
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click_pointTable);
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 220, 181, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 310, 181, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",lg_nm))
        self.pushButton.setText(_translate("MainWindow", "pointTable"))
        self.pushButton_2.setText(_translate("MainWindow", "Top-scoreres and assists"))
        self.pushButton_3.setText(_translate("MainWindow", "fixture and next matches"))
    def on_click_pointTable(self):
        print('ok clicked')
        #name=self.lineEdit.text()
        #print(name)
        ptbl=leg_tbl()
        
       # app.quit()
        ptbl.show(lg_nm)
        print('PyQt5 button click s2')
    def on_click_scor(self):
        print('ok clicked')
       # name=self.lineEdit.text()
       # print(name)
       # lg_sum=leg_summery()
      #  lg_sum.show(name)
        print('PyQt5 button click s2')
    def on_click_ok_fixture(self):
        print('ok clicked')
        #name=self.lineEdit.text()
        #print(name)
        #lg_sum=leg_summery()
        #lg_sum.show(name)
        print('PyQt5 button click s2')

if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



class leg_summery:
    def show(self,name):
         import sys
         global lg_nm
         lg_nm=name
         #global app
         #app = QtWidgets.QApplication(sys.argv)
         MainWindow = QtWidgets.QMainWindow()
         ui = Ui_MainWindow()
         ui.setupUi(MainWindow)
         MainWindow.show()
         sys.exit(app.exec_())
