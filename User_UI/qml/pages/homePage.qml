import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import "../controls"

Window {
    id: user_UI
    width: 375
    height: 712
    visible: true
    color: "#00000000"
    title: "Project"

    //Remove title bar
    flags: Qt.Window | Qt.FramelessWindowHint


    //

    Rectangle {
        id: background
        color: "#151515"
        radius: 10
        border.color: "#00000000"
        anchors.fill: parent
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10

        DragHandler {
            onActiveChanged: if(active) {
                             user_UI.startSystemMove()
                             }
        }

        Rectangle {
            id: content
            color: "#00000000"
            radius: 10
            border.color: "#00000000"
            border.width: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            anchors.rightMargin: 0
            anchors.leftMargin: 0

            ArrowButton {
                id: arrowBtn
                x: 273
                y: 552
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 90
                anchors.rightMargin: 32
                onClicked: {
                    stackView.push(Qt.resolvedUrl("main.qml"))
                }



            }

            Image {
                id: image
                x: 62
                y: 234
                width: 231
                height: 224
                anchors.verticalCenter: parent.verticalCenter
                source: "../../images/Logo_IU.png"
                anchors.horizontalCenter: parent.horizontalCenter
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: label
                color: "#ffffff"
                text: qsTr("GROUP 7")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 173
                anchors.leftMargin: 46
                anchors.bottomMargin: 557
                anchors.topMargin: 96
                font.family: "Popins"
                font.bold: true
                font.pointSize: 22
            }

            Label {
                id: label1
                x: 46
                y: 148
                color: "#ffffff"
                text: qsTr("Lab Project Presentation")
                font.family: "Popins"
                font.pointSize: 12
            }

            CustomButton {
                id: btnClose
                x: 20
                width: 30
                height: 30
                opacity: 1
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.topMargin: 15
                anchors.rightMargin: 15
                colorPressed: "#558b1f"
                font.family: "Segoe UI"
                colorMouseOver: "#7ece2d"
                colorDefault: "#67aa25"
                font.pointSize: 10
                text: "X"
                onClicked: user_UI.close()


            }

            StackView {
                id: stackView
                x: 0
                y: 0
                width: 355
                height: 692

            }
        }
    }
}


/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}
}
##^##*/
