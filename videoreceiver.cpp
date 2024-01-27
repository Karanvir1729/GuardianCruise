#include "videoreceiver.h"
#include <QDataStream>
#include <QDebug>

VideoReceiver::VideoReceiver(QObject *parent) : QObject(parent), socket(nullptr), expectedDataSize(0)
{
    socket = new QTcpSocket(this);
    connect(socket, &QTcpSocket::readyRead, this, &VideoReceiver::readData);
}

void VideoReceiver::connectToServer(const QString &serverAddress, quint16 port)
{
    socket->connectToHost(serverAddress, port);
}

void VideoReceiver::disconnectFromServer()
{
    socket->disconnectFromHost();
}

void VideoReceiver::readData()
{
    while (socket->bytesAvailable() > 0)
    {
        if (expectedDataSize == 0)
        {
            if (socket->bytesAvailable() < static_cast<int>(sizeof(quint64)))
            {
                return;
            }

            socket->read(reinterpret_cast<char*>(&expectedDataSize), sizeof(quint64));
        }

        if (socket->bytesAvailable() < expectedDataSize)
        {
            return;
        }

        buffer = socket->read(expectedDataSize);
        QImage frame = byteArrayToImage(buffer);
        emit frameReceived(frame);

        // Clear the buffer as it has already been emitted
        expectedDataSize = 0;
    }
}

QImage VideoReceiver::byteArrayToImage(const QByteArray &data)
{
    QDataStream stream(data);
    QImage image;
    stream >> image;
    return image;
}
