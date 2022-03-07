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
        MainWindow.resize(472, 217)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.filepath = QLineEdit(self.centralwidget)
        self.filepath.setObjectName(u"filepath")
        self.filepath.setGeometry(QRect(70, 30, 211, 21))
        self.choose_file_button = QPushButton(self.centralwidget)
        self.choose_file_button.setObjectName(u"choose_file_button")
        self.choose_file_button.setGeometry(QRect(300, 30, 101, 21))
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(170, 130, 75, 23))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 100, 331, 21))
        self.progressBar.setValue(0)
        self.output_filepath = QLineEdit(self.centralwidget)
        self.output_filepath.setObjectName(u"output_filepath")
        self.output_filepath.setGeometry(QRect(70, 60, 211, 21))
        self.choose_output_dir_button = QPushButton(self.centralwidget)
        self.choose_output_dir_button.setObjectName(u"choose_output_dir_button")
        self.choose_output_dir_button.setGeometry(QRect(300, 60, 101, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 472, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_file_button.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6b4c\u540d\u6587\u4ef6", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u83b7\u53d6", None))
        self.choose_output_dir_button.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u76ee\u5f55", None))
    # retranslateUi

