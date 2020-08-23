from .base import BaseComponent
from PIL import Image,ImageDraw,ImageFont
import os
import sys

class Stock(BaseComponent):

    border_size = 1
    stock_percentage_divide = 6

    def __init__(self, width, height, name, percentage_change):
        super().__init__(width, height)
        self.name = name
        self.percentage_change = percentage_change

    def draw(self):
        draw = ImageDraw.Draw(self.image)

        # Draw the border
        draw.rectangle([(0,0),(self.width,self.height)],width=self.border_size)

        # Draw the stock name
        stock_w, stock_h = draw.textsize(self.name)
        stock_w_middle= (self.width-stock_w)/2
        stock_h_middle = (((self.height)-stock_h)/4)
        draw.text((stock_w_middle,stock_h_middle), self.name, font=self.font24, fill=0)

        # Draw the percentage change under the stock name
        w, h = draw.textsize(self.percentage_change)
        stock_p_width = (self.width-w)/2
        stock_p_height = stock_h + self.stock_percentage_divide + h
        draw.text((stock_p_width,stock_p_height), self.percentage_change, font=self.font24, fill=0)

        return self.image

