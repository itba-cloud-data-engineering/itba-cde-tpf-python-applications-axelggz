from sqlalchemy import select
from datetime import datetime, timedelta

from Modules.Classes import StockValue
from Modules.PlotLib import stockPlot
import Modules.Postgres as Postgres

from Tasks.config import mSymbols

mEngine = Postgres.engine
connection = mEngine.connect()

def obtainSymbolData(pSymbol):
    a_date = datetime.now()
    days = timedelta(7)
    
    new_date = a_date - days
    print(new_date)
    
    stmt = select([
        StockValue.date,
        StockValue.open,
        StockValue.close,
        StockValue.high,
        StockValue.low,
        StockValue.symbol
    ]).where(StockValue.date >= new_date).order_by(StockValue.date.asc())
    
    results = connection.execute(stmt).fetchall()

    symbolData = {"Time": [], "Open": [], "High": [], "Low": [], "Close": []}

    for date, open, close, high, low, symbol in results:

        time = str(date)
        time = time[:10]

        if symbol == pSymbol:
            symbolData['Time'].append(time)
            symbolData['Open'].append(open)
            symbolData['High'].append(high)
            symbolData['Low'].append(low)
            symbolData['Close'].append(close)
    
    return symbolData

def makePlot():

    for lSymbol in mSymbols:
        stockPlot(obtainSymbolData(lSymbol), lSymbol)