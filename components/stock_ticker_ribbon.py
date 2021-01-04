from .base import BaseComponent
from .stock import Stock
from PIL import Image,ImageDraw,ImageFont
import math
import yfinance as yf

class StockData:
    symbol: str
    start: int
    end: int
    period: str

    def __init__(self, symbol, start=0, end=0, period=None):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.period = period

class StockTickerRibbonComponent(BaseComponent):

    stock_list = [
        'SNE',
        'TSLA',
        'AAPL',
        'MSFT',
        'ATVI',
    ]
    stock_components = []


    def __init__(self, width, height):
        super().__init__(width, height)
        component_data = self.load_component_data()
        self.create_components(component_data)

    def create_components(self, component_data):
        component_width = math.floor(self.width / len(self.stock_list))
        for stock in self.stock_list:
            data = [stock_data for stock_data in component_data if stock_data.symbol.lower() == stock.lower()][0]
            percentage_change = round(((data.end - data.start) / data.start) * 100, 2)
            stock = Stock(component_width, self.height, name=stock, percentage_change=str(percentage_change),positive=percentage_change>0)
            self.stock_components.append(stock) 

    def load_component_data(self):
        period="1d"
        component_data = []
        stocker_tickers = yf.Tickers(' '.join([stock.lower() for stock in self.stock_list]))
        for stock in self.stock_list:
            stock_history = getattr(stocker_tickers.tickers, stock).history(period=period)
            stock_data = StockData(
                symbol= stock,
                start=stock_history.iloc[0][0],
                end=stock_history.iloc[0][3],
                period=period
            )
            component_data.append(stock_data)
        return component_data


    def draw(self):
        component_num = 0
        for component in self.stock_components:
            component_image = component.draw()
            self.image.paste(component_image,(component.width * component_num, 0))
            component_num += 1
        
        return self.image
        
