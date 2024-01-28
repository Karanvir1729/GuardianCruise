#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "videoreceiver.h"
#include "chatreceiver.h"
#include <qprocess.h>
#include <QCamera>
#include <QPermissions>

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    // Create instances of VideoReceiver and ChatReceiver
    VideoReceiver videoReceiver;
    ChatReceiver chatReceiver;

    // Register VideoReceiver and ChatReceiver as QML types
    qmlRegisterType<VideoReceiver>("com.video", 1, 0, "VideoReceiver");
    qmlRegisterType<ChatReceiver>("com.chat", 1, 0, "ChatReceiver");

    QQmlApplicationEngine engine;

    // Expose instances to QML context
    engine.rootContext()->setContextProperty("videoReceiver", &videoReceiver);
    engine.rootContext()->setContextProperty("chatReceiver", &chatReceiver);

    const QUrl url(QStringLiteral("qrc:/GuardianCruise/main.qml"));
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreated,
        &app,
        [url](QObject *obj, const QUrl &objUrl) {
            if (!obj && url == objUrl)
                QCoreApplication::exit(-1);
        },
        Qt::QueuedConnection);

    chatReceiver.startServer(5570);

    engine.load(url);

    QProcess pythonProcess;
    QString pythonScriptPath = ":/socketsPY/script.py";
    QString datFilePath = ":/socketsPY/shape_predictor_68_face_landmarks.dat";
    pythonProcess.start("python", QStringList() << pythonScriptPath << datFilePath);
    pythonProcess.waitForStarted();

    engine.rootContext()->setContextProperty("pythonProcess", &pythonProcess);

    return app.exec();
}
