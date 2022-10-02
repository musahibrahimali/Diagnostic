# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login_register_option.ui'
##
# Created by: Qt User Interface Compiler version 6.3.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QWidget)


class Ui_LoginRegister(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 165)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 30, 191, 61))
        self.LoginRegisterBox = QGridLayout(self.layoutWidget)
        self.LoginRegisterBox.setObjectName(u"LoginRegisterBox")
        self.LoginRegisterBox.setContentsMargins(0, 0, 0, 0)
        self.RegisterButton = QPushButton(self.layoutWidget)
        self.RegisterButton.setObjectName(u"RegisterButton")

        self.LoginRegisterBox.addWidget(self.RegisterButton, 1, 0, 1, 1)

        self.LoginButton = QPushButton(self.layoutWidget)
        self.LoginButton.setObjectName(u"LoginButton")

        self.LoginRegisterBox.addWidget(self.LoginButton, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 315, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RegisterButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi
