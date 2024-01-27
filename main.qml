import QtQuick

Window {
    width: 2560
    height: 1600
    visible: true
    title: qsTr("GuardianCruise")



    Rectangle {
        id: background
        anchors.fill: parent

        Image {
            id: bgSvg
            source: "qrc:/bg.svg"
        }
    }
}
