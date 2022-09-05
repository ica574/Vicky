# Name: event.py
# Author: Isaac Cilia Attard
# Date: 03/09/2022
# Description: Defines an event hook to handle actions requested by the user. 

class event_hook:
    def __init__(self):
        self.handlers = [] # Contains a list of "consequences" should an event occur

    def enlist(self, handler): # Registers an event and adds it to the list
        self.handlers.append(handler)
        return self
    
    def discharge(self, handler): # De-registers an event and removes it from the list
        self.handlers.delete(handler)
        return self
    
    def activate(self, index): # Handles an event by triggering a handler from the list
        self.handlers[index]