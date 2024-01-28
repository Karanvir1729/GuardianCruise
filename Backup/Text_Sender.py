import os
from twilio.rest import Client
import dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Cohere_To_Driver_2 import Call_Papa_Cohere
import socket
import SpeechRecognizer

def my_func():
    global sock, hist
    HOST = '100.65.6.83'
    PORT = 5570
    # instantiate a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket instantiated')

    # bind the socket
    sock.connect((HOST, PORT))
    print('socket binded')

    # start the socket listening
    #sock.listen()
    print('socket now listening')

    # accept the socket response from the client, and get the connection object
    #conn, addr = sock.accept()      # Note: execution waits here until the client calls sock.connect()
    print('socket accepted, got connection object')
    start = 0
    int(start)
    while start!= b"1":
        resp = SpeechRecognizer.main()
        start = sock.recv(1024)
        
    hist = [{"Role":" User", "message": "There is an unfit driver currently driving a vehicle, you are their parent, and are sitting next to them in the passenger seat. Upon receiving a situation, you will provide words of advice and criticism to ensure their safety and well being. Mention fond memories of your time together and be specific and imaginative, while staying in the first person as the driver's parent The situation is as follows:"+"Jeff is currently distracted and is busy looking at birds outside the window"}, {"ROLE": "CHATBOT", "Message":resp}]
    message, hist = Call_Papa_Cohere("The Driver has crashed! Give me a quick explanation of what happened", scold=False, history=hist)
    print('sending: ' + 'Crash info')
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
    global hist, sock
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    MessagePost = request.values.get("Body", None)

    resp = MessagingResponse()

    YoMomsReponse, hist = Call_Papa_Cohere(str(MessagePost), scold="False", history=hist)
    # Add a message
    resp.message(YoMomsReponse)
    sock.sendall(MessagePost.encode())
    sock.sendall(YoMomsReponse.encode())
    return str(resp)
app.run()

