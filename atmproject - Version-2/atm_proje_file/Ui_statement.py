# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\pythonogreniyorum\ATM-Project\atmproject - Version-2\atm_proje_file\statement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statementScreen(object):
    def setupUi(self, statementScreen):
        statementScreen.setObjectName("statementScreen")
        statementScreen.resize(609, 638)
        statementScreen.setMinimumSize(QtCore.QSize(609, 638))
        statementScreen.setMaximumSize(QtCore.QSize(609, 638))
        font = QtGui.QFont()
        font.setPointSize(12)
        statementScreen.setFont(font)
        statementScreen.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget = QtWidgets.QWidget(statementScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.account_lable = QtWidgets.QLabel(self.centralwidget)
        self.account_lable.setGeometry(QtCore.QRect(180, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.account_lable.setFont(font)
        self.account_lable.setStyleSheet("background-color: rgb(102, 204, 255);")
        self.account_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.account_lable.setObjectName("account_lable")
        self.return4_button = QtWidgets.QPushButton(self.centralwidget)
        self.return4_button.setGeometry(QtCore.QRect(350, 500, 171, 41))
        self.return4_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\pythonogreniyorum\\ATM-Project\\atmproject - Version-2\\atm_proje_file\\../pythonogreniyorum/ATM-Project/atmproject/gümüst/icons/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\pythonogreniyorum\\ATM-Project\\atmproject - Version-2\\atm_proje_file\\../pythonogreniyorum/ATM-Project/gümüst/icons/icns/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.return4_button.setIcon(icon)
        self.return4_button.setIconSize(QtCore.QSize(50, 50))
        self.return4_button.setObjectName("return4_button")
        self.date_button = QtWidgets.QPushButton(self.centralwidget)
        self.date_button.setGeometry(QtCore.QRect(10, 500, 131, 41))
        self.date_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.date_button.setObjectName("date_button")
        self.logins_button = QtWidgets.QPushButton(self.centralwidget)
        self.logins_button.setGeometry(QtCore.QRect(10, 310, 131, 41))
        self.logins_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.logins_button.setObjectName("logins_button")
        self.aktivites_button = QtWidgets.QPushButton(self.centralwidget)
        self.aktivites_button.setGeometry(QtCore.QRect(10, 70, 131, 41))
        self.aktivites_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.aktivites_button.setObjectName("aktivites_button")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(10, 550, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.date_label.setText("")
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 360, 581, 131))
        self.textBrowser.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 120, 581, 151))
        self.textBrowser_2.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        statementScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(statementScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        statementScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(statementScreen)
        self.statusbar.setObjectName("statusbar")
        statementScreen.setStatusBar(self.statusbar)

        self.retranslateUi(statementScreen)
        self.aktivites_button.clicked.connect(self.textBrowser_2.show)
        self.logins_button.clicked.connect(self.textBrowser.show)
        QtCore.QMetaObject.connectSlotsByName(statementScreen)

    def retranslateUi(self, statementScreen):
        _translate = QtCore.QCoreApplication.translate
        statementScreen.setWindowTitle(_translate("statementScreen", "statement"))
        self.account_lable.setText(_translate("statementScreen", "ACCOUNT TRANSACTIONS"))
        self.return4_button.setText(_translate("statementScreen", "RETURN MENU"))
        self.date_button.setText(_translate("statementScreen", "CREATING DATE"))
        self.logins_button.setText(_translate("statementScreen", "LOGINS"))
        self.aktivites_button.setText(_translate("statementScreen", "MONEY ACTIVITES"))
        self.textBrowser.setHtml(_translate("statementScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("statementScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))