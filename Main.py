# Name: main.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from importlib import import_module
from apps.package_manager import search, factory, list
from apps import *
from Instance import Core
from event import EventHook

from apps.test import Test_App
from apps.weather import Weather_App

import eel
import eelHelper
eel.init("web")

eel.start("index.html", block=False)
eelHelper.letConn()

vicky = Core() # Instantiates new Vicky instance with core functions

vicky.before_wakeword, vicky.after_wakeword = EventHook(), EventHook() # Major events in the program's execution

vicky.before_wakeword.enlist(lambda: vicky.listen_for_wakeword()) # Registers event handlers with event hooks
vicky.after_wakeword.enlist(lambda: vicky.listen_for_commands())

event_state = vicky.before_wakeword.activate(0)() # Inititates program and saves state of first event

if event_state == True:
    command = vicky.after_wakeword.activate(0)() # Listens for commands such that apps can be executed
    print(command)
    eel.handleInput(command)
    app_exec = search(command)
    app = factory(app_exec[0], app_exec[1])
    if(app == "error"):
        vicky.text_to_speech("Sorry, I didn't get you")
    else:
        vicky.text_to_speech(app.run())
    