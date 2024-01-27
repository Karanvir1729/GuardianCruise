#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "videoreceiver.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    // Register VideoReceiver as a QML type
    qmlRegisterType<VideoReceiver>("com.video", 1, 0, "VideoReceiver");

    QQmlApplicationEngine engine;

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

    engine.load(url);

    return app.exec();
}
