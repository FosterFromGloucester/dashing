from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys
from .news_item import NewsItem
import math
import requests
from os import environ

class Newslist(BaseComponent):

    news_components = []

    item_padding = 10
    item_height = 25
    item_width = 70

    def __init__(self, width, height):
        super().__init__(width, height)
        data = self.load_component_data()
        self.create_components(data)


    def format_headline(self, raw_headline):
        source_removed = raw_headline[0:raw_headline.rindex('-')]
        if len(source_removed) > 70:
            truncated = source_removed[0:67]
            return f"{truncated[0:truncated.rindex(' ')]}..."
        return source_removed

    def create_components(self, news_data):
        for news_item_idx in range(5):
            news_item = NewsItem(
                self.width, 
                self.item_height, 
                headline=self.format_headline(news_data[news_item_idx]['title'])
            )
            self.news_components.append(news_item) 


    def load_component_data(self):
        news_api_url = 'http://newsapi.org/v2/top-headlines'
        params = {
            'country':'za',
            'apiKey': environ.get('NEWS_API_KEY')
        }
        news_response = requests.get(url=news_api_url, params=params, timeout=10)
        news_response.raise_for_status()
        news_data = news_response.json()
        return news_data['articles']

    def draw(self):
        component_num = 0
        for news_component in self.news_components:
            component_image = news_component.draw()
            self.image.paste(component_image,(self.item_padding, (component_num * self.item_height )))
            component_num += 1
    
        return self.image

