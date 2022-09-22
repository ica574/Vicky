import eel
import importlib
from apps.package_manager import search, factory
appsInstalled = []

@eel.expose
def setApps(apps):
    appsInstalled = apps
    
    for app in appsInstalled:
        if app == 'vicky-weather':
            factory("weather", "Weather_App")
            print("Installing weather...")
        
@eel.expose
def installApps(apps):
#after NFTs are checked
#apps is an array of app names which user is licensed for, which correspond to the file name
#for example: weather.py => ['weather']
    for app in apps:
        print("installing " + app)
        path = "./apps/" + app + ".py"
        load = importlib.util.spec_from_file_location(app, path)
        app_module = load.loader.load_module()
        app_class = getattr(app_module, app.title() + "_App")
        app_instance = app_class()
        app_instance.manifest()

def letConn():
    count = 0

    while True:
        eel.sleep(1)
        count = count + 1

        if(count > 10):
            print("Break this batch!")
            break
        continue

installApps(["weather"])
