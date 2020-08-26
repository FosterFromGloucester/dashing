from .base import BaseComponent
from .weather_item import WeatherItem
from PIL import Image,ImageDraw,ImageFont
import math
import random

class WeatherRibbonComponent(BaseComponent):

    weather_days = [
        'TODAY',
        'TOMORROW',
    ]

    weather_components = []


    def __init__(self, width, height):
        super().__init__(width, height)
        component_data = self.load_component_data()
        self.create_components(component_data)

    def create_components(self, component_data):

        component_width = math.floor(self.width / len(self.weather_days))

        for weather_day in self.weather_days:
            weather_item = WeatherItem(component_width, self.height,day=weather_day,outlook=random.choice(['windy', 'cloudy','raining','sunny']),temp_high='10',temp_low='9')
            self.weather_components.append(weather_item) 

    def load_component_data(self):
        return {}


    def draw(self):
        component_num = 0
        for component in self.weather_components:
            component_image = component.draw()
            # print(f'{component.width * component_num}:{0}')
            self.image.paste(component_image,(component.width * component_num, 0))
            component_num += 1
        
        return self.image