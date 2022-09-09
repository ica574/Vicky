# Name: weather.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Gives a brief weather report to the user.

import apps.factory as factory

class Weather():
    def test(self):
        print("Always sunny!")

class Weather_App():
    def commands(self, command: str):
        return ['weather', 'forecast', 'what is the weather']

    def handle_command(self):
        theweather = Weather()
        return theweather.test()
    
    def initialise(self):
        factory.enlist("weather_skill", self)
        factory.instantiate('weather_skill')