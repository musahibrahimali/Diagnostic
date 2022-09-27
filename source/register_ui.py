# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'registerigyNSx.ui'
##
# Created by: Qt User Interface Compiler version 6.3.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 371, 161))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EmailTextField = QLineEdit(self.layoutWidget)
        self.EmailTextField.setObjectName(u"EmailTextField")

        self.gridLayout.addWidget(self.EmailTextField, 1, 1, 1, 1)

        self.EmailLabel = QLabel(self.layoutWidget)
        self.EmailLabel.setObjectName(u"EmailLabel")

        self.gridLayout.addWidget(self.EmailLabel, 1, 0, 1, 1)

        self.PasswordTextField = QLineEdit(self.layoutWidget)
        self.PasswordTextField.setObjectName(u"PasswordTextField")

        self.gridLayout.addWidget(self.PasswordTextField, 2, 1, 1, 1)

        self.PasswordLabel = QLabel(self.layoutWidget)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.gridLayout.addWidget(self.PasswordLabel, 2, 0, 1, 1)

        self.NameLabel = QLabel(self.layoutWidget)
        self.NameLabel.setObjectName(u"NameLabel")

        self.gridLayout.addWidget(self.NameLabel, 0, 0, 1, 1)

        self.NameTextField = QLineEdit(self.layoutWidget)
        self.NameTextField.setObjectName(u"NameTextField")

        self.gridLayout.addWidget(self.NameTextField, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 230, 251, 56))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LoginButton = QPushButton(self.layoutWidget1)
        self.LoginButton.setObjectName(u"LoginButton")

        self.gridLayout_2.addWidget(self.LoginButton, 1, 0, 1, 1)

        self.RegisterButton = QPushButton(self.layoutWidget1)
        self.RegisterButton.setObjectName(u"RegisterButton")

        self.gridLayout_2.addWidget(self.RegisterButton, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 421, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.NameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.RegisterButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
    # retranslateUi
