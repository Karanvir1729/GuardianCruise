import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Layouts
import QtWebEngine
import QtLocation
import QtPositioning 6.6
import QtQml.Models
import QtWebView

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
       id: appNavList

       width: 100
       height: 840
       color: "Transparent"
       radius: 10

       anchors.verticalCenter: parent.verticalCenter
       anchors.left: parent.left
       anchors.leftMargin: 40

       Image {
           id: logo
           source: "qrc:/logo"
           width: 50
           height: 50
           anchors.top: parent.top
           anchors.topMargin: 30
           anchors.horizontalCenter: parent.horizontalCenter
       }

       ColumnLayout
       {
           id: navigation
           anchors.horizontalCenter: parent.horizontalCenter
           anchors.top: logo.bottom
           anchors.topMargin: 275
           spacing: 60

           Image
           {
               id: apps
               source: "qrc:/app"
               sourceSize.width: 30
               sourceSize.height: 30

               MouseArea
               {
                   id:appA
                   anchors.fill: parent
                   hoverEnabled: true
                   propagateComposedEvents: true

                   onEntered:
                   {
                       apps.opacity = 0.5;
                   }

                   onExited:
                   {
                       apps.opacity = 1;
                   }

                   onClicked:
                   {

                   }
               }

           }

           Image
           {
               id: graphs
               source: "qrc:/graph"
               sourceSize.width: 32
               sourceSize.height: 32

               MouseArea
               {
                   id:graphA
                   anchors.fill: parent
                   hoverEnabled: true
                   propagateComposedEvents: true

                   onEntered:
                   {
                       graphs.opacity = 0.5;
                   }

                   onExited:
                   {
                       graphs.opacity = 1;
                   }

                   onClicked:
                   {

                   }
               }

           }


           Image {
               id: crash
               source: "qrc:/crash"
               sourceSize.width: 35
               sourceSize.height: 35

               MouseArea
               {
                   id:crashA
                   anchors.fill: parent
                   hoverEnabled: true
                   propagateComposedEvents: true

                   onEntered:
                   {
                       crash.opacity = 0.5;
                   }

                   onExited:
                   {
                       crash.opacity = 1;
                   }

                   onClicked:
                   {

                   }
               }

           }
       }

   }

   ColumnLayout {
       id: dateandtime
       anchors.left: appNav.right
       anchors.leftMargin: 30
       anchors.bottom: cameraNav.top
       anchors.bottomMargin: 30

       Timer {
           id: timer
           interval: 1000 // Update every 1000 milliseconds (1 second)
           running: true
           repeat: true

           onTriggered: {
               updateDateTime();
               updateDay();
           }
       }

       Text {
           id: timeText

           font.family: black.name
           color: "White"
           font.pixelSize: 30
       }
       FontLoader {
           id: black
           source: "qrc:/black"
       }

       Text {
           id: dayText
           FontLoader {
               id: regular
               source: "qrc:/regular"
           }
           font.family: regular.name
           color: "White"
           font.pixelSize: 20
       }

   }

   function updateDateTime() {
       var currentDate = new Date();
       timeText.text = Qt.formatDateTime(currentDate, "h:mm:ss ap");
   }

   function updateDay() {
       var currentDate = new Date();
       dayText.text = Qt.formatDateTime(currentDate, "dddd | d MMMM yyyy");
   }


   Rectangle
   {
       id: cameraNav

       width: 400
       height: 760
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
        id: mapNav
        width: 450
        height: 400
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: mediaNav.top
        anchors.bottomMargin: 30
        opacity: 0.1
        radius: 10

            WebView {
                id: webView
                url: "qrc:/google_maps.html"

                BusyIndicator {
                    id: busy_indicator;
                    running: false
                    width:  100;
                    height: 100;
                    anchors.centerIn:  parent;
                    visible: false
                }
            }
    }

    Rectangle
    {
        id: weatherNav
        width: 450
        height: 160
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: mapNav.top
        anchors.bottomMargin: 30
        opacity: 0.1
        radius: 10
    }

    Rectangle
    {
        id: conNav

        width: 400
        height: 760
        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        opacity: 0.1
        radius: 10
    }

    Image {
        id: pp
        source: "qrc:/pp"
        width: 60
        height: 60

        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.top: parent.top
        anchors.topMargin: 30
    }

    Rectangle
    {
        id: voice
        width: 350
        height: 50
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.right: pp.left
        anchors.rightMargin: 30

        opacity: 0.1
        radius: 30
    }

    Rectangle
    {
        id: accident
        width: 100
        height: 50
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.right: voice.left
        anchors.rightMargin: 30

        opacity: 0.1
        radius: 30

        MouseArea
        {
            id: accArea1
            anchors.fill: parent
            hoverEnabled: true
            propagateComposedEvents: true
            onEntered:
            {
                accident.color = "White"
                accident.opacity = 0.7
                accText.color = "#00347f"
            }

            onExited:
            {
                accident.color = "White"
                accident.opacity = 0.1
                accText.color = "White"
            }

            onClicked:
            {

            }
        }
    }

    Text {
        id: accText
        text: qsTr("Accident")
        anchors.centerIn: accident
        color: "White"
        font.family: regular.name
        font.pixelSize: 15
    }

}
