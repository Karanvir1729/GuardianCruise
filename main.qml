import QtQuick
import QtQuick.Controls

Window {
    width: 2560
    height: 1600
    visible: true
    title: qsTr("GuardianCruise")

    StackView
    {
        id: loader
        anchors.fill: parent
        initialItem: "qrc:/GuardianCruise/QMLfiles/home.qml"
    }

}
