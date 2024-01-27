# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3 
from scipy.io.wavfile import write
import numpy
waveit = False
# Initialize the recognizer 
r = sr.Recognizer() 
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):    
     
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
            audio2 = r.listen(source2)

            if waveit == True:
                with open("my_file2.wav", "wb") as binary_file:
                    binary_file.write(audio2.get_wav_data())
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            SpeakText(MyText)

             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        