# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1015, 801)
        icon = QIcon()
        icon.addFile(u"resources/ico.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 85, 0);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_pic = QLabel(Form)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setMinimumSize(QSize(995, 556))

        self.verticalLayout.addWidget(self.label_pic)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.progressBar.setFont(font1)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.progressBar)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 20))
        self.lineEdit.setFont(font1)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.retranslateUi(Form)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AI\u4f5c\u753b\uff08Disco Diffusion 5.2\uff09\u5c0f\u5de5\u5177\u79bb\u7ebf\u7248V3.0\uff08\u5c0f\u5de5\u5177\u4f5c\u8005\u5fae\u4fe1\u516c\u4f17\u53f7\uff1a\u4e07\u80fd\u641c\u5427\uff09", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6253\u8d4f\u4e0e\u8054\u7cfb\u6211", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u6559\u7a0b\u63a8\u8350", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.label_pic.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"%p%[%v/%m]", None))
    # retranslateUi

