from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from api_etl import run_etl
from pokemon_dashboard import dashboard

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='Chal jaa bhai',
    schedule_interval='@daily'  # Runs daily
)

run_task = PythonOperator(
    task_id='task_1',
    python_callable=run_etl,
    dag=dag,
)

run_task2 = PythonOperator(
    task_id='task_2',  # Changed task_id to avoid duplication
    python_callable=dashboard,
    dag=dag,
)

run_task >> run_task2  # Set execution order