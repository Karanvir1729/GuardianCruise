from elevenlabs import generate, play, save, set_api_key, 
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play, clone
import dotenv
from Cohere_To_Driver import Call_Papa_Cohere
import socket
import pickle
import time
dotenv.load_dotenv()


def create_audio( response, name="Kustav"):
    set_api_key(os.environ["ELEVENKEY"])
    audio = generate(voice = name,
    text= response)
    save(audio, "Response.wav")


def picklein():
    with open('chat_history.pkl', 'rb') as f:  # open a text file
        return pickle.load(f)
def pickleout(data):
    with open('chat_history.pkl', 'wb') as f:  # open a text file
        pickle.dump(data, f) 
def get_message():
    try:
        hist = picklein()
        if type(hist) != type(list()):
            hist=[]
    except:
        hist=[]

    print('Received from server:', "The driver is looking outside the window and is watching birds")
    message = Call_Papa_Cohere("The driver is looking outside the window and is watching birds")
    pickleout(hist)
    create_audio(message)
    return message

