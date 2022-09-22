# Name: main.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from apps.package_manager import search, factory
from core import Core
from event import EventHook

import eel
import eelHelper

"""Eel initialisation"""
eel.init("web")
eel.start("index.html", block=False)
eelHelper.letConn()

weather = __import__('weather')

vicky = Core() # Instantiates new Vicky instance with core functions

vicky.before_wakeword, vicky.after_wakeword = EventHook(), EventHook() # Major events in the program's execution

vicky.before_wakeword.enlist(lambda: vicky.listen_for_wakeword()) # Registers event handlers with event hooks
vicky.after_wakeword.enlist(lambda: vicky.listen_for_commands())

"""Main organ of the program"""
while True:
    event_state = vicky.before_wakeword.activate(0)() # Inititates program and saves state of first event

    while event_state == True:
        command = vicky.after_wakeword.activate(0)() # Listens for commands such that apps can be executed
        print(command)
        try:
            app_exec = search(command)
            app = factory(app_exec[0], app_exec[1])
            app.run(command)
            event_state = False
        except:
            print("Command not identified. Please re-specify...")
            event_state = False