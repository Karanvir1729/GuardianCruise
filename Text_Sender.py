import os
from twilio.rest import Client
import dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Cohere_To_Driver import Call_Papa_Cohere

dotenv.load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

'''message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13343  842504',
                     to='+16139307969'
                 )
'''

#print(message.sid)


app = Flask("__name__")

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    MessagePost = request.values.get("Body", None)

    resp = MessagingResponse()
    hist = Call_Papa_Cohere()[1]
    YoMomsReponse = str(Call_Papa_Cohere(str(MessagePost), scold="False", history=hist)[0])
    # Add a message
    resp.message(YoMomsReponse)

    return str(resp)
app.run()