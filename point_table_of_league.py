# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study materials\database project\point table of league.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!




#unitr test kora baki
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
global lg_nm
lg_nm="'Spanish la liga'"
import cx_Oracle
global tbl_list
tbl_list=[[]]
global names
class db_ex:
    win=0;
    draw=0;
    gd=0;
    points=0;
    def extract(self):
    
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
            #print(con.version)
            
        cur1=con.cursor()
        cur2=con.cursor()
        command='select team_name from teams,league_team,league where league.ID=league_team.league_id and league_team.tm_id=teams.team_id and league.lg_name=';
        command=command+lg_nm;
        cur1.execute(command)
        print(command);
       # cur.execute('select * from goals')////figure out how to populate this table 
        print("hello wolrd   iktu por")
      #  global names
        for nmm in cur1:
           # pl=0;
            #g_d=0;
            #w=0;
            #l=0;
            #d=0;
            #poin=0;
            print("hello wolrl")
         #   cur2.callproc('calculate_point_table_for',[nmm[0],lg_nm,pl,g_d,w,l,d,poin]) #///////////////////////////check if this works
            cur2.execute("select id from league where lg_name="+lg_nm);
            row = cur2.fetchone()
            lg_ID=row[0];
            command1="select * from points where lg_id="+str(lg_ID)+" ORDER BY point DESC";
            cur2.execute(command1);
            result=cur2.fetchall()
           # tmp_lst=list(result)
            global tbl_list
            #if tbl_list is None:
             #   tbl_list=list(result)
            #else:
             #   tbl_list.append(result)
            
            tbl_list=list(result)
       # for result in cur:
           # print(result)
        #    self.lst.append(list(result))
       
        ##very very important do not delete
        #sapnu pues
        ###important part over

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 671, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(18)
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
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
       # item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 1, item)
        #item = QtWidgets.QTableWidgetItem()
       # self.tableWidget.setItem(1, 0, item)
       # item = QtWidgets.QTableWidgetItem()
       # self.tableWidget.setItem(1, 1, item)
        for i in range (0,17):
            for j in range (0,7):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)
                
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")
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
        self.label.setText(_translate("MainWindow", lg_nm))
        self.label_2.setText(_translate("MainWindow", "point table "))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "win"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Draw"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GD"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Points"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        global tbl_list
        self.tableWidget.setSortingEnabled(False)
        for i in range (0,len(tbl_list)):
            con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
            #print(con.version)
            cur3=con.cursor()
            res=cur3.execute("select team_name from teams where team_id="+str(tbl_list[i][0]))
            res=list(res)
            for j in range (0,len(tbl_list[i])):
                item = QtWidgets.QTableWidgetItem()
                print(res)
                print(" eita dekhbo ekhon")
                if j==0:
                    item.setText(_translate("MainWindow",str(res[0][0])))
                else:
                    item.setText(_translate("MainWindow",str(tbl_list[i][j])))
                self.tableWidget.setItem(i, j, item)
                
             
                print(tbl_list)
               # if tbl_list[i][j] is None:
                #    continue
                
      #  item.setText(_translate("MainWindow", "samlertext"))
       # item = self.tableWidget.item(1, 1)
       # item.setText(_translate("MainWindow", "did you get that?"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "return "))






class leg_tbl:
    def show(self,name):
         print("okay")
         dtbs=db_ex()
         dtbs.extract()
         
         global lg_nm
         lg_nm=name
        # app1 = QtWidgets.QApplication(sys.argv)
         MainWindow = QtWidgets.QMainWindow()
         ui = Ui_MainWindow()
         ui.setupUi(MainWindow)
         MainWindow.show()
         sys.exit(app.exec_())
         
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    leg=leg_tbl()
    leg.show("Spanish la liga")
