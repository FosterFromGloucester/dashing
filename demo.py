import logging
from waveshare import epd_driver
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import os 
import sys

fontsdir = os.path.join('resources','fonts')


epd = epd7in5.EPD()
logging.info("init and Clear")
epd.init()
epd.Clear()
    
font24 = ImageFont.truetype(os.path.join(fontsdir, 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join(fontsdir, 'Font.ttc'), 18)

Himage = Image.new('1', (epd.width, epd.height), 256)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
draw.line([(0,epd.height-50),(epd.width,epd.height-50)],fill=0, width=3)
draw.text((epd.width/2, epd.height/2), 'hello world', font = font24, fill = 0)
epd.display(epd.getbuffer(Himage))
