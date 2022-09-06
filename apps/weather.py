# Name: weather.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Gives a brief weather report to the user.

from apps.app import App
import apps.factory

class Weather(App):
    def commands(self, command: str):
        return ['weather', 'forecast', 'what is the weather']

    def handle_command(self):
        forecast = "Sunny forever"
        return forecast
    
    def initialise():
        factory.register('weather_skill', Weather)