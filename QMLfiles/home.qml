import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Layouts

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

   Rectangle
   {
       id: appNav

       width: 100
       height: 840
       color: "White"
       opacity: 0.1
       radius: 10

       anchors.verticalCenter: parent.verticalCenter
       anchors.left: parent.left
       anchors.leftMargin: 40

   }

   Rectangle
   {
       id: cameraNav

       width: 400
       height: 710
       anchors.left: appNav.right
       anchors.leftMargin: 30
       anchors.bottom: parent.bottom
       anchors.bottomMargin: 40
       opacity: 0.1
       radius: 10
   }

    Rectangle
    {
        id: mediaNav
        width: 450
        height: 140
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        opacity: 0.1
        radius: 10
    }

    Rectangle
    {
        id: sideCamNav
        width: 450
        height: 400
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: mediaNav.top
        anchors.bottomMargin: 30
        opacity: 0.1
        radius: 10
    }

    Rectangle
    {
        id: weatherNav
        width: 450
        height: 110
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: sideCamNav.top
        anchors.bottomMargin: 30
        opacity: 0.1
        radius: 10
    }

    Rectangle
    {
        id: conNav

        width: 400
        height: 710
        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        opacity: 0.1
        radius: 10
    }

}
