from .base import BaseComponent
from .weather_item import WeatherItem
from PIL import Image,ImageDraw,ImageFont
import math
import random
import requests
from os import environ

class WeatherRibbonComponent(BaseComponent):

    weather_days = [
        'TODAY',
        'TOMORROW',
    ]
    icon_api_mapping = {
        'cloudy': lambda x : 805 > x > 800,
        'raining': lambda x : 532 > x > 199,
        'sunny': lambda x : x == 800,
    }
    weather_components = []

    def derive_outlook_icon(self, weather_id):
        for icon, id_range_func in self.icon_api_mapping.items():
            if id_range_func(weather_id):
                return icon
        return 'unknown'

    def __init__(self, width, height):
        super().__init__(width, height)
        component_data = self.load_component_data()
        self.create_components(component_data)

    def create_components(self, weather_data):
        component_width = math.floor(self.width / len(self.weather_days))
        for weather_day_idx in range(len(self.weather_days)):
            temps = weather_data[weather_day_idx].get('temp',{})
            outlook_id = weather_data[weather_day_idx].get('weather',{})[0].get('id')
            weather_item = WeatherItem(
                component_width,
                self.height,
                day=self.weather_days[weather_day_idx],
                outlook=self.derive_outlook_icon(outlook_id),
                temp_high=f"{math.floor(temps['max'])}℃",
                temp_low=f"{math.floor(temps['min'])}℃"
            )
            self.weather_components.append(weather_item) 

    def load_component_data(self):
        weather_api = 'https://api.openweathermap.org/data/2.5/onecall'
        params = {
            'lat': -33.9249,
            'lon': 18.4241,
            'exclude': 'hourly,minutely,current,alerts',
            'appid': environ.get('OPEN_WEATHER_API_TOKEN'),
            'units': 'metric'
        }
        weather_response = requests.get(url=weather_api, params=params, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        return weather_data['daily']


    def draw(self):
        component_num = 0
        for component in self.weather_components:
            component_image = component.draw()
            self.image.paste(component_image,(component.width * component_num, 0))
            component_num += 1
        
        return self.image