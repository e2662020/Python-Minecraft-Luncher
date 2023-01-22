# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

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
        self.frame_3.setGeometry(QRect(10, 510, 781, 81))
        self.frame_3.setStyleSheet(u"background-color: rgba(85, 190, 240, 0.5);\n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(619, 11, 151, 61))
        self.pushButton_3.setStyleSheet(u"background-color: rgba(255,255,255,0.3); \n"
"border-radius: 5px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-end-end-radius: 0px;\n"
"color: white;\n"
"font-size: 16px;")
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(500, 10, 101, 61))
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
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#ffffff;\">PML</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u4e0b\u8f7d", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u542f\u52a8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u542f\u52a8\uff01", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.19</p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

