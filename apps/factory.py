# Name: factory.py
# Date: 05/09/2022
# Author: Isaac Cilia Attard
# Description: Creates objects to be used by the main program from other scripts with standard calls.

from typing import Callable
from apps.weather import Weather

app_list = {}

#def enlist(app_name: str, app_creation: Callable[..., App]):
   #app_list[app_name] = app_creation

def discharge(app_name: str):
    app_list.pop(app_name, None)

def instantiate():
    weather = Weather()
    return weather