# Name: main.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from instance import Core
from event import EventHook
from apps import factory

vicky = Core() # Instantiates new Vicky instance with core functions

vicky.before_wakeword, vicky.after_wakeword = EventHook(), EventHook() # Major events in the program's execution

vicky.before_wakeword.enlist(lambda: vicky.listen_for_wakeword()) # Registers event handlers with event hooks
vicky.after_wakeword.enlist(lambda: vicky.listen_for_commands())

event_state = vicky.before_wakeword.activate(0)() # Inititates program and saves state of first event

if event_state == True:
    weather = factory.instantiate()
    print(weather.handle_command())
    #vicky.after_wakeword.activate(0)