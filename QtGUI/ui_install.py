# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'install.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMinimumSize(QSize(800, 600))
        Widget.setMaximumSize(QSize(800, 600))
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 61))
        self.frame.setStyleSheet(u"background-color: rgb(85, 190, 240);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 81, 41))
        self.label.setStyleSheet(u"font: 40pt;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 10, 101, 41))
        self.pushButton.setStyleSheet(u"background-color: rgba(255,255,255,0.3); \n"
"border-radius: 0px;\n"
"color: white;\n"
"font-size: 16px;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 10, 101, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255,255,255,0.3); \n"
"border-radius: 0px;\n"
"color: white;\n"
"font-size: 16px;")
        self.frame_3 = QFrame(Widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 80, 781, 511))
        self.frame_3.setStyleSheet(u"background-color: rgba(85, 190, 240, 0.5);\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 30, 761, 31))
        self.comboBox.setStyleSheet(u"border-radius: 0px;")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 81, 16))
        self.label_3.setStyleSheet(u"border-radius: 0px;")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(670, 60, 100, 32))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-140, 0, 1041, 601))
        self.label_2.setPixmap(QPixmap(u"img/background.jpg"))
        self.label_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"PML - Install", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#ffffff;\">PML</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u4e0b\u8f7d", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u542f\u52a8", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u8bf7\u9009\u62e9\u7248\u672c\u53f7", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u4e0b\u8f7d", None))
        self.label_2.setText("")
    # retranslateUi

