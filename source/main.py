import sys
import os
import time

from main_window import Ui_MainWindow
from questions_ui import Ui_Questions
from results_ui import Ui_Results
from patient_clinician_option import Ui_PatientClinician
from register_ui import Ui_Register
from login_ui import Ui_Login
from login_register_option import Ui_LoginRegister
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from utils import database
from utils import voice_recorder
import PySide6.QtCore as QtCore


class MainWindow(QMainWindow):
    # setup the main window
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isClinician = False
        # resize the window
        self.resize(800, 200)
        self.show()

        # set window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # set thw window style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            #ContentBox {
                color: #ffffff;
            }
        """)

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
        if os.path.exists("./rec.wav"):
            # set the duration text
            self.ui.DurationText.setText(f"{str(self.duration)}")
            # set the voided volume text
            self.ui.VolumeText.setText(f"{str(round(self.urine_flow_rate, 4))}")  # str(self.voided_volume)
            # set the urine flow rate text
            self.ui.FlowRateText.setText(f"{str(round(self.urine_flow_rate, 4))}")
            # set the usg text
            self.ui.UsgText.setText(f"{str(round(self._usg, 4))}")

            # resize the FirstGraph to fit the image
            self.ui.FirstGraph.resize(400, 400)
            self.ui.SecondGraph.resize(400, 400)

            # set the first graph and the last graph
            self.ui.FirstGraph.setPixmap(QPixmap("sound_wave.png"))
            self.ui.SecondGraph.setPixmap(QPixmap("med_filter.png"))
            # resize the image to fit the label
            self.ui.FirstGraph.setScaledContents(True)
            self.ui.SecondGraph.setScaledContents(True)

    # animate the progress bar
    def animate(self):
        # initialize the progress bar value
        self.ui.progressBar.setValue(45)
        self.duration, self.voided_volume, self.urine_flow_rate, self._usg = voice_recorder.record_audio()
        # animate the progress bar while recording
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
            self.resize(1000, 700)

    # stop the recording
    def stop(self):
        # cancel the recording
        self.ui.ContentBox.hide()
        self.ui.ProgressBarBox.hide()
        self.ui.RecordStopBox.show()

    # proceed to the next window
    def proceed(self):
        self.myApp = QuestionsScreen()
        # close the main window
        self.close()
        self.myApp.show()


# create the questions screen
class QuestionsScreen(QMainWindow):
    # setup the questions screen
    def __init__(self):
        super(QuestionsScreen, self).__init__()
        self.ui = Ui_Questions()
        self.ui.setupUi(self)
        # resize the window
        self.resize(700, 450)
        self.show()

        # set window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # set window styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #EEF1FF;
                color: #fff;
            }
            #ResultBox {
                color: #fff;
            }
            # QuestionOneLabel {
                color: #fff;
            }
            # QuestionTwoLabel {
                color: #fff;
            }
            # QuestionThreeLabel {
                color: #fff;
            }
            #QuestionOneHigh {
                color: #fff;
            }
            #QuestionOneMedium {
                color: #fff;
            }
            #QuestionOneLow {
                color: #fff;
            }
            #QuestionTwoHigh {
                color: #fff;
            }
            #QuestionTwoMedium {
                color: #fff;
            }
            #QuestionTwoLow {
                color: #fff;
            }
            #QuestionThreeHigh {
                color: #fff;
            }
            #QuestionThreeMedium {
                color: #fff;
            }
            #QuestionThreeLow {
                color: #fff;
            }
        """)

        # connect the buttons (Questions one)
        self.ui.QuestionOneHigh.stateChanged.connect(self.question_one_high)
        self.ui.QuestionOneLow.stateChanged.connect(self.question_one_medium)
        self.ui.QuestionTwoHigh.stateChanged.connect(self.question_one_low)

        # connect the buttons (Questions two)
        self.ui.QuestionTwoHigh.stateChanged.connect(self.question_two_high)
        self.ui.QuestionTwoMedium.stateChanged.connect(self.question_two_medium)
        self.ui.QuestionTwoLow.stateChanged.connect(self.question_two_low)

        # connect the buttons (Questions three)
        self.ui.QuestionThreeHigh.stateChanged.connect(self.question_three_high)
        self.ui.QuestionThreeMedium.stateChanged.connect(self.question_three_medium)
        self.ui.QuestionThreeLow.stateChanged.connect(self.question_three_low)

        # connect the buttons (submit button)
        self.ui.SubMitButton.clicked.connect(self.submit)

    def question_one_high(self) -> None:
        self.ui.QuestionOneHigh.setChecked(True)
        self.ui.QuestionOneMedium.setChecked(False)
        self.ui.QuestionOneLow.setChecked(False)

    def question_one_medium(self) -> None:
        self.ui.QuestionOneHigh.setChecked(False)
        self.ui.QuestionOneMedium.setChecked(True)
        self.ui.QuestionOneLow.setChecked(False)

    def question_one_low(self) -> None:
        self.ui.QuestionOneHigh.setChecked(False)
        self.ui.QuestionOneMedium.setChecked(False)
        self.ui.QuestionOneLow.setChecked(True)

    def question_two_high(self) -> None:
        self.ui.QuestionTwoHigh.setChecked(True)
        self.ui.QuestionTwoMedium.setChecked(False)
        self.ui.QuestionTwoLow.setChecked(False)

    def question_two_medium(self) -> None:
        self.ui.QuestionTwoHigh.setChecked(False)
        self.ui.QuestionTwoMedium.setChecked(True)
        self.ui.QuestionTwoLow.setChecked(False)

    def question_two_low(self) -> None:
        self.ui.QuestionTwoHigh.setChecked(False)
        self.ui.QuestionTwoMedium.setChecked(False)
        self.ui.QuestionTwoLow.setChecked(True)

    def question_three_high(self) -> None:
        self.ui.QuestionThreeHigh.setChecked(True)
        self.ui.QuestionThreeMedium.setChecked(False)
        self.ui.QuestionThreeLow.setChecked(False)

    def question_three_medium(self) -> None:
        self.ui.QuestionThreeHigh.setChecked(False)
        self.ui.QuestionThreeMedium.setChecked(True)
        self.ui.QuestionThreeLow.setChecked(False)

    def question_three_low(self) -> None:
        self.ui.QuestionThreeHigh.setChecked(False)
        self.ui.QuestionThreeMedium.setChecked(False)
        self.ui.QuestionThreeLow.setChecked(True)

    def submit(self):
        # get the answers from the questions
        self.question_one_high = self.ui.QuestionOneHigh.isChecked()
        self.question_one_medium = self.ui.QuestionOneMedium.isChecked()
        self.question_one_low = self.ui.QuestionOneLow.isChecked()
        self.question_two_high = self.ui.QuestionTwoHigh.isChecked()
        self.question_two_medium = self.ui.QuestionTwoMedium.isChecked()
        self.question_two_low = self.ui.QuestionTwoLow.isChecked()
        self.question_three_high = self.ui.QuestionThreeHigh.isChecked()
        self.question_three_medium = self.ui.QuestionThreeMedium.isChecked()
        self.question_three_low = self.ui.QuestionThreeLow.isChecked()
        self.data = ''
        # if question one is high, two is high and three is high
        if self.question_one_high and self.question_two_high and self.question_three_high:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_high and self.question_three_medium:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_high and self.question_three_low:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_medium and self.question_three_high:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_medium and self.question_three_medium:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_medium and self.question_three_low:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_low and self.question_three_high:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_low and self.question_three_medium:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_high and self.question_two_low and self.question_three_low:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        elif self.question_one_medium and self.question_two_high and self.question_three_high:
            self.data = "Urinary urgency occurs when the pressure in the bladder builds suddenly. You need a doctor’s view on the result to be full diagnosed"
        else:
            self.data = "Some sample data from the database"
        # show the results screen
        self.myApp = ResultsScreen(data=self.data)
        # close the questions screen
        self.close()
        self.myApp.show()


