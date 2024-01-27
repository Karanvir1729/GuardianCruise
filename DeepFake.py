from elevenlabs import generate, play, save, set_api_key
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play
import dotenv

dotenv.load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

Name = "Jeff"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"{Name} has crashed their car. This is a message informing you of their crash location, to access further info, check yo dashboard",
                     from_='+13343842504',
                     to='+16139307969'
                 )
print(message.sid)

co = cohere.Client("GlsAPCOHHmmZZ46Kd0ivOlEsxJMDRXZNpqi9G6hW")
set_api_key("1bd01d835b2876b35376769cfe4514b8")



PromptSit = "Jeff is currently distracted and is busy looking at birds outside the window"
status = "distracted"
response = co.chat(message=PromptSit, conversation_id="1", preamble_override=f"There is a {status} driver currently driving a vehicle, you are their parent, and are about to scold them and advize them on what to do about it, in under 40 words. Be strict. The current situation is about to be given to you, respond appropiately", max_tokens=200, temperature=0.7)
print(response.text)

audio = generate(voice = 'Lexa',
    text= response.text)
save(audio, "Oldlady2.wav")
