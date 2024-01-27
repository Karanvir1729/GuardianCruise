from elevenlabs import generate, play, save, set_api_key
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play, clone
import dotenv

def create_audio(response, name="Kustav"):
    set_api_key(os.environ["ELEVENKEY"])
    audio = generate(voice = name,
    text= response)
    save(audio, "Response.wav")