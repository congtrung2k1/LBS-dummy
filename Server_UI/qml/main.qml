import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: window
    width: 400
    height: 300
    opacity: 1
    visible: true
    color: "#000000"
    property string property0: "none.none"
    title: qsTr("Server_GUI")


    Rectangle {

        id: svBackground
        color: "#4d78c3"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0

        Text {
            id: text1
            height: 30
            color: "#88ff00"
            text: qsTr("True location")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.bottom
            anchors.bottom: parent.top
            font.pixelSize: 20
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            scale: 1
            anchors.rightMargin: 230
            anchors.bottomMargin: -100
            anchors.topMargin: -250
            font.family: "Arial"
            anchors.leftMargin: 25
        }

        Text {
            id: text2
            x: 25
            height: 30
            color: "#ff0000"
            text: qsTr("Dummy location")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.bottom
            anchors.bottom: parent.top
            font.pixelSize: 20
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 230
            anchors.bottomMargin: -200
            anchors.topMargin: -150
            font.family: "Arial"
            anchors.leftMargin: 25
        }

        TextEdit {
            id: yTrue
            x: 300
            y: 50
            width: 50
            height: 50
            text: qsTr("Y")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        TextEdit {
            id: yDumm
            x: 300
            y: 150
            width: 50
            height: 50
            text: qsTr("Y")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        TextEdit {
            id: xDumm
            x: 206
            y: 150
            width: 50
            height: 50
            text: qsTr("X")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        TextEdit {
            id: xTrue
            x: 206
            y: 50
            width: 50
            height: 50
            text: qsTr("X")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        Button {
            id: showButton
            x: 25
            y: 230
            text: qsTr("SAVED")
            font.pointSize: 16

            Connections {
                target: showButton
                onClicked: core.showMemorized()
            }
        }
    }

    ScrollView {
        id: scrollView
        x: 0
        y: 0
        width: 200
        height: 200
    }

    Connections {
        target: core

        function onGetUpdateResult(res){
            xTrue.text = res.split('-')[0]
            yTrue.text = res.split('-')[1]
            xDumm.text = res.split('-')[2]
            yDumm.text = res.split('-')[3]
        }
    }
}
