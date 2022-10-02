# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'questionsYSoMrL.ui'
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
from PySide2.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
                               QMainWindow, QMenuBar, QPushButton, QScrollArea,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_Questions(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 334)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 291, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 289, 279))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 231, 61))
        self.QuestionOneBox = QGridLayout(self.layoutWidget)
        self.QuestionOneBox.setObjectName(u"QuestionOneBox")
        self.QuestionOneBox.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.QuestionOneHigh = QCheckBox(self.layoutWidget)
        self.QuestionOneHigh.setObjectName(u"QuestionOneHigh")

        self.gridLayout.addWidget(self.QuestionOneHigh, 0, 0, 1, 1)

        self.QuestionOneMedium = QCheckBox(self.layoutWidget)
        self.QuestionOneMedium.setObjectName(u"QuestionOneMedium")

        self.gridLayout.addWidget(self.QuestionOneMedium, 0, 1, 1, 1)

        self.QuestionOneLow = QCheckBox(self.layoutWidget)
        self.QuestionOneLow.setObjectName(u"QuestionOneLow")

        self.gridLayout.addWidget(self.QuestionOneLow, 0, 2, 1, 1)

        self.QuestionOneBox.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.QuestionOne = QLabel(self.layoutWidget)
        self.QuestionOne.setObjectName(u"QuestionOne")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.QuestionOne.setFont(font)

        self.QuestionOneBox.addWidget(self.QuestionOne, 0, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 80, 231, 61))
        self.QuestionTwoBox = QGridLayout(self.layoutWidget1)
        self.QuestionTwoBox.setObjectName(u"QuestionTwoBox")
        self.QuestionTwoBox.setContentsMargins(0, 0, 0, 0)
        self.QuestionTwo = QLabel(self.layoutWidget1)
        self.QuestionTwo.setObjectName(u"QuestionTwo")
        self.QuestionTwo.setFont(font)

        self.QuestionTwoBox.addWidget(self.QuestionTwo, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.QuestionTwoHigh = QCheckBox(self.layoutWidget1)
        self.QuestionTwoHigh.setObjectName(u"QuestionTwoHigh")

        self.gridLayout_2.addWidget(self.QuestionTwoHigh, 0, 0, 1, 1)

        self.QuestionTwoMedium = QCheckBox(self.layoutWidget1)
        self.QuestionTwoMedium.setObjectName(u"QuestionTwoMedium")

        self.gridLayout_2.addWidget(self.QuestionTwoMedium, 0, 1, 1, 1)

        self.QuestionTwoLow = QCheckBox(self.layoutWidget1)
        self.QuestionTwoLow.setObjectName(u"QuestionTwoLow")

        self.gridLayout_2.addWidget(self.QuestionTwoLow, 0, 2, 1, 1)

        self.QuestionTwoBox.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.layoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 150, 231, 61))
        self.QuestionTheeBox = QGridLayout(self.layoutWidget_2)
        self.QuestionTheeBox.setObjectName(u"QuestionTheeBox")
        self.QuestionTheeBox.setContentsMargins(0, 0, 0, 0)
        self.QuestionThree = QLabel(self.layoutWidget_2)
        self.QuestionThree.setObjectName(u"QuestionThree")
        self.QuestionThree.setFont(font)

        self.QuestionTheeBox.addWidget(self.QuestionThree, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.QuestionThreeHigh = QCheckBox(self.layoutWidget_2)
        self.QuestionThreeHigh.setObjectName(u"QuestionThreeHigh")

        self.gridLayout_3.addWidget(self.QuestionThreeHigh, 0, 0, 1, 1)

        self.QuestionThreeMedium = QCheckBox(self.layoutWidget_2)
        self.QuestionThreeMedium.setObjectName(u"QuestionThreeMedium")

        self.gridLayout_3.addWidget(self.QuestionThreeMedium, 0, 1, 1, 1)

        self.QuestionThreeLow = QCheckBox(self.layoutWidget_2)
        self.QuestionThreeLow.setObjectName(u"QuestionThreeLow")

        self.gridLayout_3.addWidget(self.QuestionThreeLow, 0, 2, 1, 1)

        self.QuestionTheeBox.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.SubMitButton = QPushButton(self.scrollAreaWidgetContents)
        self.SubMitButton.setObjectName(u"SubMitButton")
        self.SubMitButton.setGeometry(QRect(80, 230, 121, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.SubMitButton.setFont(font1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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
        self.QuestionOneHigh.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.QuestionOneMedium.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.QuestionOneLow.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.QuestionOne.setText(
            QCoreApplication.translate("MainWindow", u"Did you have any difficulty voiding ?", None))
        self.QuestionTwo.setText(
            QCoreApplication.translate("MainWindow", u"Did you have any difficulty voiding ?", None))
        self.QuestionTwoHigh.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.QuestionTwoMedium.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.QuestionTwoLow.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.QuestionThree.setText(
            QCoreApplication.translate("MainWindow", u"Did you have any difficulty voiding ?", None))
        self.QuestionThreeHigh.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.QuestionThreeMedium.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.QuestionThreeLow.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.SubMitButton.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
    # retranslateUi
