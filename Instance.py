# Name: instance.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Forms the fundamental properties of a Vicky instance.

import pyttsx3
import json
from vosk import Model, KaldiRecognizer
import pyaudio
from nlu.classifier import classify

class Core(): # Defines core functions of the AI
    __skills = [] # Contains a list of skills that the assistant has at its disposal

    def __init__(self): # Constructor - initialises engines and neural networks for AI
        self.speech_engine = pyttsx3.init() # Speech synthesis engine
        self.vosk_model = Model("model")
        self.recogniser = KaldiRecognizer(self.vosk_model, 16000) # VOSK speech recognition model
        self.audio_input = pyaudio.PyAudio() # Microphone input
        self.input_stream = self.audio_input.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000) # Input stream
    
    def text_to_speech(self, text): # Utiilises speech synthesis engine
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listen_for_wakeword(self): # Listens for wakeword
        while True:
            data = self.input_stream.read(4000, exception_on_overflow=False) # Reads datastream from microphone

            if self.recogniser.AcceptWaveform(data):

                result = self.recogniser.Result()            
                result = json.loads(result)
                text = result['text']

                print(text)

                if text == "vicky": # Wake word detection
                    print("Listening...")
                    self.text_to_speech("Listening...")
                    return True

    def listen_for_commands(self): # Listens for commands and classifies them
        while True:
            data = self.input_stream.read(4000, exception_on_overflow=False) # Read datastream from microphone
            text = ""
            if self.recogniser.AcceptWaveform(data):
                result = self.recogniser.Result()            
                result = json.loads(result)
                text = result['text']
                if text == "":
                    pass
                else:
                    return text