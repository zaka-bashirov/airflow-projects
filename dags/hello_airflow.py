from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 11, 24),
    schedule="@daily",
    catchup=False,
    tags=["learning"],
) as dag:

    hello_task = BashOperator(
        task_id="hello_task",
        bash_command="echo 'Hello from GitHub and Airflow!'",
    )
