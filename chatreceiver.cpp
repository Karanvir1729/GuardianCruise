// chatreceiver.cpp

#include "chatreceiver.h"
#include <QDataStream>
#include <QDebug>

ChatReceiver::ChatReceiver(QObject *parent) : QObject(parent), server(nullptr)
{
    server = new QTcpServer(this);
    connect(server, &QTcpServer::newConnection, this, &ChatReceiver::newConnection);
}

void ChatReceiver::startServer(quint16 port)
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

void ChatReceiver::stopServer()
{
    qDebug() << "Stopping server";
    server->close();
}

void ChatReceiver::newConnection()
{
    qDebug() << "New connection established";
    QTcpSocket *newSocket = server->nextPendingConnection();

    // Check if the socket is not already in the list
    if (!sockets.contains(newSocket))
    {
        connect(newSocket, &QTcpSocket::readyRead, this, &ChatReceiver::readData);
        connect(newSocket, &QTcpSocket::disconnected, this, &ChatReceiver::clientDisconnected);

        sockets.append(newSocket);
    }
    else
    {
        // If the socket is already in the list, close the new connection
        newSocket->close();
        newSocket->deleteLater();
    }
}

void ChatReceiver::readData()
{
    for (QTcpSocket *socket : sockets)
    {
        if (socket->bytesAvailable() > 0)
        {
            QByteArray buffer = socket->readAll();
            QString message = QString::fromUtf8(buffer);  // Decode the received data

            qDebug() << "Received Message from Client:" << message;

            // Emit a signal to pass the received message to QML
            emit messageReceived(message);

            // Send acknowledgment back to the client (optional)
            socket->write("ACK");
        }
    }
}

void ChatReceiver::clientDisconnected()
{
    QTcpSocket *disconnectedSocket = qobject_cast<QTcpSocket*>(sender());
    if (disconnectedSocket)
    {
        qDebug() << "Client disconnected";
        sockets.removeOne(disconnectedSocket);
        disconnectedSocket->deleteLater();
    }
}
