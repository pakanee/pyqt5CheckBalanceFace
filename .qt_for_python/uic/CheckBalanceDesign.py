# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CheckBalanceDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import MyImage_rc

class Ui_CheckBalance(object):
    def setupUi(self, CheckBalance):
        if not CheckBalance.objectName():
            CheckBalance.setObjectName(u"CheckBalance")
        CheckBalance.resize(900, 505)
        self.centralwidget = QWidget(CheckBalance)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsViewPerson = QGraphicsView(self.centralwidget)
        self.graphicsViewPerson.setObjectName(u"graphicsViewPerson")
        self.graphicsViewPerson.setGeometry(QRect(10, 10, 211, 91))
        self.graphicsViewPerson.setStyleSheet(u"image: url(:/image/TCMLOGO.jfif);\n"
"background-image: url(:/image/TCMLOGO.jfif);")
        self.labe_lCardNo = QLabel(self.centralwidget)
        self.labe_lCardNo.setObjectName(u"labe_lCardNo")
        self.labe_lCardNo.setGeometry(QRect(230, 30, 91, 21))
        font = QFont()
        font.setFamily(u"Angsana New")
        font.setPointSize(24)
        self.labe_lCardNo.setFont(font)
        self.lineEdit_PersonNo = QLineEdit(self.centralwidget)
        self.lineEdit_PersonNo.setObjectName(u"lineEdit_PersonNo")
        self.lineEdit_PersonNo.setGeometry(QRect(10, 140, 211, 41))
        self.label_PersonNo = QLabel(self.centralwidget)
        self.label_PersonNo.setObjectName(u"label_PersonNo")
        self.label_PersonNo.setGeometry(QRect(10, 110, 131, 21))
        self.label_PersonNo.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 110, 131, 21))
        self.label_3.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 280, 871, 181))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_AmountCanUse = QLabel(self.centralwidget)
        self.label_AmountCanUse.setObjectName(u"label_AmountCanUse")
        self.label_AmountCanUse.setGeometry(QRect(560, 20, 321, 91))
        font1 = QFont()
        font1.setFamily(u"Angsana New")
        font1.setPointSize(72)
        font1.setBold(True)
        self.label_AmountCanUse.setFont(font1)
        self.label_AmountCanUse.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_AmountCanUse.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_personLeave = QLineEdit(self.centralwidget)
        self.lineEdit_personLeave.setObjectName(u"lineEdit_personLeave")
        self.lineEdit_personLeave.setGeometry(QRect(10, 220, 211, 41))
        self.label_PersonalLeave = QLabel(self.centralwidget)
        self.label_PersonalLeave.setObjectName(u"label_PersonalLeave")
        self.label_PersonalLeave.setGeometry(QRect(10, 190, 131, 31))
        self.label_PersonalLeave.setFont(font)
        self.lineEdit_RemainingLeave = QLineEdit(self.centralwidget)
        self.lineEdit_RemainingLeave.setObjectName(u"lineEdit_RemainingLeave")
        self.lineEdit_RemainingLeave.setGeometry(QRect(670, 220, 211, 41))
        self.lineEdit_MedicalExpenses = QLineEdit(self.centralwidget)
        self.lineEdit_MedicalExpenses.setObjectName(u"lineEdit_MedicalExpenses")
        self.lineEdit_MedicalExpenses.setGeometry(QRect(230, 220, 211, 41))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(450, 220, 211, 41))
        self.label_Department = QLabel(self.centralwidget)
        self.label_Department.setObjectName(u"label_Department")
        self.label_Department.setGeometry(QRect(580, 110, 131, 31))
        self.label_Department.setFont(font)
        self.label_RemainingLeave = QLabel(self.centralwidget)
        self.label_RemainingLeave.setObjectName(u"label_RemainingLeave")
        self.label_RemainingLeave.setGeometry(QRect(230, 190, 151, 31))
        self.label_RemainingLeave.setFont(font)
        self.label_MedicalExpense = QLabel(self.centralwidget)
        self.label_MedicalExpense.setObjectName(u"label_MedicalExpense")
        self.label_MedicalExpense.setGeometry(QRect(450, 190, 151, 31))
        self.label_MedicalExpense.setFont(font)
        self.lineEdit_cardNo = QLineEdit(self.centralwidget)
        self.lineEdit_cardNo.setObjectName(u"lineEdit_cardNo")
        self.lineEdit_cardNo.setGeometry(QRect(230, 60, 321, 41))
        self.lineEdit_PersonName = QLineEdit(self.centralwidget)
        self.lineEdit_PersonName.setObjectName(u"lineEdit_PersonName")
        self.lineEdit_PersonName.setGeometry(QRect(230, 140, 331, 41))
        self.lineEdit_DepartMent = QLineEdit(self.centralwidget)
        self.lineEdit_DepartMent.setObjectName(u"lineEdit_DepartMent")
        self.lineEdit_DepartMent.setGeometry(QRect(570, 140, 311, 41))
        self.label_MedicalRemaining = QLabel(self.centralwidget)
        self.label_MedicalRemaining.setObjectName(u"label_MedicalRemaining")
        self.label_MedicalRemaining.setGeometry(QRect(670, 190, 161, 31))
        self.label_MedicalRemaining.setFont(font)
        self.pushButton_API = QPushButton(self.centralwidget)
        self.pushButton_API.setObjectName(u"pushButton_API")
        self.pushButton_API.setGeometry(QRect(360, 10, 111, 41))
        CheckBalance.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CheckBalance)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        CheckBalance.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CheckBalance)
        self.statusbar.setObjectName(u"statusbar")
        CheckBalance.setStatusBar(self.statusbar)

        self.retranslateUi(CheckBalance)

        QMetaObject.connectSlotsByName(CheckBalance)
    # setupUi

    def retranslateUi(self, CheckBalance):
        CheckBalance.setWindowTitle(QCoreApplication.translate("CheckBalance", u"Check Balance", None))
        self.labe_lCardNo.setText(QCoreApplication.translate("CheckBalance", u"Card No", None))
        self.label_PersonNo.setText(QCoreApplication.translate("CheckBalance", u"Person No.", None))
        self.label_3.setText(QCoreApplication.translate("CheckBalance", u"Person Name ", None))
        self.label_AmountCanUse.setText(QCoreApplication.translate("CheckBalance", u"0.00", None))
        self.label_PersonalLeave.setText(QCoreApplication.translate("CheckBalance", u"Personal Leave", None))
        self.label_Department.setText(QCoreApplication.translate("CheckBalance", u"Department", None))
        self.label_RemainingLeave.setText(QCoreApplication.translate("CheckBalance", u"Remaining Leave", None))
        self.label_MedicalExpense.setText(QCoreApplication.translate("CheckBalance", u"Medical Expenses", None))
        self.label_MedicalRemaining.setText(QCoreApplication.translate("CheckBalance", u"Medical remaining", None))
        self.pushButton_API.setText(QCoreApplication.translate("CheckBalance", u"API", None))
    # retranslateUi

