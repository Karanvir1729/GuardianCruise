#ifndef VIDEORECEIVER_H
#define VIDEORECEIVER_H

#include <QObject>
#include <QTcpServer>
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
};

#endif // VIDEORECEIVER_H
