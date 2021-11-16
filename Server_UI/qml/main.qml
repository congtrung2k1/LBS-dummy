import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import "controls"

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
        color: "#fff8a5"
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
            color: "#00ff00"
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

        ShowButton {
            anchors.right: parent.left
            anchors.top: parent.bottom
            anchors.rightMargin: -85
            anchors.topMargin: -50

        }

        Text {
            id: xTrue
            height: 30
            color: "#000000"
            text: qsTr("X")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            styleColor: "#000000"
            font.bold: true
            anchors.bottomMargin: 200
            anchors.topMargin: 50
            anchors.rightMargin: 150
            font.family: "Arial"
            anchors.leftMargin: 200

        }

        Text {
            id: yTrue
            height: 30
            color: "#000000"
            text: qsTr("Y")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.topMargin: 50
            anchors.bottomMargin: 200
            anchors.rightMargin: 50
            font.family: "Arial"
            anchors.leftMargin: 300
            font.bold: true
        }

        Text {
            id: xFake
            height: 30
            color: "#000000"
            text: qsTr("X")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.topMargin: 150
            anchors.bottomMargin: 100
            anchors.rightMargin: 150
            font.family: "Arial"
            anchors.leftMargin: 200
            font.bold: true
        }

        Text {
            id: yFake
            height: 30
            color: "#000000"
            text: qsTr("Y")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.bottomMargin: 100
            anchors.topMargin: 150
            anchors.rightMargin: 50
            font.family: "Arial"
            font.bold: true
            anchors.leftMargin: 300
        }

    }

    ScrollView {
        id: scrollView
        x: 0
        y: 0
        width: 200
        height: 200
    }
}
