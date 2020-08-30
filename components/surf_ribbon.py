from .base import BaseComponent
from .surf_item import SurfItem
from PIL import Image,ImageDraw,ImageFont
import math
import random

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
            surf_item = SurfItem(component_width, self.height,day=surf_day,rating=random.choice(['five_star']),swell_min_max='3-5ft',wind_speed='4 MPH', wind_direction='N')
            self.surf_components.append(surf_item) 

    def load_component_data(self):
        return {}


    def draw(self):
        component_num = 0
        for component in self.surf_components:
            component_image = component.draw()
            # print(f'{component.width * component_num}:{0}')
            self.image.paste(component_image,(component.width * component_num, 0))
            component_num += 1
        
        return self.image