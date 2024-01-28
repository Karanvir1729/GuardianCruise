from elevenlabs import generate, play, save, set_api_key
import cohere 
import os
from twilio.rest import Client
from elevenlabs import Voice, VoiceDesign, Gender, Age, Accent, play, clone
import dotenv
from Cohere_To_Driver import Call_Papa_Cohere
import socket
import pickle
dotenv.load_dotenv()

class Ride:
    def __init__(self, name, host, port):
        self.voicename = name
        self.host = host
        self.port = port
    def create_audio(self, response, name="Kustav"):
        set_api_key(os.environ["ELEVENKEY"])
        audio = generate(voice = name,
        text= response)
        save(audio, "Response.wav")

    def picklein(self):
        with open('chat_history.pkl', 'rb') as f:  # open a text file
            return pickle.load(f)
    def pickleout(self, data):
        with open('chat_history.pkl', 'wb') as f:  # open a text file
            return pickle.dump(data, f) 
    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket instantiated')

    # bind the socket
        sock.bind((self.host, self.port))
        print('socket binded')

        # start the socket listening
        while True:
            sock.listen()
            print('socket now listening')

        # accept the socket response from the client, and get the connection object
            conn, addr = sock.accept()
            # Receive the response from the server
            data = conn.recv(1024)
            try:
                hist =self.picklein()
                if type(hist) != type(list()):
                    hist=[]
            except:
                hist=[]

            print('Received from server:', data.decode())
            message, hist = Call_Papa_Cohere(data.decode(), history=hist)
            self.pickleout(hist)
            self.create_audio(message)


if __name__ == "__main__":
    Jeff = Ride("Kustav", "100.65.1.28", 6002)
    Jeff.listen()