import logging
from components.stock_ticker_ribbon import StockTickerRibbonComponent
from components.weather_ribbon import WeatherRibbonComponent
from components.surf_ribbon import SurfRibbonComponent
from components.news_list import Newslist
import time
from PIL import Image,ImageDraw,ImageFont
from os import environ

print('Create Image...')
dashboard_image = Image.new('1', (640, 384), 1)

print('Draw Weather...')
weather_ribbon = WeatherRibbonComponent(320,175)
weather_ribbon_image = weather_ribbon.draw()
dashboard_image.paste(weather_ribbon_image,(0,0))

print('Draw Surf...')
surf_ribbon = SurfRibbonComponent(320,175)
surf_ribbon_image = surf_ribbon.draw()
dashboard_image.paste(surf_ribbon_image,(320,0))

print('Draw News...')
news_list = Newslist(640,160)
news_list_image = news_list.draw()
dashboard_image.paste(news_list_image,(0, weather_ribbon.height + 1))

print('Draw Stocks...')
stock_ribbon = StockTickerRibbonComponent(640,50)
stock_ribbon_image = stock_ribbon.draw()
dashboard_image.paste(stock_ribbon_image,(0, weather_ribbon.height + news_list.height + 1))

on_device = environ.get('ON_DEVICE', False)
if on_device:
    print('Init drivers...')
    from waveshare import epd_driver
    epd = epd_driver.EPD()
    epd.init()
    epd.Clear()
    print('Write to screen...')
    epd.display(epd.getbuffer(dashboard_image))
else:
    dashboard_image.save("images/merged_image.jpg","JPEG")
    dashboard_image.show()
print('Done')
