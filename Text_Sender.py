import os
from twilio.rest import Client
import dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Cohere_To_Driver import Call_Papa_Cohere
import socket
def my_func():
    global conn, hist
    HOST = "100.65.1.28"
    PORT = 65432
    global hist
    # instantiate a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket instantiated')

    # bind the socket
    sock.bind((HOST, PORT))
    print('socket binded')

    # start the socket listening
    sock.listen()
    print('socket now listening')

    # accept the socket response from the client, and get the connection object
    conn, addr = sock.accept()      # Note: execution waits here until the client calls sock.connect()
    print('socket accepted, got connection object')
    start = conn.recv(1024)
    while start!=b'1':
        start = conn.recv(1024)

    message, hist = Call_Papa_Cohere()
    message, hist = Call_Papa_Cohere("Jeff has crashed! Give me a quick explanation of what happened", scold=False, history=hist)
    print('sending: ' + 'Crash info')
    conn.sendall(message.encode())
    message = client.messages \
                .create(
                     body=str(message),
                     from_='+13343842504',
                     to='+16139307969')


dotenv.load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



my_func()
app = Flask("__name__")



@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global hist, conn
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    MessagePost = request.values.get("Body", None)

    resp = MessagingResponse()

    YoMomsReponse = Call_Papa_Cohere(str(MessagePost), scold="False", history=hist)[0]
    # Add a message
    resp.message(YoMomsReponse)
    conn.sendall(MessagePost.encode())
    conn.sendall(YoMomsReponse.encode())
    return str(resp)
app.run()

