# Name: test.py
# Author: Isaac Cilia Attard
# Date: 09/09/2022
# Description: Dummy app used to test factory functionality

import apps.package_manager as package_manager
from apps.app import App

class Test():
    def test(self):
        print("It worked!")

class Test_App(App):
    def cues(self):
        return ['test']

    def run(self):
        test = Test()
        return test.test()

    def initialise(self):
        package_manager.install("test", self.__class__.__name__, self.cues())