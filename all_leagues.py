# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study materials\database project\all_leagues.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cx_Oracle
from PyQt5 import QtCore, QtGui, QtWidgets
from league_summery import leg_summery
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 90, 256, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 250, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 35, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 200, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 480, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
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
        pop=populate()
        pop.get_items()
        item = self.tableWidget.verticalHeaderItem(0)
        cnt=0;
        while cnt<len(pop.lst):
            self.tableWidget.setVerticalHeaderItem(cnt, item)
            item = self.tableWidget.verticalHeaderItem(cnt)
           
            cnt+=1
           # item.setText(_translate("MainWindow", str(cnt)))
             #item.setText("blah blah")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        cnt=0
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
      
        for texts in pop.lst:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(cnt, 0, item)
            print(cnt)
            print(texts) 
            if cnt is None:
                   cnt=0
            item.setText(_translate("MainWindow",texts[0]))
            item = self.tableWidget.item(cnt, 0)
           
            cnt+=1;
       # item = self.tableWidget.verticalHeaderItem(1)
        #item.setText(_translate("MainWindow", "2"))
       # item = self.tableWidget.verticalHeaderItem(2)
        #item.setText(_translate("MainWindow", "3"))
     #   item = self.tableWidget.verticalHeaderItem(3)
      #  item.setText(_translate("MainWindow", "4"))
      #  item = self.tableWidget.verticalHeaderItem(4)
      #  item.setText(_translate("MainWindow", "5"))
       # item = self.tableWidget.verticalHeaderItem(5)
       # item.setText(_translate("MainWindow", "6"))
       # item = self.tableWidget.verticalHeaderItem(6)
       # item.setText(_translate("MainWindow", "7"))
       # item = self.tableWidget.verticalHeaderItem(7)
       # item.setText(_translate("MainWindow", "8"))
       # item = self.tableWidget.verticalHeaderItem(8)
        """item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))"""
        
    
        
       # item = self.tableWidget.item(2, 0)
       # item.setText(_translate("MainWindow", "get"))
       # item = self.tableWidget.item(3, 0)
       # item.setText(_translate("MainWindow", "it"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "ok"))
        self.label.setText(_translate("MainWindow", "all leagues "))
        self.label_2.setText(_translate("MainWindow", "enter league name and press ok to view details "))
        self.pushButton_2.setText(_translate("MainWindow", "go back !"))
        self.pushButton.clicked.connect(self.on_click_ok)
    
    def on_click_ok(self):
        print('ok clicked')
        name=self.lineEdit.text()
        print(name)
        lg_sum=leg_summery()
        lg_sum.show(name)
        print('PyQt5 button click s2')
        





class populate:
    items=0
    lst=list()
    def get_items(self):
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
            #print(con.version)
        cur=con.cursor()
        cur.execute('select lg_name from league order by lg_name')
        for result in cur:
           # print(result)
            self.lst.append(list(result))
        
       # cur.callproc('extract_all_league_names',list)
        print(self.lst)
        
class all_leg:
    def show():
        import sys
         #app = QtWidgets.QApplication(sys.argv)
        #global app
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

