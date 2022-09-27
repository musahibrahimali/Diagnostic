# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_windowVCYyLe.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QMenuBar, QProgressBar, QPushButton,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 616)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RecordStopBox = QWidget(self.centralwidget)
        self.RecordStopBox.setObjectName(u"RecordStopBox")
        self.RecordStopBox.setGeometry(QRect(170, 10, 551, 61))
        self.layoutWidget = QWidget(self.RecordStopBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 501, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.RecordButton = QPushButton(self.layoutWidget)
        self.RecordButton.setObjectName(u"RecordButton")

        self.horizontalLayout.addWidget(self.RecordButton)

        self.StopButton = QPushButton(self.layoutWidget)
        self.StopButton.setObjectName(u"StopButton")

        self.horizontalLayout.addWidget(self.StopButton)

        self.ContentBox = QWidget(self.centralwidget)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setGeometry(QRect(60, 140, 841, 431))
        self.ProceedButton = QPushButton(self.ContentBox)
        self.ProceedButton.setObjectName(u"ProceedButton")
        self.ProceedButton.setGeometry(QRect(220, 370, 351, 51))
        self.layoutWidget1 = QWidget(self.ContentBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 821, 261))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.FirstGraph = QLabel(self.layoutWidget1)
        self.FirstGraph.setObjectName(u"FirstGraph")

        self.gridLayout.addWidget(self.FirstGraph, 0, 0, 1, 1)

        self.SecondGraph = QLabel(self.layoutWidget1)
        self.SecondGraph.setObjectName(u"SecondGraph")

        self.gridLayout.addWidget(self.SecondGraph, 0, 1, 1, 1)

        self.layoutWidget2 = QWidget(self.ContentBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 300, 821, 41))
        self.gridLayout_2 = QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DurationText = QLabel(self.layoutWidget2)
        self.DurationText.setObjectName(u"DurationText")

        self.gridLayout_2.addWidget(self.DurationText, 0, 1, 1, 1)

        self.VolumeLabel = QLabel(self.layoutWidget2)
        self.VolumeLabel.setObjectName(u"VolumeLabel")

        self.gridLayout_2.addWidget(self.VolumeLabel, 0, 2, 1, 1)

        self.VolumeText = QLabel(self.layoutWidget2)
        self.VolumeText.setObjectName(u"VolumeText")

        self.gridLayout_2.addWidget(self.VolumeText, 0, 3, 1, 1)

        self.DurationLabel = QLabel(self.layoutWidget2)
        self.DurationLabel.setObjectName(u"DurationLabel")

        self.gridLayout_2.addWidget(self.DurationLabel, 0, 0, 1, 1)

        self.FlowRateLabel = QLabel(self.layoutWidget2)
        self.FlowRateLabel.setObjectName(u"FlowRateLabel")

        self.gridLayout_2.addWidget(self.FlowRateLabel, 1, 0, 1, 1)

        self.FlowRateText = QLabel(self.layoutWidget2)
        self.FlowRateText.setObjectName(u"FlowRateText")

        self.gridLayout_2.addWidget(self.FlowRateText, 1, 1, 1, 1)

        self.UsgLabel = QLabel(self.layoutWidget2)
        self.UsgLabel.setObjectName(u"UsgLabel")

        self.gridLayout_2.addWidget(self.UsgLabel, 1, 2, 1, 1)

        self.UsgText = QLabel(self.layoutWidget2)
        self.UsgText.setObjectName(u"UsgText")

        self.gridLayout_2.addWidget(self.UsgText, 1, 3, 1, 1)

        self.ProgressBarBox = QWidget(self.centralwidget)
        self.ProgressBarBox.setObjectName(u"ProgressBarBox")
        self.ProgressBarBox.setGeometry(QRect(210, 80, 451, 41))
        self.progressBar = QProgressBar(self.ProgressBarBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 10, 431, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RecordButton.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.ProceedButton.setText(QCoreApplication.translate("MainWindow", u"PROCEED", None))
        self.FirstGraph.setText("")
        self.SecondGraph.setText("")
        self.DurationText.setText("")
        self.VolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Voided Volume : ", None))
        self.VolumeText.setText("")
        self.DurationLabel.setText(QCoreApplication.translate("MainWindow", u"Duration :", None))
        self.FlowRateLabel.setText(QCoreApplication.translate("MainWindow", u"Urine Flow Rate : ", None))
        self.FlowRateText.setText("")
        self.UsgLabel.setText(QCoreApplication.translate("MainWindow", u"USG : ", None))
        self.UsgText.setText("")
    # retranslateUi
