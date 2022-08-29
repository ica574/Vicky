# Name: Main.py
# Author: Isaac Cilia Attard
# Data: 26/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
from NLP import SystemInfo
from NLP.Classifier import classify

def textToSpeech(text):
    engine.say(text)
    engine.runAndWait()

# Initialisation
engine = pyttsx3.init() # Text to speech

model = Model("model") # Utilises VOSK model for speech recognition
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio() # Audio input stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

stream.start_stream() # Instantiates microphone datastream

print("Running...")

while True: # Speech recognition

    data = stream.read(4000, exception_on_overflow=False) # Read datastream from microphone

    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):

        result = rec.Result()            
        result = json.loads(result)
        text = result['text']

        print(text)

        if text == "vicky": # Wake word detection
            pauseCounter = 0
            print("Listening...")
            textToSpeech("Listening...")
            while pauseCounter < 1:
                data = stream.read(4000, exception_on_overflow=False) # Read datastream from microphone
                if rec.AcceptWaveform(data):
                    result = rec.Result()            
                    result = json.loads(result)
                    text = result['text']
                    if text == "":
                        pauseCounter += 1
                    else:
                        pauseCounter = 1
                        entity = classify(text) # Classifies recognised text after wake word invocation