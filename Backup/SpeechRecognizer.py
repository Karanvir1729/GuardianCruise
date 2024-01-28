# Python program to translate
# speech to text and text to speech
 
import speech_recognition as sr
import pyttsx3 
from scipy.io.wavfile import write
import numpy
import Socket_Connection
import cohere 
import dotenv
import os
import pickle
from Cohere_To_Driver import Call_Papa_Cohere

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
    #create_audio(message)
    return message

# Initialize the recognizer 

 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak

def listening(r, waveit, co):    
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2, phrase_time_limit=5)
            if waveit == True:
                with open("my_file2.wav", "wb") as binary_file:
                    binary_file.write(audio2.get_wav_data())
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            SpeakText(MyText)
            alcoholtest = co.classify([MyText], "3a06fe6e-32ab-423d-8fb5-5f2e80f470f1-ft")
            print(alcoholtest.classifications[0].prediction)
            
            if alcoholtest.classifications[0].prediction == "Bad":
                MyText = get_message()
                print(MyText)
                Socket_Connection.socket_init(MyText)
                print("This is worlioh")
                return MyText
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        
def main():
    dotenv.load_dotenv()
    waveit = False
    r = sr.Recognizer() 
    co = cohere.Client(os.environ["COHERE_KEY"])
    MyText = listening(r, waveit, co)
    print(MyText)
    return MyText