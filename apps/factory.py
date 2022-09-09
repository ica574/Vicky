# Name: factory.py
# Date: 05/09/2022
# Author: Isaac Cilia Attard
# Description: Creates objects to be used by the main program from other scripts with standard calls.

#app_list = dict()
app_list = {"weather_skill": "test"}
    
def enlist(app_name, app_object):
    app_list[app_name] = app_object

def discharge(app_name):
   app_list.pop(app_name)

def instantiate(app_name):
    app_object = app_list[app_name]
    return app_object