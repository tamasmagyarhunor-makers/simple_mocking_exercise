# Simple Python mocking exercise

### Setting up
```
$ git clone git@github.com:tamasmagyarhunor-makers/simple_mocking_exercise.git
$ cd simple_mocking_exercise
$ pipenv install
$ pipenv run pytest
```

### Exercise
Notice how the tests are inconsistently passing or failing depending on what the `Weather::gimme_weather_status()` returns. The function has a random functionality so its behaviour is 50-50% between returning 'rainy' or 'sunny'. Because of this, our tests outcome is completely random. We have to find a way to mock this behavior, so that both scenarios can be tested consistently.

1. Go out when its 'rainy' should return `"Let's go out with an umbrella!"`
2. Go out when its 'sunny' should return `"Let's go out with sunglasses!"`