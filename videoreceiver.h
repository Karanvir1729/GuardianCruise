#ifndef VIDEORECEIVER_H
#define VIDEORECEIVER_H

#include <QObject>
<<<<<<< HEAD
#include <QTcpServer>
=======
>>>>>>> 42bcbfd (working on some headers, and class methods)
#include <QTcpSocket>
#include <QImage>

class VideoReceiver : public QObject
{
    Q_OBJECT
public:
    explicit VideoReceiver(QObject *parent = nullptr);

signals:
    void frameReceived(const QImage &frame);

public slots:
<<<<<<< HEAD
    void startServer(quint16 port);
    void stopServer();

private slots:
    void newConnection();
    void readData();

private:
    QTcpServer *server;
    QTcpSocket *socket;
    quint64 expectedDataSize;
    QByteArray buffer;

    QImage byteArrayToImage(const QByteArray &data);
=======
    void connectToServer(const QString &serverAddress, quint16 port);
    void disconnectFromServer();

private slots:
    void readData();

private:
    QTcpSocket *socket;
    quint64 expectedDatasize;
    QByteArray buffer;

    QImage byteArrayToImage(const QByteArray &data);

>>>>>>> 42bcbfd (working on some headers, and class methods)
};

#endif // VIDEORECEIVER_H
