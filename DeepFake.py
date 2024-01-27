from elevenlabs import generate, play, save, set_api_key
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play
def create_audio(response):
    set_api_key("1bd01d835b2876b35376769cfe4514b8")
    audio = generate(voice = 'Lexa',
        text= response)
    save(audio, "Oldlady2.wav")

'''voice = clone(
    name="Alex",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
    files=["./sample_0.mp3", "./sample_1.mp3", "./sample_2.mp3"],
)

audio = generate(text="Hi! I'm a cloned voice!", voice=voice)

play(audio)'''
