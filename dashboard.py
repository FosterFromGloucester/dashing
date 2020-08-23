import logging
from components.stock_ticker_ribbon import StockTickerRibbonComponent
from components.news_list import Newslist
import time
from PIL import Image,ImageDraw,ImageFont

dashboard_image = Image.new('1', (640, 384), 1)  # 255: clear the frame
stock_ribbon = StockTickerRibbonComponent(640,50)
stock_ribbon_image = stock_ribbon.draw()
dashboard_image.paste(stock_ribbon_image,(0, 384 - stock_ribbon.height))

news_list = Newslist(640,100)
news_list_image = news_list.draw()
dashboard_image.paste(news_list_image,(0, 384 - stock_ribbon.height - news_list_image.height))

dashboard_image.save("images/merged_image.jpg","JPEG")
dashboard_image.show()