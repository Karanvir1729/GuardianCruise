// chatreceiver.h
#pragma once

#include <QObject>
#include <QTcpServer>
#include <QTcpSocket>

class ChatReceiver : public QObject
{
    Q_OBJECT

public:
    explicit ChatReceiver(QObject *parent = nullptr);

signals:
    void messageReceived(const QString &message);

public slots:
    void startServer(quint16 port);
    void stopServer();
    void sendButtonClickedMessage();

private slots:
    void newConnection();
    void readData();
    void clientDisconnected();

private:
    QTcpServer *server;
    QList<QTcpSocket*> sockets;
};
