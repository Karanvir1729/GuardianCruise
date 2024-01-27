#include "videoreceiver.h"
#include <QDataStream>
#include <QDebug>

VideoReceiver::VideoReceiver(QObject *parent) : QObject(parent), server(nullptr), socket(nullptr), expectedDataSize(0)
{
    server = new QTcpServer(this);
    connect(server, &QTcpServer::newConnection, this, &VideoReceiver::newConnection);
}

void VideoReceiver::startServer(quint16 port)
{
    qDebug() << "Starting server on port" << port;
    if (server->listen(QHostAddress::Any, port))
    {
        qDebug() << "Server started";
    }
    else
    {
        qDebug() << "Error starting server:" << server->errorString();
    }
}

void VideoReceiver::stopServer()
{
    qDebug() << "Stopping server";
    server->close();
}

void VideoReceiver::newConnection()
{
    qDebug() << "New connection established";
    socket = server->nextPendingConnection();
    connect(socket, &QTcpSocket::readyRead, this, &VideoReceiver::readData);
}

void VideoReceiver::readData()
{
    qDebug() << "Connected...";
    while (socket->bytesAvailable() > 0)
    {
        if (expectedDataSize == 0)
        {
            if (socket->bytesAvailable() < static_cast<int>(sizeof(quint64)))
            {
                return;
            }

            socket->read(reinterpret_cast<char *>(&expectedDataSize), sizeof(quint64));
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
