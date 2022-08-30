# Name: Instance.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Forms the fundamental properties of a Vicky instance.

import pyttsx3
import json
from vosk import Model, KaldiRecognizer
import pyaudio
from NLP.Classifier import classify

class Core():

    def __init__(self, wakeword="Vicky"):
        self.speech_engine = pyttsx3.init()
        self.vosk_model = Model("model")
        self.recogniser = KaldiRecognizer(self.vosk_model, 16000)
        self.audio_input = pyaudio.PyAudio()
        self.input_stream = self.audio_input.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        print("{} activated".format(wakeword))
        while True:
            self.listenForWakeword()
    
    def textToSpeech(self, text):
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def listenForWakeword(self):
        data = self.input_stream.read(4000, exception_on_overflow=False) # Read datastream from microphone

        if self.recogniser.AcceptWaveform(data):

            result = self.recogniser.Result()            
            result = json.loads(result)
            text = result['text']

            print(text)

            if text == "vicky": # Wake word detection
                self.listenForCommands()

    def listenForCommands(self):
        pauseCounter = 0
        print("Listening...")
        self.textToSpeech("Listening...")
        while pauseCounter < 1:
            data = self.input_stream.read(4000, exception_on_overflow=False) # Read datastream from microphone
            if self.recogniser.AcceptWaveform(data):
                result = self.recogniser.Result()            
                result = json.loads(result)
                text = result['text']
                if text == "":
                    pauseCounter += 1
                else:
                    pauseCounter = 1
                    entity = classify(text) # Classifies recognised text after wake word invocation

Vicky = Instance()