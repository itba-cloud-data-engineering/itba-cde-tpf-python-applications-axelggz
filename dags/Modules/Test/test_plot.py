import os; import sys
sys.path.insert(1, '/opt/airflow/dags/')

from Tasks.config import mSymbols
import Tasks.makePlot as makePlot

errorsFound = 0

for lSymbol in mSymbols:
    symbolData = makePlot.obtainSymbolData(lSymbol)
    if len(symbolData) == 0:
       errorsFound == 1 


def test_data():
    assert errorsFound == 0