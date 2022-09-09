# Name: factory.py
# Date: 05/09/2022
# Author: Isaac Cilia Attard
# Description: Creates objects to be used by the main program from other scripts with standard calls.

import json

app_list = dict()
app_list_file = open("apps.json", "w")
    
def enlist(app_name, app_object):
    app_list[app_name] = app_object
    json.dump(app_list, app_list_file)

def discharge(app_name):
   app_list.pop(app_name)
   json.dump(app_list, app_list_file)

def instantiate(app_name):
    app_object = app_list[app_name]
    return app_object