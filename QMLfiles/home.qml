import QtQuick 2.15
import QtQuick.Controls
import QtQuick.Layouts
import QtMultimedia
import com.video 1.0

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
                   acceptedButtons: Qt.LeftButton
                   cursorShape: Qt.PointingHandCursor

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
                        //loader.push("qrc:/GuardianCruise/QMLfiles/home.qml")
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
                   acceptedButtons: Qt.LeftButton
                   cursorShape: Qt.PointingHandCursor

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
                        loader.push("qrc:/GuardianCruise/QMLfiles/graphs.qml")
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
                   acceptedButtons: Qt.LeftButton
                   cursorShape: Qt.PointingHandCursor

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
                        loader.push("qrc:/GuardianCruise/QMLfiles/crash.qml")
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
           interval: 1
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
           text: " "
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
           text: " "
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


   Rectangle {
       id: cameraNav
       width: 400
       height: 760
       anchors.left: appNav.right
       anchors.leftMargin: 30
       anchors.bottom: parent.bottom
       anchors.bottomMargin: 40
       opacity: 0.1
       radius: 10

       VideoReceiver {
           id: videoReceiver
       }

       // VideoOutput {
       //     id: videopull
       //     width: parent.width
       //     height: parent.height
       //     anchors.horizontalCenter: parent.horizontalCenter
       // }

       Component.onCompleted: {
           // Connect to the server
           videoReceiver.startServer(5560);
       }

       Connections {
           target: videoReceiver
           function onFrameReceived(frame)
           {
               videopull.source = frame;
               console.log("frame receiving");
           }
       }
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
        id: mediaNav1
        width: 450
        height: 140
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        color: "Transparent"
        radius: 10
        clip: true
        AnimatedImage
        {
            id: gifmap
            source: "qrc:/map"
            anchors.fill: parent

        }
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

            // WebView {
            //     id: webView
            //     url: "qrc:/google_maps.html"

            //     BusyIndicator {
            //         id: busy_indicator;
            //         running: false
            //         width:  100;
            //         height: 100;
            //         anchors.centerIn:  parent;
            //         visible: false
            //     }
            // }
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
        id: weatherNav1
        width: 450
        height: 160
        anchors.left: cameraNav.right
        anchors.leftMargin: 30
        anchors.bottom: mapNav.top
        anchors.bottomMargin: 30
        color: "Transparent"
        radius: 10



        Image
        {
            id: albumcover
            source: "qrc:/cover"
            height: 400
            fillMode: Image.PreserveAspectFit
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 30
        }

        Image {
            id: ppb
            source: "qrc:/play"
            height: 50
            fillMode: Image.PreserveAspectFit
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: 30

        }

        MediaPlayer {
            id:music
            audioOutput: AudioOutput {}
            source: "qrc:/music"
            // Component.onCompleted: { play() }
        }

        MouseArea
        {
            id: musicA
            anchors.fill: parent
            propagateComposedEvents: true
            onClicked: {
                console.log("MouseArea clicked");
                if (ppb.source !== "qrc:/play")
                {
                    console.log("Changing source to pause");
                    ppb.source = "qrc:/pause";
                    music.play();
                } if(ppb.source === "qrc:/play")
                {
                    console.log("Changing source to play");
                    ppb.source = "qrc:/pause";

                }
                else
                {
                    console.log("Changing source to play");
                    ppb.source = "qrc:/pause";
                }
            }
        }

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

    Rectangle
    {
        id: conNav1
        width: 400
        height: 760
        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        color: "Transparent"
        radius: 10
        Text {
                id:chatText
                width: parent.width * 0.8
                height: parent.width * 0.7
                text: "" // Initial empty text
                FontLoader {
                    id: medium
                    source: "qrc:/medium"
                }
                color: "White"
                font.family: "medium"
                minimumPixelSize: 40
                verticalAlignment:Text.AlignJustify
                wrapMode: Text.WordWrap
                Connections
                {
                    target: chatReceiver

                }
            }
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
        id: voice1
        width: 350
        height: 50
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.right: pp.left
        anchors.rightMargin: 30
        color: "Transparent"
        radius: 30
        Text {
            id: search
            text: qsTr("Use voice command..")
            color: "White"
            font.family: regular.name
            font.pixelSize: 15
            anchors.left: parent.left
            anchors.leftMargin: 30
            anchors.verticalCenter: parent.verticalCenter
        }
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
            acceptedButtons: Qt.LeftButton
            cursorShape: Qt.PointingHandCursor
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
                loader.push("qrc:/GuardianCruise/QMLfiles/crash.qml")
            }
        }
    }
    Text
    {
        id: accText
        text: qsTr("Accident")
        anchors.centerIn: accident
        color: "White"
        font.family: regular.name
        font.pixelSize: 15
    }
}
