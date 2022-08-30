# Name: main.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
from nlu import SystemInfo
from nlu.classifier import classify
from instance import Core

Vicky = Core("Vicky")