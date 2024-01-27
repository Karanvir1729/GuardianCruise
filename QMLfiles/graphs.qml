import QtQuick 2.15
import QtQuick.Controls

Page
{
    background: Rectangle
    {
        id: background
        anchors.fill: parent

        Image
        {
            id: bgSvg
            anchors.fill: parent
            source: "qrc:/bg.svg"
        }
    }


}
