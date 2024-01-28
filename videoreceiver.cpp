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

    if (socket->bytesAvailable() < static_cast<int>(sizeof(quint64)))
    {
        qDebug() << "Not enough data for size, waiting for more data";
        return;
    }

    socket->read(reinterpret_cast<char *>(&expectedDataSize), sizeof(quint64));

    if (expectedDataSize <= 0)
    {
        qDebug() << "Invalid data size received: " << expectedDataSize;
        return;
    }

    qDebug() << "Received Data Size: " << expectedDataSize;

    // Wait for the complete data payload
    if (socket->waitForReadyRead(-1))
    {
        buffer = socket->read(expectedDataSize);

        if (buffer.size() != expectedDataSize)
        {
            qDebug() << "Received incomplete data payload. Expected:" << expectedDataSize << ", Received:" << buffer.size();
            return;
        }

        // Print the received raw data in hex and as a string
        qDebug() << "Received Data (Hex):" << buffer.toHex();
        qDebug() << "Received Data (String):" << buffer;

        QImage frame = byteArrayToImage(buffer);

        if (frame.isNull())
        {
            qDebug() << "Error loading image from data.";
            return;
        }

        qInfo() << "Received Frame:" << frame;

        emit frameReceived(frame);

        // Send acknowledgment back to the client (optional)
        socket->write("ACK");

        // Clear the buffer as it has already been emitted
        expectedDataSize = 0;
    }

    else
    {
        qDebug() << "waitForReadyRead timed out or encountered an error.";
    }
}



QImage VideoReceiver::byteArrayToImage(const QByteArray &data)
{
    QDataStream stream(data);
    QImage image;
    stream >> image;

    if (image.isNull())
    {
        qDebug() << "Error loading image from data.";
    }
    return image;
}
