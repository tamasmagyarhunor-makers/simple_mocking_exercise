from lib.person import *
from lib.weather import *
from unittest.mock import Mock

def test_person_instantiates_with_name():
    person = Person('Samantha')

    actual_name = person.name

    expected_name = 'Samantha'
    assert actual_name == expected_name

def test_lets_go_out_when_rainy():
    person = Person('Vijay')
    weather = Weather()
    person.add_weather(weather)

    actual = person.go_out()
    expected = "Let's go out with an umbrella!"

    assert actual == expected

def test_lets_go_out_when_sunny():
    person = Person('Anamaria')
    weather = Weather()
    person.add_weather(weather)
    actual = person.go_out()
    expected = "Let's go out with sunglasses!"

    assert actual == expected
