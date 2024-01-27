#ifndef VIDEORECEIVER_H
#define VIDEORECEIVER_H

#include <QObject>
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
    void connectToServer(const QString &serverAddress, quint16 port);
    void disconnectFromServer();

private slots:
    void readData();

private:
    QTcpSocket *socket;
    quint64 expectedDatasize;
    QByteArray buffer;

    QImage byteArrayToImage(const QByteArray &data);

};

#endif // VIDEORECEIVER_H
