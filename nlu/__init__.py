import datetime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        return "Current time: " + str(datetime.datetime.now().hour)
    
    @staticmethod
    def get_date():
        return "Current date: " + str(datetime.datetime.now().date)
    
    @staticmethod
    def get_year():
        return "Current year: " + str(datetime.datetime.now().year)