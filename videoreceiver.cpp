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


