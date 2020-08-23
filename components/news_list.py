from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys
from .news_item import NewsItem
import math

class Newslist(BaseComponent):
    # TODO: Remove me 
    news_items = [
        'This is a test news headline',
        'This is another headline text that is slightly longer'
    ]
    news_components = []
    item_padding = 10
    item_height = 30

    def __init__(self, width, height):
        super().__init__(width, height)

        for news_item in self.news_items:
            news_item = NewsItem(self.width, self.item_height, headline=news_item)
            self.news_components.append(news_item) 

    def draw(self):
        component_num = 0
        for news_component in self.news_components:
            component_image = news_component.draw()
            self.image.paste(component_image,(self.item_padding, (component_num * self.item_height )))
            component_num += 1
    
        return self.image

