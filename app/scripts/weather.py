import dotenv
import requests
from os import path
def get_weather(city='Prague'):
    env_path = path.join(path.dirname(path.dirname(__file__)), '..', '.env')
    dotenv.load_dotenv(env_path)
    api_key = dotenv.get_key(env_path, 'WEATHER_API_KEY')
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
    "key": api_key,
    "q": city,
    "lang": "cs",  
}

    response = requests.get(url, params=params)
    data = response.json()
    #Teplota C | pocasi text | pocasi ikona | teplota pocitova
    weather_dict = data['current']['temp_c'], data['current']['condition']['text'], data['current']['condition']['icon'], data['current']['feelslike_c']
    return weather_dict
get_weather()