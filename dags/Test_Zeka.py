
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# Task-in icra edəcəyi Python funksiyası
def say_hello():
    print("Hello Data Engineer!")
    print("My first Airflow DAG is working!")


# DAG yaradılması
with DAG(
    dag_id="hello_world_dag",
    description="My first simple Airflow DAG",
    start_date=datetime(2026, 11, 24),
    schedule="@daily",
    catchup=False,
    tags=["learning", "example"],
) as dag:

    # Task yaradılması
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
