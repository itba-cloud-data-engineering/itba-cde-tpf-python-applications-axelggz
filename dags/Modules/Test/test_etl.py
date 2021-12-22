import sys; sys.path.insert(1, '/opt/airflow/dags/')
import Modules.WebRequests as WebRequests
from Tasks.config import mSymbols

API_Response = WebRequests.obtain_stocks(mSymbols)

def test_api():
    assert len(API_Response) == len(mSymbols)