import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

import "../controls"

Item {
    width: 355
    height: 692

    Rectangle {
        id: mainBg
        color: "#151515"
        radius: 10
        border.color: "#00000000"
        border.width: 0
        anchors.fill: parent
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10

        Rectangle {
            id: mainContent
            color: "#00ffffff"
            border.width: 0
            anchors.fill: parent
            property string property0: "none.none"

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

            CustomButton {
                id: runBtn
                x: 93
                y: 350
                width: 149
                height: 40
                text: "Run"
                property string property0: runBtn.property0
                font.family: "Segoe UI"
                font.pointSize: 10
                colorPressed: "#558b1f"
                colorDefault: "#67aa25"
                colorMouseOver: "#7ece2d"
                onClicked: {
                    backend.callMovingLocation()
                    backend.callDummyLocation(1)
                }

            }

            Rectangle {
                id: start
                x: 66
                y: 91
                width: 203
                height: 208
                color: "#00ffffff"

                CustomButton {
                    id: startBtn
                    colorPressed: "#558b1f"
                    font.family: "Segoe UI"
                    colorMouseOver: "#7ece2d"
                    colorDefault: "#67aa25"
                    font.pointSize: 10
                    text: "Start"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 15
                    anchors.bottomMargin: 153
                    anchors.leftMargin: 27
                    anchors.rightMargin: 27
                    onClicked: {
                        backend.callRandLocation()
                        backend.callDummyLocation(0)
                    }
                }

                Rectangle {
                    id: startResultScreen
                    x: -21
                    y: 88
                    width: 245
                    height: 120
                    color: "#282c34"

                    Text {
                        id: randlocation
                        color: "#ffffff"
                        anchors.fill: parent
                        font.pixelSize: 16
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Verdana"
                    }
                }

                Rectangle {
                    id: runScreenResult
                    x: -21
                    y: 345
                    width: 245
                    height: 120
                    color: "#282c34"

                    Text {
                        id: dummylocation
                        color: "#ffffff"
                        anchors.fill: parent
                        font.pixelSize: 16
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.family: "Verdana"
                    }
                }
            }
        }
    }

    Connections {
        target: backend

        function onGetRandLocation(result){
            randlocation.text = result

        }

        function onGetDummyLocation(result){
            dummylocation.text = result
        }

        function onGetMovingLocation(result){
            randlocation.text = result
        }
    }
}

