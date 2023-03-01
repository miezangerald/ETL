from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 28, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mon_programme',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

def run_extract():
    os.system("python3 /media/prempeh/Nouveau nom/MASTER2/DATA ENGINEERING/airflow/EXTRACT/main.py")

def run_transform():
    os.system("python3 /media/prempeh/Nouveau nom/MASTER2/DATA ENGINEERING/airflow/TRANSFORM/analyse_sentiment.py")


extract_task = PythonOperator(
    task_id='extract',
    python_callable=run_extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=run_transform,
    dag=dag,
)

extract_task >> transform_task