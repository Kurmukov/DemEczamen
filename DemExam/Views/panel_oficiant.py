# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel_oficiant.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(350, 10, 321, 70))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 140, 121, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 140, 161, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(370, 140, 161, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(560, 140, 161, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.Namber_table = QtWidgets.QLineEdit(self.centralwidget)
        self.Namber_table.setGeometry(QtCore.QRect(20, 190, 113, 26))
        self.Namber_table.setObjectName("Namber_table")
        self.Namber_table_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Namber_table_2.setGeometry(QtCore.QRect(20, 230, 113, 26))
        self.Namber_table_2.setObjectName("Namber_table_2")
        self.Namber_table_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Namber_table_3.setGeometry(QtCore.QRect(20, 270, 113, 26))
        self.Namber_table_3.setObjectName("Namber_table_3")
        self.poset = QtWidgets.QLineEdit(self.centralwidget)
        self.poset.setGeometry(QtCore.QRect(200, 190, 113, 26))
        self.poset.setObjectName("poset")
        self.poset_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.poset_3.setGeometry(QtCore.QRect(200, 270, 113, 26))
        self.poset_3.setObjectName("poset_3")
        self.poset_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.poset_2.setGeometry(QtCore.QRect(200, 230, 113, 26))
        self.poset_2.setObjectName("poset_2")
        self.foot = QtWidgets.QLineEdit(self.centralwidget)
        self.foot.setGeometry(QtCore.QRect(390, 190, 113, 26))
        self.foot.setObjectName("foot")
        self.foot_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.foot_3.setGeometry(QtCore.QRect(390, 270, 113, 26))
        self.foot_3.setObjectName("foot_3")
        self.foot_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.foot_2.setGeometry(QtCore.QRect(390, 230, 113, 26))
        self.foot_2.setObjectName("foot_2")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(560, 190, 80, 26))
        self.enter.setObjectName("enter")
        self.buy = QtWidgets.QPushButton(self.centralwidget)
        self.buy.setGeometry(QtCore.QRect(650, 190, 80, 26))
        self.buy.setObjectName("buy")
        self.enter_2 = QtWidgets.QPushButton(self.centralwidget)
        self.enter_2.setGeometry(QtCore.QRect(560, 230, 80, 26))
        self.enter_2.setObjectName("enter_2")
        self.buy_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buy_2.setGeometry(QtCore.QRect(650, 230, 80, 26))
        self.buy_2.setObjectName("buy_2")
        self.enter_3 = QtWidgets.QPushButton(self.centralwidget)
        self.enter_3.setGeometry(QtCore.QRect(560, 270, 80, 26))
        self.enter_3.setObjectName("enter_3")
        self.buy_3 = QtWidgets.QPushButton(self.centralwidget)
        self.buy_3.setGeometry(QtCore.QRect(650, 270, 80, 26))
        self.buy_3.setObjectName("buy_3")
        self.kol_vo_posit = QtWidgets.QTextEdit(self.centralwidget)
        self.kol_vo_posit.setGeometry(QtCore.QRect(180, 320, 161, 31))
        self.kol_vo_posit.setObjectName("kol_vo_posit")
        self.numder_show = QtWidgets.QTextEdit(self.centralwidget)
        self.numder_show.setGeometry(QtCore.QRect(20, 320, 121, 31))
        self.numder_show.setObjectName("numder_show")
        self.state_show = QtWidgets.QTextEdit(self.centralwidget)
        self.state_show.setGeometry(QtCore.QRect(560, 320, 161, 31))
        self.state_show.setObjectName("state_show")
        self.foot_show = QtWidgets.QTextEdit(self.centralwidget)
        self.foot_show.setGeometry(QtCore.QRect(370, 320, 161, 31))
        self.foot_show.setObjectName("foot_show")
        self.kol_vo_posit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.kol_vo_posit_2.setGeometry(QtCore.QRect(180, 360, 161, 31))
        self.kol_vo_posit_2.setObjectName("kol_vo_posit_2")
        self.numder_2_show = QtWidgets.QTextEdit(self.centralwidget)
        self.numder_2_show.setGeometry(QtCore.QRect(20, 360, 121, 31))
        self.numder_2_show.setObjectName("numder_2_show")
        self.state_show_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.state_show_2.setGeometry(QtCore.QRect(560, 360, 161, 31))
        self.state_show_2.setObjectName("state_show_2")
        self.foot_show_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.foot_show_2.setGeometry(QtCore.QRect(370, 360, 161, 31))
        self.foot_show_2.setObjectName("foot_show_2")
        self.kol_vo_posit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.kol_vo_posit_3.setGeometry(QtCore.QRect(180, 400, 161, 31))
        self.kol_vo_posit_3.setObjectName("kol_vo_posit_3")
        self.numder_3_show = QtWidgets.QTextEdit(self.centralwidget)
        self.numder_3_show.setGeometry(QtCore.QRect(20, 400, 121, 31))
        self.numder_3_show.setObjectName("numder_3_show")
        self.state_show_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.state_show_3.setGeometry(QtCore.QRect(560, 400, 161, 31))
        self.state_show_3.setObjectName("state_show_3")
        self.foot_show_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.foot_show_3.setGeometry(QtCore.QRect(370, 400, 161, 31))
        self.foot_show_3.setObjectName("foot_show_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 23))
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
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Панель официанта</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Номер столика</p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Кол-во поситителей</p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Блюда и напитки</p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Статус</p></body></html>"))
        self.Namber_table.setPlaceholderText(_translate("MainWindow", "Номер столика"))
        self.Namber_table_2.setPlaceholderText(_translate("MainWindow", "Номер столика"))
        self.Namber_table_3.setPlaceholderText(_translate("MainWindow", "Номер столика"))
        self.poset.setPlaceholderText(_translate("MainWindow", "Кол-во"))
        self.poset_3.setPlaceholderText(_translate("MainWindow", "Кол-во"))
        self.poset_2.setPlaceholderText(_translate("MainWindow", "Кол-во"))
        self.foot.setPlaceholderText(_translate("MainWindow", "блюда и напитки"))
        self.foot_3.setPlaceholderText(_translate("MainWindow", "блюда и напитки"))
        self.foot_2.setPlaceholderText(_translate("MainWindow", "блюда и напитки"))
        self.enter.setText(_translate("MainWindow", "принят"))
        self.buy.setText(_translate("MainWindow", "оплачен"))
        self.enter_2.setText(_translate("MainWindow", "принят"))
        self.buy_2.setText(_translate("MainWindow", "оплачен"))
        self.enter_3.setText(_translate("MainWindow", "принят"))
        self.buy_3.setText(_translate("MainWindow", "оплачен"))
        self.kol_vo_posit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>"))
        self.numder_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.state_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">принят</p></body></html>"))
        self.foot_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Блюда и напитки</p></body></html>"))
        self.kol_vo_posit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.numder_2_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>"))
        self.state_show_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">принят</p></body></html>"))
        self.foot_show_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Блюда и напитки</p></body></html>"))
        self.kol_vo_posit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>"))
        self.numder_3_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.state_show_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">принят</p></body></html>"))
        self.foot_show_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Блюда и напитки</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())