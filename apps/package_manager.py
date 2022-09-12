# Name: package_manager.py
# Date: 05/09/2022
# Author: Isaac Cilia Attard
# Description: Manages packages and creates objects to be used by the main program from other scripts with standard calls.

from importlib import *
import importlib
import pickle

#app_dict = pickle.load(open("apps/apps.pkl", "rb"))
app_dict = pickle.load(open("apps/apps.pkl", "rb"))
# app_dict = pickle.Unpickler.load(open("apps/apps.pkl", "rb"))

def install(app_name, class_name, app_cues):
    app_dict[app_name] = {}
    app_dict[app_name]['class'] = class_name
    app_dict[app_name]['cues'] = app_cues
    pickle.dump(app_dict, open("apps/apps.pkl", "wb"), protocol=pickle.HIGHEST_PROTOCOL)

def uninstall(app_name):
    app_dict.pop(app_dict[app_name])
    pickle.dump(app_dict, open("apps/apps.pkl", "wb"), protocol=pickle.HIGHEST_PROTOCOL)

def factory(module_name, class_name):
    directory = importlib.util.spec_from_file_location(module_name, "./apps/{}.py".format(module_name))
    app_module = directory.loader.load_module()
    #class_ = getattr(module, "Weather_App")
    #instance = class_()
    #instance.run()
    app_object = getattr(app_module, class_name)
    app_instance = app_object()
    return app_instance

def search_by_value(command):
    for app_name in app_dict.keys():
        for cue in app_dict[app_name]['cues']:
            if command == cue:
                return [app_name, app_dict[app_name]['class']]
            else:
                return None