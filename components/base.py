from PIL import Image, ImageFont
import os
import sys

class BaseComponent:

    fonts_dir = os.path.join('resources','fonts')
    icon_dir = os.path.join('resources','icons')

    font_path = (os.path.abspath(os.path.join(fonts_dir, 'Font.ttc')))
    font24 = ImageFont.truetype(font_path, 18)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('1', (width, height), 255)  # 255: clear the frame

    def load_icon(self,icon_name):
        return Image.open(os.path.abspath(os.path.join(self.icon_dir,icon_name+'.png')))

    def draw(self):
        return 
    

    