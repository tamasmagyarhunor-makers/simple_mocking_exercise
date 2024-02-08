from lib.weather import Weather

class Person():
    def __init__(self, name):
        self.name = name
        self.weather = Weather()

    def go_out(self):
        if self.weather.gimme_weather_status() == 'rainy':
            return "Let's go out with an umbrella!"
        if self.weather.gimme_weather_status() == 'sunny':
            return "Let's go out with sunglasses!"