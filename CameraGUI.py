# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CameraGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 335)
        self.CamLB = QtWidgets.QLabel(Form)
        self.CamLB.setGeometry(QtCore.QRect(150, 30, 271, 161))
        self.CamLB.setText("")
        self.CamLB.setObjectName("CamLB")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 230, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(10, 20, 75, 46))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.ForwardBT = QtWidgets.QPushButton(self.splitter_3)
        self.ForwardBT.setObjectName("ForwardBT")
        self.BackwardBT = QtWidgets.QPushButton(self.splitter_3)
        self.BackwardBT.setObjectName("BackwardBT")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 120, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 75, 46))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.OpenCamBT = QtWidgets.QPushButton(self.splitter)
        self.OpenCamBT.setObjectName("OpenCamBT")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 120, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_2.setGeometry(QtCore.QRect(20, 20, 75, 46))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.StartBT = QtWidgets.QPushButton(self.splitter_2)
        self.StartBT.setObjectName("StartBT")
        self.ResetBT = QtWidgets.QPushButton(self.splitter_2)
        self.ResetBT.setObjectName("ResetBT")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(180, 230, 231, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.GetherBT = QtWidgets.QPushButton(self.groupBox_4)
        self.GetherBT.setGeometry(QtCore.QRect(21, 21, 75, 23))
        self.GetherBT.setObjectName("GetherBT")
        self.CrossBT = QtWidgets.QPushButton(self.groupBox_4)
        self.CrossBT.setGeometry(QtCore.QRect(102, 21, 75, 23))
        self.CrossBT.setObjectName("CrossBT")
        self.LeftBT = QtWidgets.QPushButton(self.groupBox_4)
        self.LeftBT.setGeometry(QtCore.QRect(21, 50, 75, 23))
        self.LeftBT.setObjectName("LeftBT")
        self.RightBT = QtWidgets.QPushButton(self.groupBox_4)
        self.RightBT.setGeometry(QtCore.QRect(102, 50, 75, 23))
        self.RightBT.setObjectName("RightBT")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "步行步态"))
        self.ForwardBT.setText(_translate("Form", "前进"))
        self.BackwardBT.setText(_translate("Form", "后退"))
        self.groupBox_2.setTitle(_translate("Form", "摄像头控制"))
        self.OpenCamBT.setText(_translate("Form", "打开摄像头"))
        self.groupBox_3.setTitle(_translate("Form", "系统设置"))
        self.StartBT.setText(_translate("Form", "系统上电"))
        self.ResetBT.setText(_translate("Form", "复位"))
        self.groupBox_4.setTitle(_translate("Form", "游动步态"))
        self.GetherBT.setText(_translate("Form", "同步游动"))
        self.CrossBT.setText(_translate("Form", "交错游动"))
        self.LeftBT.setText(_translate("Form", "左转"))
        self.RightBT.setText(_translate("Form", "右转"))
