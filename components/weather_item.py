from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys
import math

class WeatherItem(BaseComponent):

    border_size = 1

    def __init__(self, width, height, day, outlook, temp_high, temp_low):
        super().__init__(width, height)
        self.outlook = outlook
        self.temp_high = temp_high
        self.temp_low = temp_low
        self.day = day

    def draw(self):
        draw = ImageDraw.Draw(self.image)
        
        draw.rectangle([(0,0),(self.width,self.height)],width=self.border_size)

        day_w, day_h = self.font18.getsize(self.day)
        day_w_middle= math.floor((self.width-day_w)/2)
        draw.text((day_w_middle, 10), self.day, font=self.font18, fill=0)

        weather_icon = self.load_icon(self.outlook)
        self.image.paste(weather_icon,(math.floor((self.width-75)/2),day_h+20))

        draw.rectangle([(0,self.height-25),(self.width,self.height-50)],width=self.border_size)
        temp_high_w, _ = self.font24.getsize(self.temp_high)
        temp_h_w_middle= math.floor((self.width-temp_high_w)/2)
        draw.text((temp_h_w_middle, self.height - 50), self.temp_high, font=self.font24, fill=0)
        
        draw.rectangle([(0,self.height),(self.width,self.height-25)],width=self.border_size)
        temp_low_w, _ = self.font24.getsize(self.temp_low)
        temp_l_w_middle= math.floor((self.width-temp_low_w)/2)
        draw.text((temp_l_w_middle, self.height - 25), self.temp_low, font=self.font24, fill=0)
        
        return self.image
