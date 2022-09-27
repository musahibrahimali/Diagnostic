import sys
import os
import time

from main_window import Ui_MainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    # setup the main window
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # resize the window
        self.resize(800, 200)
        self.show()

        # set window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # hide the progress bar box and the content box and its content
        self.ui.ProgressBarBox.hide()
        self.ui.ContentBox.hide()

        # connect the buttons
        self.ui.RecordButton.clicked.connect(self.record)
        self.ui.StopButton.clicked.connect(self.stop)
        self.ui.ProceedButton.clicked.connect(self.proceed)

    # record the audio
    def record(self):
        # show the progress bar box
        self.ui.ProgressBarBox.show()
        self.ui.progressBar.setValue(0)
        # animate the progress bar
        self.animate()

    # animate the progress bar
    def animate(self):
        # initialize the progress bar value
        self.ui.progressBar.setValue(0)
        # increase the progress bar value with time
        while self.ui.progressBar.value() < 100:
            time.sleep(0.1)
            self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
        if self.ui.progressBar.value() == 100:
            # hide the progress bar box
            self.ui.ProgressBarBox.hide()
            self.ui.RecordStopBox.hide()
            # show the content box and its content
            self.ui.ContentBox.show()
            # resize the window
            self.resize(800, 650)

    # stop the recording
    def stop(self):
        pass

    # proceed to the next window
    def proceed(self):
        pass


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')
        self.setFixedSize(500, 250)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300  # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # set the style sheet
        self.setStyleSheet('''
                    #LabelTitle {
                        font-size: 60px;
                        color:#55ffff;
                    }

                    #LabelDesc {
                        font-size: 30px;
                        color: #c2ced1;
                    }

                    #LabelLoading {
                        font-size: 30px;
                        color: #e8e8eb;
                    }

                    QFrame {
                        background-color: #1a2127;
                        color: rgb(220, 220, 220);
                    }

                    QProgressBar {
                        background-color: #1a2127;
                        border:  rgb(41, 52, 61);
                        color:  #fff;
                        border-radius: 5px;
                        text-align: center;
                        text-align: center;
                        font-size: 30px;                
                    }

                    QProgressBar::chunk {
                        background-color:  qlineargradient(
                            spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(85, 255, 255, 255)
                        );
                        color: #fff;
                        border-radius: 5px;
                    }
                ''')

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        # center labels
        self.labelTitle.resize(self.width() - 10, 100)
        self.labelTitle.move(0, 10)  # x, y
        self.labelTitle.setText('Welcome')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 100, 30)
        self.progressBar.move(40, self.labelDescription.y() + 40)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(30)

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            self.myApp = MainWindow()
            self.myApp.show()

        self.counter += 1


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #         #LabelTitle {
    #             font-size: 60px;
    #             color:#55ffff;
    #         }
    #
    #         #LabelDesc {
    #             font-size: 30px;
    #             color: #c2ced1;
    #         }
    #
    #         #LabelLoading {
    #             font-size: 30px;
    #             color: #e8e8eb;
    #         }
    #
    #         QFrame {
    #             background-color: #1a2127;
    #             color: rgb(220, 220, 220);
    #         }
    #
    #         QProgressBar {
    #             background-color: #1a2127;
    #             border:  rgb(41, 52, 61);
    #             color:  #fff;
    #             border-radius: 5px;
    #             text-align: center;
    #             text-align: center;
    #             font-size: 30px;
    #         }
    #
    #         QProgressBar::chunk {
    #             background-color:  qlineargradient(
    #                 spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(85, 255, 255, 255)
    #             );
    #             color: #fff;
    #             border-radius: 5px;
    #         }
    #     ''')

    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        pass
