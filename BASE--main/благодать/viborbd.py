# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viborbd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 400)
        Form.setStyleSheet("background-color: rgb(33, 33, 33)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 60, 121, 16))
        self.label.setStyleSheet("color: rgb(20, 255, 236)")
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(110, 110, 131, 121))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setStyleSheet("color: rgb(20, 255, 236)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setStyleSheet("color: rgb(20, 255, 236)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(320, 110, 131, 121))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_3.setStyleSheet("color: rgb(20, 255, 236)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_4.setStyleSheet("color: rgb(20, 255, 236)")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Выберите базу данных"))
        self.pushButton.setText(_translate("Form", "services"))
        self.pushButton_2.setText(_translate("Form", "workers"))
        self.pushButton_3.setText(_translate("Form", "client"))
        self.pushButton_4.setText(_translate("Form", "zakazi"))
