import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: arrowBtn
    property bool isActive: false
    property color colorDefault: "#67aa25"
    property color colorMouseOver: "#7ece2d"
    property color colorPressed: "#558b1f"

    QtObject {
        id: internal

        property var dynamicColor: if(arrowBtn.down){
                                       arrowBtn.down ? colorPressed : colorDefault
                                   }else{
                                       arrowBtn.hovered ? colorMouseOver : colorDefault
                                   }
    }

    implicitWidth: 50
    implicitHeight: 50

    background: Rectangle{
        color: internal.dynamicColor
        radius: 240
        border.width: 0

        Image {
            id: arrowImage
            source: "../../images/svg_images/Arrow - Right.svg"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
