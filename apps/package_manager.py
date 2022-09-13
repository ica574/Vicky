# Name: package_manager.py
# Date: 05/09/2022
# Author: Isaac Cilia Attard
# Description: Manages packages and creates objects to be used by the main program from other scripts with standard calls.

import importlib
import json

app_dict = json.load(open("./apps/apps.json", "r"))

def install(module_name, class_name, app_cues): # Installs a module into the application dictionary
    app_dict[module_name] = {}
    app_dict[module_name]['class'] = class_name
    app_dict[module_name]['cues'] = app_cues
    json.dump(app_dict, open("./apps/apps.json", 'w'))

def uninstall(module_name): # Removes an app from the dictionary
    app_dict.pop(app_dict[module_name])
    json.dump(app_dict, open("./apps/apps.json", 'w'))

def list():
    return app_dict

def search(command): # Returns a key from a value in the dictionary
    for module_name in app_dict.keys():
        for cue in app_dict[module_name]['cues']:
            if command == cue:
                return [module_name, app_dict[module_name]['class']]
            else:
                pass

def factory(module_name, class_name): # Instantiates objects based on the keys corresponding to them in the dictionary
    directory = importlib.util.spec_from_file_location(module_name, "./apps/{}.py".format(module_name))
    app_module = directory.loader.load_module()
    app_object = getattr(app_module, class_name)
    app_instance = app_object()
    return app_instance