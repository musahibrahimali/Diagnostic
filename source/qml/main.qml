import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 760
    height: 500
    visible: true
    title: qsTr("JIJ DIAGNOSTIC")

    // SET MATERIAL STYLE
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    // add a column
    Column {
        anchors.fill: parent
        anchors.margins: 10
        // center the content
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        // add a progress indicator
        ProgressIndicator {
            id: progressIndicator
            running: true
            visible: true
            width: 150
            height: 50
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }

        // add a row
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            spacing: 10
            // add a button
            Button {
                text: "Record"
                onClicked: console.log("Button 1 clicked")
            }
            // add a button
            Button {
                text: "Stop"
                onClicked: console.log("Button 2 clicked")
            }
        }
    }
}
