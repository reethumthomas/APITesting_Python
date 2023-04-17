import pytest
import requests

API_KEY = '8980b5466f51d568ee460354f761a642'
BASE_URL = ' http://api.openweathermap.org/data/2.5/weather'

""" 1. Use the below weather end-point to get the current weather details of Hyderabad
    http://api.openweathermap.org/data/2.5/weather?q=hyderabad&appid={your_key} """


@pytest.fixture
def test_get_weather_data():
    query_param = {
        'q': 'hyderabad',
        'appid': API_KEY
    }

    weather_response = requests.get(BASE_URL, params=query_param)
    print(weather_response.url)
    assert weather_response.encoding == 'utf-8'
    print("Weather condition is", weather_response.json()['weather'][0]['description'])
    return weather_response


"""2. Use the coordinates (longitude and latitude) of of the above response to the end-point 
http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={your_key} and verify the below 
in response - name --> Hyderabad - sys.country --> IN - main.temp_min --> greater than 0 - main.temp --> greater than 0 """


def test_weather_with_lat_long(test_get_weather_data):
    response = test_get_weather_data.json()
    latitude = response['coord']['lat']
    longitude = response['coord']['lon']

    query_param = {
        'lat': latitude,
        'lon': longitude,
        'appid': API_KEY
    }

    weather_response = requests.get(BASE_URL, params=query_param)
    print(weather_response.url)

    assert weather_response.json()['name'] == 'Hyderabad'
    assert weather_response.json()['sys']['country'] == 'IN'
    assert weather_response.json()['main']['temp_min'] > 0
    assert weather_response.json()['main']['temp_max'] > 0

