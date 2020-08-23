from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys
import math

class NewsItem(BaseComponent):

    padding = 5

    def __init__(self, width, height, headline):
        super().__init__(width, height)
        self.headline = headline

    def draw(self):
        draw = ImageDraw.Draw(self.image)

        # Draw the bullet point 
        middle = math.floor(self.height / 2)
        bullet_width, bullet_height = 4,4
        draw.rectangle([(0, middle-bullet_height/2),(bullet_width, middle+bullet_height/2)], fill=0)

        # Draw the headline text 
        _, h = draw.textsize(self.headline)
        news_height = ((self.height)-h)/2
        draw.text((bullet_width + self.padding, news_height), self.headline, font=self.font24, fill=0)

        return self.image
