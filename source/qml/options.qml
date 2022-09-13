import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 400
    height: 300
    visible: true
    title: qsTr("JIJ-DIAGNOSTICS")
    flags: Qt.FramelessWindowHint
    opacity: 1.0
    color: "transparent"

    // SET MATERIAL STYLE
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    // create a main column to hold the content
    Column{
        id: mainContent
        visible: true
        anchors.fill: parent
        spacing: 0

        // options for the window (patient or clinician)
        Rectangle {
            id: container_rect
            visible: true
            x: 10
            y: 10
            width: parent.width-20
            height: parent.height-20
            radius: 15
            color: Material.color(Material.Grey, Material.Shade900)

            // add a column
            Column{
                id: main_column
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                anchors.margins: 10
                spacing: 10
                    // BUTTON LOGIN
                    Button{
                        id: patientButton
                        width: 300
                        visible: true
                        text: qsTr("PATIENT")
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: patientClinicianBackend.patientClinician("PATIENT")
                    }

                    // BUTTON LOGIN
                    Button{
                        id: clinicianButton
                        width: 300
                        text: qsTr("CLINICIAN")
                        visible: true
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: patientClinicianBackend.patientClinician("CLINICIAN")
                    }

                    // LOGIN BUTTON LOGIN
                    Button{
                        id: loginButton
                        width: 300
                        visible: false
                        text: qsTr("LOGIN")
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: patientClinicianBackend.loginRegister("LOGIN")
                    }

                    // BUTTON LOGIN
                    Button{
                        id: registerButton
                        width: 300
                        text: qsTr("REGISTER")
                        visible: false
                        anchors.horizontalCenter: parent.horizontalCenter
                        onClicked: patientClinicianBackend.loginRegister("REGISTER")
                    }

            }
        }

        // backend connection
        Connections {
            target: patientClinicianBackend

            // CUSTOM PROPERTIES
            property string patient: "PATIENT"
            property string clinician: "CLINICIAN"
            // login or register
            property string optLoginLogin: "LOGIN"
            property string optLoginRegister: "REGISTER"
            // patient or clinician
            function onSignalPatient(myPatient){ patient = myPatient }
            function onSignalClinician(myClinician){ clinician = myClinician }
            // login or register
            function onSignalLogin(myLogin){ optLoginLogin = myLogin }
            function onSignalRegister(myRegister){ optLoginRegister = myRegister }

            // FUNTION OPEN NEW WINDOW (APP WINDOW)
            function onSignalChoice(boolValue) {
                if(boolValue){
                    // hide the patient and clinician buttons
                    patientButton.visible = false
                    clinicianButton.visible = false
                    // show the login and register button
                    loginButton.visible = true
                    registerButton.visible = true
                } else{
                    // log error
                    console.log("Error: could not open new window")
                }
            }

            // signal for login or register
            function onSignalLoginRegister(boolValue) {
                if(boolValue){
                    var component = Qt.createComponent("login.qml")
                    var win = component.createObject()
                    win.show()
                    visible = false
                } else{
                    var component = Qt.createComponent("register.qml")
                    var win = component.createObject()
                    win.show()
                    visible = false
                }
            }
        }
    }
}
