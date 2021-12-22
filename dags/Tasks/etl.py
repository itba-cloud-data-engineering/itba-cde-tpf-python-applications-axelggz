import os
import sys
from typing import MutableSequence

import Modules.WebRequests as WebRequests
import Modules.Postgres as Postgres
from Modules.Classes import StockValue

from datetime import datetime, timedelta
from Tasks.config import mSymbols

mEngine = Postgres.engine
mSession = Postgres.session

def uploadData():

    # Create tables if they don't exist
    StockValue.metadata.create_all(mEngine)
    mResponses = WebRequests.obtain_stocks(mSymbols)


    for mResponse in mResponses:
        
        # Obtaining Metadata
        mMetadata = mResponse['Meta Data']
        mSymbol = mMetadata['2. Symbol']
        mDate = mMetadata['3. Last Refreshed']
        mTimeseries = mResponse['Time Series (15min)']

        for serie in mTimeseries.items():

            date_time_obj = datetime.strptime(serie[0], '%Y-%m-%d %H:%M:%S')

            # Searching in the db for and old value
            oldValue = mSession.query(StockValue.date, StockValue.symbol).filter((StockValue.date == date_time_obj) & (StockValue.symbol == mSymbol)).first()

            if not oldValue:
                newValue = StockValue(
                    symbol=mSymbol,
                    date=date_time_obj,
                    open=serie[1]['1. open'],
                    high=serie[1]['2. high'],
                    low=serie[1]['3. low'],
                    close=serie[1]['4. close'])

                mSession.add(newValue)

        mSession.commit()
        mSession.close()