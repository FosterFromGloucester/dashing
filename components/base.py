from PIL import Image, ImageFont
import os
import sys

class BaseComponent:

    fontsdir = os.path.join('resources','fonts')
    path = (os.path.abspath(os.path.join(fontsdir, 'Font.ttc')))
    font24 = ImageFont.truetype(path, 18)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('1', (width, height), 255)  # 255: clear the frame

    def draw(self):
        return 
    

    