# Name: weather.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Gives a brief weather report to the user.

#import package_manager as package_manager

class Weather():
    def test(self):
        print("Always sunny!")

class Weather_App():
    def cues(self):
        return ["forecast"]

    def run(self):
        weather_app = Weather()
        return weather_app.test()

    def initialise(self):
        pass
        #package_manager.install("weather", self.__class__.__name__, self.cues())