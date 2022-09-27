# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'resultsOWXphI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget)


class Ui_Results(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 90, 881, 421))
        self.ResultLayoutBox = QGridLayout(self.gridLayoutWidget)
        self.ResultLayoutBox.setObjectName(u"ResultLayoutBox")
        self.ResultLayoutBox.setContentsMargins(0, 0, 0, 0)
        self.ResultBox = QLabel(self.gridLayoutWidget)
        self.ResultBox.setObjectName(u"ResultBox")
        font = QFont()
        font.setPointSize(12)
        self.ResultBox.setFont(font)
        self.ResultBox.setMargin(15)

        self.ResultLayoutBox.addWidget(self.ResultBox, 0, 1, 1, 1)

        self.ResultImage = QLabel(self.gridLayoutWidget)
        self.ResultImage.setObjectName(u"ResultImage")

        self.ResultLayoutBox.addWidget(self.ResultImage, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 659, 51))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.CloseButton = QPushButton(self.centralwidget)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(300, 550, 321, 51))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.CloseButton.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 22))
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
        self.ResultImage.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"RESULTS/RECOMMENDATIONS", None))
        self.CloseButton.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
    # retranslateUi
