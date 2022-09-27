# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'patient_clinician_optionPjYmaJ.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QStatusBar, QWidget)


class Ui_PatientClinician(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 120, 301, 111))
        self.PatientClinicianBox = QGridLayout(self.layoutWidget)
        self.PatientClinicianBox.setObjectName(u"PatientClinicianBox")
        self.PatientClinicianBox.setContentsMargins(0, 0, 0, 0)
        self.ClinicianButton = QPushButton(self.layoutWidget)
        self.ClinicianButton.setObjectName(u"ClinicianButton")

        self.PatientClinicianBox.addWidget(self.ClinicianButton, 1, 0, 1, 1)

        self.PatientButton = QPushButton(self.layoutWidget)
        self.PatientButton.setObjectName(u"PatientButton")

        self.PatientClinicianBox.addWidget(self.PatientButton, 0, 0, 1, 1)

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
        self.ClinicianButton.setText(QCoreApplication.translate("MainWindow", u"CLINICIAN", None))
        self.PatientButton.setText(QCoreApplication.translate("MainWindow", u"PATIENT", None))
    # retranslateUi