# results screen
class ResultsScreen(QMainWindow):
    # setup the results screen
    def __init__(self, data: str):
        super(ResultsScreen, self).__init__()
        self.ui = Ui_Results()
        self.ui.setupUi(self)
        # resize the window
        # self.resize(700, 450)
        # set the data to the resultbox
        self.ui.ResultBox.setText(data)
        # enable word wrap for ResultBox
        self.ui.ResultBox.setWordWrap(True)
        # add the image to the resultImage label
        self.ui.ResultImage.setPixmap(QPixmap("./images/result_image.jpg"))
        # Allow the image to cover the label
        self.ui.label.setScaledContents(True)
        self.show()

        # set window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # set window styles
        self.setStyleSheet("""
            #centralwidget {
                background-color: #EEF1FF;
                color: #fff;
            }
            #ResultBox {
                color: #212121;
                font-size: 20px;
            }
        """)

        # connect the buttons
        self.ui.CloseButton.clicked.connect(self.home)

    # go to the home screen
    def home(self):
        self.myApp = MainWindow()
        # close the results screen
        self.close()
        self.myApp.show()


# patient or clinician screen
class PatientOrClinicianScreen(QMainWindow):
    # setup the patient or clinician screen
    def __init__(self):
        super(PatientOrClinicianScreen, self).__init__()
        self.ui = Ui_PatientClinician()
        self.ui.setupUi(self)

        # set the window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set the window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # add a border radius to the window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # set window styles
        self.setStyleSheet("""
            QMainWindow {
                background-color:  qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(85, 255, 255, 255)
                );
                color: #fff;
            }
        """)
        # connect the buttons
        self.ui.PatientButton.clicked.connect(self.action)
        self.ui.ClinicianButton.clicked.connect(self.action)

    # go to the patient screen
    def action(self):
        self.myApp = LoginOrRegisterScreen()
        # close the patient or clinician screen
        self.close()
        self.myApp.show()


