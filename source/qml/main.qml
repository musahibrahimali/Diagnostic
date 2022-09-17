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

    Rectangle {
        id: recordStopContent
        visible: false
        x: 10
        y: 10
        width: parent.width-20
        height: parent.height-20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        color: Material.color(Material.Grey, Material.Shade900)

        Column{
            anchors.margins: 10
            visible: true
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            // add a row
            Row {
                    id: recordAndStopRow
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
        }
    }

    // add a column for the questionaire
    Rectangle {
        id: questionaireContainer
        visible: false
        x: 10
        y: 10
        width: parent.width-20
        height: parent.height-20
        color: Material.color(Material.Grey, Material.Shade900)
        // question one
        Column {
            id: questionOne
            anchors.margins: 10
            spacing: 10
            anchors.top: parent.top
            anchors.left: parent.left

            // add a text for the question
            Text {
                id: questionOneQuestion
                text: "Did you have any difficulty while voiding ?"
                color: Material.color(Material.Grey, Material.Shade50)
                font.pixelSize: 20
                font.bold: true
            }

            Row{
                id:questionOneOptions
//                    anchors.margins: 10
                anchors.topMargin: 30
                anchors.rightMargin: 10
                spacing: 10
                anchors.top: parent.top
                anchors.left: parent.left

                //  high checkbox
                CheckBox{
                    id: questionOneHighCheckbox
                    text: qsTr("High")
                    anchors.left: questionOneQuestion.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionOneModerateCheckbox
                    text: qsTr("Moderate")
                    anchors.left: questionOneHighCheckbox.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionOneLowCheckbox
                    text: qsTr("Low")
                    anchors.left: questionOneModerateCheckbox.right
                    anchors.topMargin: 10
                }

            }
        }

        // question two
        Column {
            id: questionTwo
            anchors.margins: 10
            anchors.topMargin: 70
            spacing: 10
            anchors.top: questionOne.bottom
            anchors.left: parent.left

            // add a text for the question
            Text {
                id: questionTwoQuestion
                text: "Did you feel any pain while voiding ?"
                color: Material.color(Material.Grey, Material.Shade50)
                font.pixelSize: 20
                font.bold: true
            }

            Row{
                id:questionTwoOptions
                anchors.topMargin: 30
                anchors.rightMargin: 10
                spacing: 10
                anchors.top: parent.top
                anchors.left: parent.left

                //  high checkbox
                CheckBox{
                    id: questionTwoHighCheckbox
                    text: qsTr("High")
                    anchors.left: questionTwoQuestion.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionTwoModerateCheckbox
                    text: qsTr("Moderate")
                    anchors.left: questionTwoHighCheckbox.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionTwoLowCheckbox
                    text: qsTr("Low")
                    anchors.left: questionTwoModerateCheckbox.right
                    anchors.topMargin: 10
                }

            }
        }

        // question one
        Column {
            id: questionThree
            anchors.margins: 10
            anchors.topMargin: 70
            spacing: 10
            anchors.top: questionTwo.bottom
            anchors.left: parent.left

            // add a text for the question
            Text {
                id: questionThreeQuestion
                text: "Level of urgency ?"
                color: Material.color(Material.Grey, Material.Shade50)
                font.pixelSize: 20
                font.bold: true
            }

            Row{
                id:questionThreeOptions
                anchors.topMargin: 30
                anchors.rightMargin: 10
                spacing: 10
                anchors.top: parent.top
                anchors.left: parent.left

                //  high checkbox
                CheckBox{
                    id: questionThreeHighCheckbox
                    text: qsTr("High")
                    anchors.left: questionThreeQuestion.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionThreeModerateCheckbox
                    text: qsTr("Moderate")
                    anchors.left: questionThreeHighCheckbox.right
                    anchors.topMargin: 10
                }
                //  high checkbox
                CheckBox{
                    id: questionThreeLowCheckbox
                    text: qsTr("Low")
                    anchors.left: questionThreeModerateCheckbox.right
                    anchors.topMargin: 10
                }

            }
        }

    }

    // results column
    Rectangle {
        visible: true
        x: 10
        y: 10
        width: parent.width-20
        height: parent.height-20
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        color: Material.color(Material.Grey, Material.Shade900)
            // a text witht the results
            Column{
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                Text {
                    id: resultsTitle
                    text: "Results"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    color: Material.color(Material.Grey, Material.Shade50)
                    font.pixelSize: 24
                    font.bold: true
                }

                Text {
                    id: resultsText
                    text: "Results"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    color: Material.color(Material.Grey, Material.Shade50)
                    anchors.top: resultsTitle.bottom
                    anchors.topMargin: 20
                    font.pixelSize: 20
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
    }
}
