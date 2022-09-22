import eel
import apps.weather as weather
from apps.package_manager import search, factory
from Main import importer
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
        path = "./apps/" + app
        AppImport = importer(path)
        AppClass = getattr(AppImport, app + "_App")
        AppClass.manifest()

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
