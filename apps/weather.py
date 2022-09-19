# Name: weather.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Gives a brief weather report to the user.

import apps.package_manager as package_manager
import eel

class Weather():
    def test(self):
        eel.handleResponse("Always sunny!")
        print("Always sunny!")
        return "Always sunny!"

class Weather_App():
    def cues(self):
        return ["forecast", "what is the weather", "tell me the weather", "How is the weather tomorrow"]

    def run(self):
        weather_app = Weather()
        return weather_app.test()

    def manifest(self):
        package_manager.install("weather", self.__class__.__name__, self.cues())