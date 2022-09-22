# Name: weather.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Gives a brief weather report to the user.

import apps.package_manager as package_manager
import geocoder
import requests
import eel
from core import Core

class Weather():
    def exec(self):
        """Defines API keys and essential URLs for operating the App"""
        owm_api_key = "ca4693daa0d99e87456db96bb2b70108" # API key for OpenWeatherMap
        tt_api_key = "2gDxHCqjw2GhXnX2vcLCbGDDeCOB5AV7" # API key for TomTom
        base_url = "http://api.openweathermap.org/data/2.5/weather?" # URL for OpenWeatherMap

        """Geolocation data parsing"""
        geolocation = geocoder.ip("me") # Extracts location from IP address
        geolocation_data = geocoder.tomtom(geolocation, key=tt_api_key) # Downloads JSON-embedded data about location from TomTom API
        city_name = geolocation_data.json['raw']['address']['municipality'] # Extracts city name from geolocation data

        """Retrieval of weather data"""
        complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name # Builds URL to extract weather data from OpenWeatherMap API
        response = requests.get(complete_url) # Retrieves weather data based on previous URL
        x = response.json() # Encodes request data in JSON

        if x["cod"] != "404": # Presents data given that city name successfully matches query
            y = x["main"]
            current_temperature = y["temp"] - 273
            z = x["weather"]
            weather_description = z[0]["description"]
            print("Current temperature is " + str(current_temperature) + ".\n Current weather condition is " + str(weather_description))
            tts = Core()
            tts.text_to_speech("Current temperature is " + str(current_temperature) + ".\n Current weather condition is " + str(weather_description))

        else: # Handles case in which city name is not identified
            print("City mismatch!")

class Weather_App():
    def cues(self):
        return ["forecast", "what is the weather", "tell me the weather"]

    def run(self, command):
        weather_app = Weather()
        return weather_app.exec()

    def manifest(self):
        print("weather manifest")
        package_manager.install("weather", self.__class__.__name__, self.cues())