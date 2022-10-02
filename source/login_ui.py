# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'loginEhzmQa.ui'
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
from PySide2.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QScrollArea,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 271)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 9, 331, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 329, 219))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 271, 81))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PasswordLabel = QLabel(self.layoutWidget)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.gridLayout.addWidget(self.PasswordLabel, 1, 0, 1, 1)

        self.EmailLabel = QLabel(self.layoutWidget)
        self.EmailLabel.setObjectName(u"EmailLabel")

        self.gridLayout.addWidget(self.EmailLabel, 0, 0, 1, 1)

        self.EmailTextField = QLineEdit(self.layoutWidget)
        self.EmailTextField.setObjectName(u"EmailTextField")

        self.gridLayout.addWidget(self.EmailTextField, 0, 1, 1, 1)

        self.PasswordTextField = QLineEdit(self.layoutWidget)
        self.PasswordTextField.setObjectName(u"PasswordTextField")

        self.gridLayout.addWidget(self.PasswordTextField, 1, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 120, 151, 56))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RegisterButton = QPushButton(self.layoutWidget1)
        self.RegisterButton.setObjectName(u"RegisterButton")

        self.gridLayout_2.addWidget(self.RegisterButton, 1, 0, 1, 1)

        self.LoginButton = QPushButton(self.layoutWidget1)
        self.LoginButton.setObjectName(u"LoginButton")

        self.gridLayout_2.addWidget(self.LoginButton, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 345, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.RegisterButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi
