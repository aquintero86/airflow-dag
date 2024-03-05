from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG(
        dag_id = "my-first-dag",
        start_date= datetime(2024,2,24)

) as dag:
    task_1= BashOperator(task_id="my-first-task", bash_command="echo hello world")