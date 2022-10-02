# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'resultstyhOca.ui'
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
from PySide2.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QScrollArea, QSizePolicy,
                               QStatusBar, QWidget)


class Ui_Results(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 339)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 341, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 339, 279))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 50, 291, 151))
        self.ResultLayoutBox = QGridLayout(self.gridLayoutWidget)
        self.ResultLayoutBox.setObjectName(u"ResultLayoutBox")
        self.ResultLayoutBox.setContentsMargins(0, 0, 0, 0)
        self.ResultBox = QLabel(self.gridLayoutWidget)
        self.ResultBox.setObjectName(u"ResultBox")
        font = QFont()
        font.setPointSize(12)
        self.ResultBox.setFont(font)

        self.ResultLayoutBox.addWidget(self.ResultBox, 0, 1, 1, 1)

        self.ResultImageBox = QLabel(self.gridLayoutWidget)
        self.ResultImageBox.setObjectName(u"ResultImageBox")

        self.ResultLayoutBox.addWidget(self.ResultImageBox, 0, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 231, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.CloseButton = QPushButton(self.scrollAreaWidgetContents)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(90, 220, 141, 31))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.CloseButton.setFont(font2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ResultBox.setText("")
        self.ResultImageBox.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"RESULTS/RECOMMENDATIONS", None))
        self.CloseButton.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
    # retranslateUi
