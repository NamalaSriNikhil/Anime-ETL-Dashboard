

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from extract import fetch_anime_data
from transform import transform_data
from load import load_to_sqlite

default_args = {
    'owner': 'Nikhil',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='Popular_anime_pipeline',
    description='ETL pipeline for popular animes',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id='extract_anime_data',
        python_callable=fetch_anime_data
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id='load_to_db',
        python_callable=load_to_sqlite
    )

    extract >> transform >> load