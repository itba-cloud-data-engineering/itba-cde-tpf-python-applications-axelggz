from datetime import datetime, timedelta
from airflow.models import dag
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os

import Tasks.etl as etl
import Tasks.makePlot as makePlot



args={
    'owner': 'axel',
}


dt = datetime.strptime('19 Aug 2021', '%d %b %Y')
newdatetime = dt.replace(hour=14, minute=50)

dag = dag.DAG(
    default_args=args,
    dag_id='dag_stocks',
    start_date= datetime(year=2021, month=8, day=19),
    schedule_interval=('0 * * * *'),
    description='Dag de prueba para ITBA',
    catchup=False)

def _etl():
    etl.uploadData()


def _plot ():
    makePlot.makePlot()



with dag:
    etl = PythonOperator(
        task_id = 'etl',
        python_callable=_etl,
        retries = 10,
        retry_delay = timedelta(seconds = 3),
        provide_context=True
    )

    plot = PythonOperator(
        task_id = 'plot',
        python_callable=_plot,
        retries = 10,
        retry_delay = timedelta(seconds = 3),
        provide_context=True
    )

    etl >> plot