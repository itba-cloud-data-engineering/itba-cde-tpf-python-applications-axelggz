from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Stocks table class
class StockValue(Base):
    __tablename__ = "stock_value"

    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    date = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)

    def __init__(self, symbol, date, open, high, low, close):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close

