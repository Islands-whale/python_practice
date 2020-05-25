# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_graphic_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class QtUiForm(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setMinimumSize(QtCore.QSize(500, 400))
        Form.setMaximumSize(QtCore.QSize(500, 400))
        self.path_label = QtWidgets.QLabel(Form)
        self.path_label.setGeometry(QtCore.QRect(30, 30, 31, 20))
        self.path_label.setObjectName("path_label")
        self.path = QtWidgets.QLineEdit(Form)
        self.path.setGeometry(QtCore.QRect(80, 30, 281, 20))
        self.path.setObjectName("path_edit")
        self.start_label = QtWidgets.QLabel(Form)
        self.start_label.setGeometry(QtCore.QRect(30, 70, 41, 20))
        self.start_label.setObjectName("start_label")
        self.step_label = QtWidgets.QLabel(Form)
        self.step_label.setGeometry(QtCore.QRect(280, 70, 31, 20))
        self.step_label.setObjectName("step_label")
        self.start = QtWidgets.QLineEdit(Form)
        self.start.setGeometry(QtCore.QRect(80, 70, 41, 20))
        self.start.setObjectName("start_edit")
        self.start.setText('1')
        self.step = QtWidgets.QLineEdit(Form)
        self.step.setGeometry(QtCore.QRect(320, 70, 41, 20))
        self.step.setObjectName("step_edit")
        self.step.setText('1')
        self.path_button = QtWidgets.QPushButton(Form)
        self.path_button.setGeometry(QtCore.QRect(390, 30, 75, 23))
        self.path_button.setObjectName("path_button")
        self.confirm_button = QtWidgets.QPushButton(Form)
        self.confirm_button.setGeometry(QtCore.QRect(390, 70, 75, 23))
        self.confirm_button.setObjectName("confirm_button")
        self.quit_button = QtWidgets.QPushButton(Form)
        self.quit_button.setGeometry(QtCore.QRect(390, 110, 75, 23))
        self.quit_button.setObjectName("quit_button")
        self.out_browser = QtWidgets.QTextBrowser(Form)
        self.out_browser.setGeometry(QtCore.QRect(80, 130, 281, 192))
        self.out_browser.setObjectName("out_browser")
        self.out_label = QtWidgets.QLabel(Form)
        self.out_label.setGeometry(QtCore.QRect(30, 130, 41, 20))
        self.out_label.setObjectName("out_label")

        self.retranslate_ui(Form)
        self.quit_button.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "约瑟夫环"))
        self.path_label.setText(_translate("Form", "路径"))
        self.start_label.setText(_translate("Form", "起始值"))
        self.step_label.setText(_translate("Form", "步进"))
        self.path_button.setText(_translate("Form", "选择文件"))
        self.confirm_button.setText(_translate("Form", "确认"))
        self.quit_button.setText(_translate("Form", "退出"))
        self.out_label.setText(_translate("Form", "输出"))
