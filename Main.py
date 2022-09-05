# Name: main.py
# Author: Isaac Cilia Attard
# Date: 29/08/2022
# Description: Main file pertatining to the assistant. Includes speech recognition model and wake word invocation function.

from instance import core
from event import event_hook

vicky = core() # Instantiates new Vicky instance with core functions

vicky.before_wakeword, vicky.after_wakeword = event_hook(), event_hook() # Major events in the program's execution

vicky.before_wakeword.enlist(vicky.listen_for_wakeword())
vicky.after_wakeword.enlist(vicky.listen_for_commands())
vicky.before_wakeword.activate(0)

if vicky.before_wakeword.activate(0) == True:
    vicky.after_wakeword.activate(0)