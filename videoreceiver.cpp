#include "videoreceiver.h"

VideoReceiver::VideoReceiver(QObject *parent) : QObject(parent) , socket(nullptr), expectedDatasize(0)
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
    while(socket->bytesAvailable() > 0)
    {
        if(expectedDatasize == 0)
        {
            if(socket->bytesAvailable() < sizeof(quint64))
            {
                return;
            }

            socket->read(reinterpret_cast<char*>(&expectedDatasize), sizeof(quint64));
        }

        if(socket->bytesAvailable() < expectedDatasize)
        {
            return;
        }

        buffer = socket->read(expectedDatasize);
        QImage frame = byteArrayToImage(buffer);
        emit frameReceived(frame);
        //Here we cleared the buffer as we have already emmited it
        expectedDatasize = 0;
        buffer.clear();
    }
}

QImage VideoReceiver::byteArrayToImage(const QByteArray &data)
{
    QDataStream stream(data);
    QImage image;
    stream >> image;
    return image;
}



