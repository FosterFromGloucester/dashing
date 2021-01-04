from .base import BaseComponent
from .surf_item import SurfItem
from PIL import Image,ImageDraw,ImageFont
import math
import random
from bs4 import BeautifulSoup
import requests
import re 


class SurfData:
    day: str
    rating: int
    wave_height: str
    wind_speed: str
    wind_direction: str

    def __init__(self, day, rating=0, wave_height=None, wind_speed=None, wind_direction=None):
        self.day = day
        self.rating = rating
        self.wave_height = wave_height
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed

class SurfRibbonComponent(BaseComponent):

    surf_days = [
        'SATURDAY',
        'SUNDAY',
    ]
    surf_components = []


    def __init__(self, width, height):
        super().__init__(width, height)
        component_data = self.load_component_data()
        self.create_components(component_data)

    def create_components(self, component_data):
        component_width = math.floor(self.width / len(self.surf_days))
        for surf_day in self.surf_days:
            data = [day_data for day_data in component_data if day_data.day.lower() == surf_day.lower()][0]
            surf_item = SurfItem(
                component_width,
                self.height,
                day=data.day,
                rating=f'{data.rating}_star',
                swell_min_max=data.wave_height,
                wind_speed=data.wind_speed,
                wind_direction=data.wind_direction
            )
            self.surf_components.append(surf_item) 

    @classmethod
    def extract_data_for_day(cls, day, soup):
        surf_day_data = SurfData(day=day.upper())
        soup_rows = soup.find_all('tr',{'data-date-anchor':re.compile(f'{day}.*')})
        for row in soup_rows:
            if row.small.text == 'Noon':
                wave_height_row = row.find('td','table-forecast-breaking-wave')
                surf_day_data.wave_height = list(wave_height_row.children)[1].text.strip()

                forecast_wind_speed_row = row.find('td','table-forecast-wind')
                surf_day_data.wind_speed = list(forecast_wind_speed_row.children)[1].text.strip() + ' MPH'

                wind_direction_row = row.find('td','last')
                surf_day_data.wind_direction =  wind_direction_row.get('title').split(' ')[2]

                forecast_rating_row = row.find('td','table-forecast-rating')
                stars = forecast_rating_row.find('ul','rating')
                star_count = 0
                for star in list(stars)[1::2]:
                    if star['class'] == ['active']:
                        star_count += 1
                surf_day_data.rating = star_count
        return surf_day_data

    def load_component_data(self):
        report_url = 'https://magicseaweed.com/Cape-Town-Surf-Report/81/'
        response = requests.get(url=report_url)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        
        saturday_surf_data = self.extract_data_for_day('Saturday',soup)
        sunday_surf_data = self.extract_data_for_day('Sunday', soup)

        return saturday_surf_data, sunday_surf_data


    def draw(self):
        component_num = 0
        for component in self.surf_components:
            component_image = component.draw()
            self.image.paste(component_image,(component.width * component_num, 0))
            component_num += 1
        return self.image