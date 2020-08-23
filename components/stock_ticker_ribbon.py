from .base import BaseComponent
from .stock import Stock
from PIL import Image,ImageDraw,ImageFont
import math
class StockTickerRibbonComponent(BaseComponent):

    stock_list = [
        'APPL',
        'GOOGL',
        'TSLA',
        'MCSFT',
        'ABIN',
        'TEST6'

    ]

    stock_components = []


    def __init__(self, width, height):
        super().__init__(width, height)
        component_data = self.load_component_data()
        self.create_components(component_data)

    def create_components(self, component_data):

        component_width = math.floor(self.width / len(self.stock_list))

        for stock in self.stock_list:
            stock = Stock(component_width, self.height, name = stock, percentage_change='-9.31')
            self.stock_components.append(stock) 

    def load_component_data(self):
        return {}


    def draw(self):
        component_num = 0
        component_width = math.floor(self.width / len(self.stock_list))
        for component in self.stock_components:
            component_image = component.draw()
            self.image.paste(component_image,(component_width * component_num, 0))
            component_num += 1
        
        return self.image
        
