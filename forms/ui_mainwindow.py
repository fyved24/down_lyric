# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 278)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.filepath = QLineEdit(self.centralwidget)
        self.filepath.setObjectName(u"filepath")
        self.filepath.setGeometry(QRect(110, 80, 211, 21))
        self.choose_file_button = QPushButton(self.centralwidget)
        self.choose_file_button.setObjectName(u"choose_file_button")
        self.choose_file_button.setGeometry(QRect(340, 80, 101, 21))
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(210, 180, 75, 23))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(110, 150, 331, 21))
        self.progressBar.setValue(0)
        self.output_filepath = QLineEdit(self.centralwidget)
        self.output_filepath.setObjectName(u"output_filepath")
        self.output_filepath.setGeometry(QRect(110, 110, 211, 21))
        self.choose_output_dir_button = QPushButton(self.centralwidget)
        self.choose_output_dir_button.setObjectName(u"choose_output_dir_button")
        self.choose_output_dir_button.setGeometry(QRect(340, 110, 101, 21))
        self.down_source = QComboBox(self.centralwidget)
        self.down_source.addItem("")
        self.down_source.addItem("")
        self.down_source.setObjectName(u"down_source")
        self.down_source.setGeometry(QRect(170, 40, 69, 22))
        self.options_num = QComboBox(self.centralwidget)
        self.options_num.addItem("")
        self.options_num.addItem("")
        self.options_num.addItem("")
        self.options_num.setObjectName(u"options_num")
        self.options_num.setGeometry(QRect(340, 40, 69, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 54, 12))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 40, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_file_button.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6b4c\u540d\u6587\u4ef6", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u83b7\u53d6", None))
        self.choose_output_dir_button.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u76ee\u5f55", None))
        self.down_source.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u6613\u4e91", None))
        self.down_source.setItemText(1, QCoreApplication.translate("MainWindow", u"QQ\u97f3\u4e50", None))

        self.options_num.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.options_num.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.options_num.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6e90", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5907\u9009\u6570\u91cf", None))
    # retranslateUi
