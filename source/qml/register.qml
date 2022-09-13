import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 400
    height: 600
    visible: true
    title: qsTr("Register Page")

    // SET FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint

    // SET MATERIAL STYLE
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    // CREATE TOP BAR
    Rectangle{
        id: topBar
        height: 40
        color: Material.color(Material.Blue)
        anchors{
            left: parent.left
            right: parent.right
            top: parent.top
            margins: 10
        }
        radius: 10

        Text{
            text: qsTr("LOGIN PAGE")
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            color: "#ffffff"
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 10
        }
    }

    // IMAGE IMPORT
    Image{
        id: image
        width: 300
        height: 120
        source: "../images/logo.png"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.topMargin: 60
    }

    // TEXT FIELD USERNAME
    TextField{
        id: fullNameField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("John Doe")
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: image.bottom
        anchors.topMargin: 60
    }

    // TEXT FIELD USERNAME
    TextField{
        id: usernameField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("johndoe@email.com")
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: fullNameField.bottom
        anchors.topMargin: 10
    }

    // TEXT FIELD USERNAME
    TextField{
        id: passwordField
        width: 300
        text: qsTr("")
        selectByMouse: true
        placeholderText: qsTr("***************")
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: usernameField.bottom
        anchors.topMargin: 10
        echoMode: TextInput.Password
    }

    // CHECKBOX SAVE PASS
    CheckBox{
        id: checkBox
        text: qsTr("Save password")
        anchors.top: passwordField.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter

    }

    // BUTTON LOGIN
    Button{
        id: buttonLogin
        width: 300
        text: qsTr("Register")
        anchors.top: checkBox.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: registerBackend.checkRegister(fullNameField.text, usernameField.text, passwordField.text)
    }

    // add a text box to display the result
    Text {
        id: result
        visible: false
        anchors.top: buttonLogin.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        text: qsTr("An error occured")
    }


    Connections {
        target: registerBackend

        // CUSTOM PROPERTIES
        property string fullname: ""
        property string username: ""
        property string password: ""
        function onSignalFullName(myFullName){ fullname = myFullName }
        function onSignalUser(myUser){ username = myUser }
        function onSignalPass(myPass){ password = myPass }

        // FUNTION OPEN NEW WINDOW (APP WINDOW)
        function onSignalRegister(boolValue) {
            if(boolValue){
                var component = Qt.createComponent("main.qml")
                var win = component.createObject()
                win.show()
                visible = false
            } else{
                result.visible = true
                // make the result text pink
                result.color = "#ff0000"
                // CHANGE USER COLOR
                fullNameField.Material.foreground = Material.Pink
                fullNameField.Material.accent = Material.Pink
                usernameField.Material.foreground = Material.Pink
                usernameField.Material.accent = Material.Pink
                passwordField.Material.foreground = Material.Pink
                passwordField.Material.accent = Material.Pink
            }
        }
    }
}
