from elevenlabs import generate, play, save, set_api_key
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play, clone
import dotenv
dotenv.load_dotenv()
set_api_key(os.environ["ELEVENKEY"])
def create_audio(response):
    audio = generate(voice = 'Lexa',
    text= response)
    save(audio, "Oldlady2.wav")



audio = generate(text="Hello, I code in C plus plus", voice="Kustav")


save(audio, "Kustavyya")