# login or register screen
class LoginOrRegisterScreen(QMainWindow):
    # setup the login or register screen
    def __init__(self):
        super(LoginOrRegisterScreen, self).__init__()
        self.ui = Ui_LoginRegister()
        self.ui.setupUi(self)
        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # make sure window cannot be resized
        self.setFixedSize(self.size())

        self.setStyleSheet("""
            QMainWindow {
                background-color:  qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop:0 rgba(85, 255, 255, 255), stop:1 rgba(9, 27, 27, 255)
                );
                color: #fff;
            }
        """)

        # connect the buttons
        self.ui.LoginButton.clicked.connect(self.loginOption)
        self.ui.RegisterButton.clicked.connect(self.registerOption)

    # go to the login screen
    def loginOption(self):
        self.myApp = LoginScreen()
        # close the login or register screen
        self.close()
        self.myApp.show()

    # go to the register screen
    def registerOption(self):
        self.myApp = RegisterScreen()
        # close the login or register screen
        self.close()
        self.myApp.show()


# login screen
class LoginScreen(QMainWindow):
    # setup the login screen
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # make sure window cannot be resized
        self.setFixedSize(self.size())
        # set window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        self.ui.label.setPixmap(QPixmap("./images/login_image.jpg"))
        # Allow the image to cover the label
        self.ui.label.setScaledContents(True)
        # set window styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a2127;
                color: #fff;
            }
            #EmailLabel {
                color: #fff;
            }
            #PasswordLabel {
                color: #fff;
            }
        """)

        # connect the buttons
        self.ui.LoginButton.clicked.connect(self.login)
        self.ui.RegisterButton.clicked.connect(self.register)

        # obscure the password
        self.ui.PasswordTextField.setEchoMode(QLineEdit.Password)

    # go to the home screen
    def login(self):
        # get the text of the email and password fields
        self.email = self.ui.EmailTextField.text()
        self.password = self.ui.PasswordTextField.text()
        # create the database handler
        self.db = database.DatabaseHandler()  # type: database.DatabaseHandler
        self.db.create_table()  # create database table
        # check if the email contains @ and .com and if the password is not empty
        if "@" in self.email and ".com" in self.email and self.password != "":
            # check if the email and password are correct
            if self.db.check_login(self.email) is not None:
                # login the user
                user = self.db.login_user(self.email, self.password)
                if user is not None:
                    self.myApp = MainWindow()
                    # close the login screen
                    self.close()
                    self.myApp.show()
            else:
                # change the color of the email and password fields to red
                self.ui.EmailTextField.setStyleSheet("border: 1px solid red;")
                self.ui.PasswordTextField.setStyleSheet("border: 1px solid red;")
        else:
            # change the color of the email and password fields to red
            self.ui.EmailTextField.setStyleSheet("border: 1px solid red;")
            self.ui.PasswordTextField.setStyleSheet("border: 1px solid red;")

    # go to the patient or clinician screen
    def register(self):
        self.myApp = RegisterScreen()
        # close the login screen
        self.close()
        self.myApp.show()


# register screen
class RegisterScreen(QMainWindow):
    # setup the register screen
    def __init__(self):
        super(RegisterScreen, self).__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        # make sure window cannot be resized
        self.setFixedSize(self.size())
        # set thw window title
        self.setWindowTitle("JIJ DIAGNOSTICS")
        # set the window icon
        self.setWindowIcon(QIcon("./images/logo.png"))

        # set window styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a2127;
                color: #fff;
            }
            #NameLabel {
                color: #fff;
            }
            #EmailLabel {
                color: #fff;
            }
            #PasswordLabel {
                color: #fff;
            }
        """)

        # connect the buttons
        self.ui.RegisterButton.clicked.connect(self.register)
        self.ui.LoginButton.clicked.connect(self.login)

        # obscure the password field
        self.ui.PasswordTextField.setEchoMode(QLineEdit.Password)

    # go to the home screen
    def register(self):
        # get the name, email and password fields
        self.name = self.ui.NameTextField.text()
        self.email = self.ui.EmailTextField.text()
        self.password = self.ui.PasswordTextField.text()
        # check if the user exist already
        # create the database handler
        self.db = database.DatabaseHandler()  # type: database.DatabaseHandler
        self.db.create_table()  # create database table
        # print(f" name : {self.name}, Email: {self.email}, Password : {self.password}")
        if self.name != "" and "@" in self.email and ".com" in self.email and self.password != "" and self.db.check_login(
                self.email) is None:
            # register the user
            user = self.db.register_user(self.name, self.email, self.password)
            if user:
                self.myApp = MainWindow()
                # close the register screen
                self.close()
                self.myApp.show()
            else:
                # change the color of the email and password fields to red
                self.ui.NameTextField.setStyleSheet("border: 1px solid red;")
                self.ui.EmailTextField.setStyleSheet("border: 1px solid red;")
                self.ui.PasswordTextField.setStyleSheet("border: 1px solid red;")
        else:
            # change the color of the email and password fields to red
            self.ui.NameTextField.setStyleSheet("border: 1px solid red;")
            self.ui.EmailTextField.setStyleSheet("border: 1px solid red;")
            self.ui.PasswordTextField.setStyleSheet("border: 1px solid red;")

    # go to the patient or clinician screen
    def login(self):
        self.myApp = LoginScreen()
        # close the register screen
        self.close()
        self.myApp.show()


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
                        border-radius: 10px;
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

            self.myApp = PatientOrClinicianScreen()
            self.myApp.show()

        self.counter += 1


if __name__ == "__main__":

    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        pass
