import requests
import json
import pandas as pd
import time

# Importing API Key from Config file
import sys
sys.path.insert(1, '/opt/airflow/dags/')
from Tasks.config import API_Key


def http_request(url):
    return requests.get(url).json()


def obtain_stocks(pSymbols):

    Responses = []

    for Symbol in pSymbols:

        response = http_request(
            f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=15min&symbol={Symbol}&apikey={API_Key}')

        Responses.append(response)
        time.sleep(1)

    return Responses
