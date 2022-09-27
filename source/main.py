import sys
import os
import time
from time import sleep
from threading import Thread

import PySide6.QtQuick
# IMPORT MODULES
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal, QThread
from utils import database
from utils import voice_recorder
from tensorflow.keras.models import load_model

duration = 0.0


# create a worker class
class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        self._running = True
        while self._running:
            # do stuff
            time.sleep(1)
            self.progress.emit(1)
        self.finished.emit()

    # terminate the worker
    def terminate(self):
        self._running = False

    # stop the worker
    def stop(self):
        self.terminate()


# create the options window
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

        # create the database handler
        self.db = database.DatabaseHandler()  # type: database.DatabaseHandler
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

    # Signals To log in
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

    # signals for record, stop, delete, play
    recordSignal = Signal(str)
    stopSignal = Signal(str)
    deleteSignal = Signal(str)
    playSignal = Signal(str)

    # onSignal for record, stop, delete, play
    signalRecord = Signal(bool)
    signalStop = Signal(bool)

    # create a worker to record audio
    def record(self):
        self.signalRecord.emit(True)

    def record_audio(self):
        self.duration, self.voided_volume, self.urine_flow_rate, self._usg = voice_recorder.record_audio()
        if os.path.exists("./rec.wav"):
            # replace the duration property of the main.qml file

            self.signalRecord.emit(False)
        return self.duration, self.voided_volume, self.urine_flow_rate, self._usg

    signalProceed = Signal(bool)
    signalSubmit = Signal(bool)

    # function to handle the choice of patient or clinician
    @Slot(str)
    def patientClinician(self, getPatientClinician):
        if self.staticPatient.lower() == getPatientClinician.lower():
            self.isClinician = False
            # send patient signal
            self.patientSignal.emit("Patient")
            # send patient clinician signal
            self.signalChoice.emit(True)
        elif self.staticClinician.lower() == getPatientClinician.lower():
            self.isClinician = True
            # send clinician signal
            self.clinicianSignal.emit("Clinician")
            # send patient clinician signal
            self.signalChoice.emit(True)
        else:
            self.onSignalChoice.emit(False)
            # print("Patient/Clinician error!")

    # function to handle the choice of login or register
    @Slot(str)
    def loginRegister(self, getLoginRegister):
        if self.staticOptLogin.lower() == getLoginRegister.lower():
            # send login signal
            self.optLoginSignal.emit("Login")
            # send login register signal
            self.signalLoginRegister.emit(True)
        elif self.staticOptRegister.lower() == getLoginRegister.lower():
            # send register signal
            self.optRegisterSignal.emit("Register")
            # send login register signal
            self.signalLoginRegister.emit(False)
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
            # print(f"the user is {user}")
            if user is not None:
                self.signalLogin.emit(True)
                # print("Login successful!")
        else:
            self.signalLogin.emit(False)
            # print("Login error!")

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
            pass
            # print("Register Unsuccessful!")

    # function to handle the record, stop, delete, play
    @Slot(str)
    def recordStopDeletePlay(self, getRecordStopDeletePlay):
        if self.staticRecord.lower() == getRecordStopDeletePlay.lower():
            self.recordSignal.emit("Record")
            self.signalRecord.emit(True)
            self.record_audio()
            print(f"Record pressed! {getRecordStopDeletePlay}")
        elif self.staticStop.lower() == getRecordStopDeletePlay.lower():
            # send stop signal
            self.stopSignal.emit("Stop")
            # send stop signal
            self.signalStop.emit(True)
            print(f"Stop pressed! {getRecordStopDeletePlay}")
        else:
            # send stop signal
            self.signalStop.emit(True)
            print("Record/Stop error!")

    # function to handle the proceed button
    @Slot()
    def proceedToQuestions(self):
        # send proceed signal
        self.signalProceed.emit(True)
        print("Proceed pressed!")

    # function to handle the submit button
    @Slot()
    def submitQuestions(self):
        # send submit signal
        self.signalSubmit.emit(True)
        print("Submit pressed!")


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
