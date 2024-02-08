import random
class Weather():
    def __init__(self):
        self.status = ['rainy', 'sunny']

    def gimme_weather_status(self): #6
        return random.choice(self.status)