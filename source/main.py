import sys
import os
import sqlite3

# IMPORT MODULES
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal


# database handler class
class DatabaseHandler(QObject):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    # create table
    def create_table(self):
        # the users should have a unique username, so we use the UNIQUE
        # keyword and a boolean with default as false for clinician
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (fullname TEXT, email TEXT UNIQUE, password TEXT, isClinician BOOLEAN DEFAULT 0)"
        )

    # register user
    def register_user(self, fullname: str, email: str, password: str, isClinician: bool = False):
        try:
            self.cursor.execute(
                "INSERT INTO users (fullname, email, password, isClinician) VALUES (?, ?, ?, ?)",
                (fullname, email, password, isClinician),
            )
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    # login user
    def login_user(self, email: str, password: str):
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()
        return user


# create the options window
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

        # create the database handler
        self.db = DatabaseHandler()  # type: DatabaseHandler
        self.db.create_table()  # create database table
        self.isClinician = False

    # Static Info
    staticPatient = "PATIENT"
    staticClinician = "CLINICIAN"
    patientSignal = Signal(str)
    clinicianSignal = Signal(str)
    signalChoice = Signal(bool)

    # login and register
    staticOptLogin = "LOGIN"
    staticOptRegister = "REGISTER"
    optLoginSignal = Signal(str)
    optRegisterSignal = Signal(str)
    signalLoginRegister = Signal(bool)

    # Static Info
    staticUser = "musah"
    staticPass = "123456"

    # Signals To Send Data
    signalUser = Signal(str)
    signalPass = Signal(str)
    signalLogin = Signal(bool)

    # Signals To Send Data
    signalFullName = Signal(str)
    signalEmail = Signal(str)
    signalPassword = Signal(str)
    signalRegister = Signal(bool)

    # static for record, stop, delete, play
    staticRecord = "RECORD"
    staticStop = "STOP"
    staticDelete = "DELETE"
    staticPlay = "PLAY"

    # signals for record, stop, delete, play
    recordSignal = Signal(str)
    stopSignal = Signal(str)
    deleteSignal = Signal(str)
    playSignal = Signal(str)

    # onSignal for record, stop, delete, play
    signalPlay = Signal(bool)
    signalStop = Signal(bool)
    signalDelete = Signal(bool)
    signalRecord = Signal(bool)

    # function to handle the choice of patient or clinician
    @Slot(str)
    def patientClinician(self, getPatientClinician):
        if self.staticPatient.lower() == getPatientClinician.lower():
            self.isClinician = False
            # send patient signal
            self.patientSignal.emit("Patient")
            # send patient clinician signal
            self.signalChoice.emit(True)
            print(f"Patient passed! {getPatientClinician}, isClinician {self.isClinician}")
        elif self.staticClinician.lower() == getPatientClinician.lower():
            self.isClinician = True
            # send clinician signal
            self.clinicianSignal.emit("Clinician")
            # send patient clinician signal
            self.signalChoice.emit(True)
            print(f"Clinician passed! {getPatientClinician}, isClinician {self.isClinician}")
        else:
            self.onSignalChoice.emit(False)
            print("Patient/Clinician error!")

    # function to handle the choice of login or register
    @Slot(str)
    def loginRegister(self, getLoginRegister):
        if self.staticOptLogin.lower() == getLoginRegister.lower():
            # send login signal
            self.optLoginSignal.emit("Login")
            # send login register signal
            self.signalLoginRegister.emit(True)
            print(f"Login pressed! {getLoginRegister}")
        elif self.staticOptRegister.lower() == getLoginRegister.lower():
            # send register signal
            self.optRegisterSignal.emit("Register")
            # send login register signal
            self.signalLoginRegister.emit(False)
            print(f"Register pressed! {getLoginRegister}")
        else:
            print("Login/Register error!")

    # Function To Check Login
    @Slot(str, str)
    def checkLogin(self, getUser, getPass):
        # if the getUser and getPass are not empty
        if getUser != "" and getPass != "":
            # Send User And Pass
            self.signalUser.emit(getUser)
            self.signalPass.emit(getPass)
            user = self.db.login_user(getUser, getPass)
            print(f"the user is {user}")
            if user is not None:
                if self.isClinician and user[3]:
                    self.signalLogin.emit(True)
                    print("Login successful!")
                else:
                    self.signalLogin.emit(False)
                    print("Login failed!")
        else:
            self.signalLogin.emit(False)
            print("Login error!")

    # Function To Check Register
    @Slot(str, str, str)
    def checkRegister(self, getFullName, getEmail, getPass):
        # add the user to the database if the fields are not empty
        if getFullName != "" and getEmail != "" and getPass != "":
            # make sure email is valid and password is not too short
            if "@" in getEmail and len(getPass) >= 6 and len(getFullName) >= 3:
                # send the data to the database
                self.signalFullName.emit(getFullName)
                self.signalEmail.emit(getEmail)
                self.signalPassword.emit(getPass)
                # register the user in the database
                _isRegister = self.db.register_user(getFullName, getEmail, getPass, self.isClinician)
                if _isRegister:
                    self.signalRegister.emit(True)
                else:
                    self.signalRegister.emit(False)
            else:
                self.signalRegister.emit(False)
                # print(f"Register Successful! {getFullName} {getEmail} {getPass}")
        else:
            print("Register Unsuccessful!")

    # function to handle the record, stop, delete, play
    @Slot(str)
    def recordStopDeletePlay(self, getRecordStopDeletePlay):
        if self.staticRecord.lower() == getRecordStopDeletePlay.lower():
            # send record signal
            self.recordSignal.emit("Record")
            # send record signal
            self.signalRecord.emit(True)
            print(f"Record pressed! {getRecordStopDeletePlay}")
        elif self.staticStop.lower() == getRecordStopDeletePlay.lower():
            # send stop signal
            self.stopSignal.emit("Stop")
            # send stop signal
            self.signalStop.emit(True)
            print(f"Stop pressed! {getRecordStopDeletePlay}")
        elif self.staticDelete.lower() == getRecordStopDeletePlay.lower():
            # send delete signal
            self.deleteSignal.emit("Delete")
            # send delete signal
            self.signalDelete.emit(True)
            print(f"Delete pressed! {getRecordStopDeletePlay}")
        elif self.staticPlay.lower() == getRecordStopDeletePlay.lower():
            # send play signal
            self.playSignal.emit("Play")
            # send play signal
            self.signalPlay.emit(True)
            print(f"Play pressed! {getRecordStopDeletePlay}")
        else:
            print("Record/Stop/Delete/Play error!")


def start_app() -> None:
    # start the application engine
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/logo.png"))
    engine = QQmlApplicationEngine()

    # get context
    main = MainWindow()
    # backend connections to frontend
    engine.rootContext().setContextProperty("patientClinicianBackend", main)
    engine.rootContext().setContextProperty("loginBackend", main)
    engine.rootContext().setContextProperty("registerBackend", main)
    engine.rootContext().setContextProperty("mainBackend", main)

    # load the QML file
    engine.load(os.path.join(os.path.dirname(__file__), "qml/options.qml"))

    # check if the application is running
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())


if __name__ == "__main__":
    start_app()
