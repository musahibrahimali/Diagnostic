import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window
    width: 550
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

        // add a row
        Row {
            id: playAndStopRow
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            spacing: 10
            // add a button
            Button {
                text: "Record"
                width: 150
                onClicked: mainBackend.recordStopDeletePlay("RECORD")
            }
            // add a button
            Button {
                text: "Stop"
                width: 150
                onClicked: mainBackend.recordStopDeletePlay("STOP")
            }
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            anchors.margins: 10
            anchors.top: playAndStopRow.bottom
            spacing: 10
            // add a button
            Button {
                text: "Play"
                width: 150
                onClicked: mainBackend.recordStopDeletePlay("PLAY")
            }
            // add a button
            Button {
                text: "Delete"
                width: 150
                onClicked: mainBackend.recordStopDeletePlay("DELETE")
            }
        }

    }

    Connections {
        target: mainBackend

        // FUNTION OPEN NEW WINDOW (APP WINDOW)
        function onSignalRecord(boolValue) {

        }

        function onSignalStop(boolValue) {

        }

        function onSignalPlay(boolValue) {

        }

        function onSignalDelete(boolValue) {

        }
    }
}
