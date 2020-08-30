from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys
import math

class SurfItem(BaseComponent):

    border_size = 1

    def __init__(self, width, height, day, rating, swell_min_max,wind_speed, wind_direction):
        super().__init__(width, height)
        self.rating = rating
        self.swell_min_max = swell_min_max
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.day = day

    def draw(self):
        draw = ImageDraw.Draw(self.image)
        
        draw.rectangle([(0,0),(self.width,self.height)],width=self.border_size)

        day_w, day_h = self.font18.getsize(self.day)
        day_w_middle= math.floor((self.width-day_w)/2)
        draw.text((day_w_middle, 10), self.day, font=self.font18, fill=0)

        rating_icon = self.load_icon(self.rating)
        self.image.paste(rating_icon,(2,day_h+40))

        swell_min_max_w, _ = self.font24.getsize(self.swell_min_max)
        swell_min_max_middle = math.floor((self.width-swell_min_max_w)/2)
        draw.text((swell_min_max_middle, self.height - 60), self.swell_min_max, font=self.font24, fill=0)
        
        wind_speed_w, _ = self.font24.getsize(self.wind_speed)
        wind_speed_w_middle= math.floor((self.width-wind_speed_w)/2)
        draw.text((wind_speed_w_middle, self.height - 40), self.wind_speed, font=self.font24, fill=0)
        


        return self.image
