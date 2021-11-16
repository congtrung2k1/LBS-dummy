import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{

    id: showBtn
    height: 30
    text: "Show"
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    anchors.rightMargin: 300
    anchors.leftMargin: 25
    anchors.bottomMargin: 15
    anchors.topMargin: 250

    font.pointSize: 12
    font.family: "Arial"

    background: Rectangle{
        color: '#ffaaff'
    }

    Connections{
        target: showBtn
        onClicked:{
            print('Show the list of locations')
        }
    }

}
