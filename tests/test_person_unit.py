from lib.person import *

def test_person_instantiates_with_name_and_weather():
    person = Person('Samantha')

    actual_name = person.name
    actual_weather = type(person.weather)

    expected_name = 'Samantha'
    expected_weather = type(Weather())
    assert actual_name == expected_name
    assert actual_weather == expected_weather

def test_lets_go_out_when_rainy():
    person = Person('Vijay')

    actual = person.go_out()
    expected = "Let's go out with an umbrella!"

    assert actual == expected

def test_lets_go_out_when_sunny():
    person = Person('Anamaria')

    actual = person.go_out()
    expected = "Let's go out with sunglasses!"

    assert actual == expected
