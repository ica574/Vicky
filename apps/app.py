# Name: app.py
# Author: Isaac Cilia Attard
# Date: 05/09/2022
# Description: Defines an abstract class to be used by specific classes that extend it.

from instance import Core


class App():
    def commands(self, command:str):
        pass

    def handle_command(self, command:str, core:Core):
        pass