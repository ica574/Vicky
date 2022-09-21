import eel
import apps.weather as weather
from apps.package_manager import search, factory

appsInstalled = []

@eel.expose
def setApps(apps):
    appsInstalled = apps
    
    for app in appsInstalled:
        if app == 'vicky-weather':
            factory("weather", "Weather_App")
            print("Installing weather...")
        
def letConn():
    count = 0

    while True:
        eel.sleep(1)
        count = count + 1

        if(count > 10):
            print("Break this batch!")
            break
        continue