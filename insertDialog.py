# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        
  
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tm_name = QtWidgets.QLineEdit(self.centralwidget)
        self.tm_name.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.tm_name.setObjectName("tm_name")
        
        
        
        self.lg_nm = QtWidgets.QLineEdit(self.centralwidget)
        self.lg_nm.setGeometry(QtCore.QRect(110, 50, 81, 31))
        self.lg_nm.setObjectName("lg_nm")
        self.sqd_id = QtWidgets.QLineEdit(self.centralwidget)
        self.sqd_id.setGeometry(QtCore.QRect(210, 50, 71, 31))
        self.sqd_id.setObjectName("sqd_id")
        self.home = QtWidgets.QLineEdit(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(300, 50, 81, 31))
        self.home.setObjectName("home")
        self.is_national = QtWidgets.QLineEdit(self.centralwidget)
        self.is_national.setGeometry(QtCore.QRect(400, 50, 81, 31))
        self.is_national.setObjectName("is_national")
        
        self.insertTeam = QtWidgets.QPushButton(self.centralwidget)
        self.insertTeam.setGeometry(QtCore.QRect(530, 50, 181, 31))
        self.insertTeam.setObjectName("insertTeam")
        self.insertTeam.clicked.connect(self.on_click_team);######################################
      
         
         
        self.insertLeague = QtWidgets.QPushButton(self.centralwidget)
        self.insertLeague.setGeometry(QtCore.QRect(530, 180, 181, 31))
        self.insertLeague.setObjectName("insertLeague")
        self.insertLeague.clicked.connect(self.on_click_league);#######################
        
     
        self.season = QtWidgets.QLineEdit(self.centralwidget)
        self.season.setGeometry(QtCore.QRect(110, 180, 91, 31))
        self.season.setObjectName("season")
        self.endDate = QtWidgets.QLineEdit(self.centralwidget)
        self.endDate.setGeometry(QtCore.QRect(360, 180, 121, 31))
        self.endDate.setObjectName("endDate")
        self.lg_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lg_name.setGeometry(QtCore.QRect(20, 180, 71, 31))
        self.lg_name.setObjectName("lg_name")
        self.startDate = QtWidgets.QLineEdit(self.centralwidget)
        self.startDate.setGeometry(QtCore.QRect(230, 180, 111, 31))
        self.startDate.setObjectName("startDate")
        self.team = QtWidgets.QLineEdit(self.centralwidget)
        self.team.setGeometry(QtCore.QRect(320, 300, 111, 31))
        self.team.setObjectName("team")
        self.position = QtWidgets.QLineEdit(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(210, 300, 71, 31))
        self.position.setObjectName("position")
        self.insertPlayer = QtWidgets.QPushButton(self.centralwidget)
        self.insertPlayer.setGeometry(QtCore.QRect(530, 300, 181, 31))
        self.insertPlayer.setObjectName("insertPlayer")
        
        self.insertPlayer.clicked.connect(self.on_click_player);#######################################################################
         
          
         
        self.birthDate = QtWidgets.QLineEdit(self.centralwidget)
        self.birthDate.setGeometry(QtCore.QRect(110, 300, 81, 31))
        self.birthDate.setObjectName("birthDate")
        self.p_name = QtWidgets.QLineEdit(self.centralwidget)
        self.p_name.setGeometry(QtCore.QRect(20, 300, 71, 31))
        self.p_name.setObjectName("p_name")
        self.createMatch = QtWidgets.QPushButton(self.centralwidget)
        self.createMatch.setGeometry(QtCore.QRect(530, 420, 181, 31))
        self.createMatch.setObjectName("createMatch")
        self.createMatch.clicked.connect(self.on_click_match);##################################################################
        
  
        self.awayGoal = QtWidgets.QLineEdit(self.centralwidget)
        self.awayGoal.setGeometry(QtCore.QRect(340, 420, 61, 31))
        self.awayGoal.setObjectName("awayGoal")
        self.homeTeamName = QtWidgets.QLineEdit(self.centralwidget)
        self.homeTeamName.setGeometry(QtCore.QRect(110, 420, 61, 31))
        self.homeTeamName.setObjectName("homeTeamName")
        self.homeGoal = QtWidgets.QLineEdit(self.centralwidget)
        self.homeGoal.setGeometry(QtCore.QRect(260, 420, 61, 31))
        self.homeGoal.setObjectName("homeGoal")
        self.leagueName = QtWidgets.QLineEdit(self.centralwidget)
        self.leagueName.setGeometry(QtCore.QRect(20, 420, 71, 31))
        self.leagueName.setObjectName("leagueName")
        self.awayTeamName = QtWidgets.QLineEdit(self.centralwidget)
        self.awayTeamName.setGeometry(QtCore.QRect(190, 420, 61, 31))
        self.awayTeamName.setObjectName("awayTeamName")
        self.matchType = QtWidgets.QLineEdit(self.centralwidget)
        self.matchType.setGeometry(QtCore.QRect(420, 420, 71, 31))
        self.matchType.setObjectName("matchType")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 90, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 90, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 220, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 220, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 220, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 340, 71, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 340, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 340, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 340, 41, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 460, 71, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(110, 460, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 460, 51, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(190, 460, 51, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(350, 460, 51, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(426, 460, 61, 20))
        self.label_19.setObjectName("label_19")
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
        self.insertTeam.setText(_translate("MainWindow", "insert new Team"))
        self.insertLeague.setText(_translate("MainWindow", "insert new League"))
        self.insertPlayer.setText(_translate("MainWindow", "insert new Player"))
        self.createMatch.setText(_translate("MainWindow", "enter new Match"))
        self.label.setText(_translate("MainWindow", "team name"))
        self.label_2.setText(_translate("MainWindow", "league name"))
        self.label_3.setText(_translate("MainWindow", "squad name"))
        self.label_4.setText(_translate("MainWindow", "home"))
        self.label_5.setText(_translate("MainWindow", "is_national"))
        self.label_6.setText(_translate("MainWindow", "league name"))
        self.label_7.setText(_translate("MainWindow", "season"))
        self.label_8.setText(_translate("MainWindow", "start date"))
        self.label_9.setText(_translate("MainWindow", "end date"))
        self.label_10.setText(_translate("MainWindow", "player name"))
        self.label_11.setText(_translate("MainWindow", "birthdate"))
        self.label_12.setText(_translate("MainWindow", "position"))
        self.label_13.setText(_translate("MainWindow", "team"))
        self.label_14.setText(_translate("MainWindow", "league name"))
        self.label_15.setText(_translate("MainWindow", "home team"))
        self.label_16.setText(_translate("MainWindow", "home goal"))
        self.label_17.setText(_translate("MainWindow", "away team"))
        self.label_18.setText(_translate("MainWindow", "away goal"))
        self.label_19.setText(_translate("MainWindow", "match type"))
    def on_click_team(self): 
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
        cur=con.cursor()
        
       # tm_name1,lg_nm1,sqd_id1,address1,home1,is_national1
        
        tm_name1=self.tm_name.text()
        lg_nm1=self.lg_nm.text()
        sqd_id1=self.sqd_id.text()
        address1=self.home.text()
        home1=self.home.text()
        is_national1=self.is_national.text()
        arr=[tm_name1,int(lg_nm1),int(sqd_id1),address1,home1,int(is_national1)]
       # print(arr)
        cur.callproc('insert_new_team',arr)
        
        
    def on_click_league(self): 
         #  season,endDate,lg_name,startDate
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
        cur=con.cursor()
        season1=self.season.text()
        endDate1=self.enndDate.text()
        startDate1=self.startDate.text()
        lg_nm1=self.lg_nm.text()
        arr=[lg_nm1,season1,startDate1,endDate1]
        cur.callproc('insert_new_league',arr)
    
    
    
    def on_click_player(self):
         #  season,endDate,lg_name,startDate
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
        cur=con.cursor()
        p_name1=self.p_name.text()
        birth1=self.birth.text()
        position1=self.position1.text()
        team1=self.team.text()
        arr=[p_name1,birth1,position1,team1]
        cur.callproc('insert_player',arr)
    
    def on_click_match(self):
        con=cx_Oracle.connect('dbms_project/proc123@127.0.0.1:1522/orcl')
        cur=con.cursor()
        lg1=self.leagueName.text()
        home1=self.homeTeamName.text()
        away=self.awayTeamName.text()
        hg=self.homeGoal.text()
        ag=self.awayGoal.text()
        hg=int(hg)
        ag=int(ag)
        wn=0
        tp=self.matchType.text()
        arr=[lg1,home1,away,hg,ag,wn,tp]
        cur.callproc('create_match',arr)
        

       
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

