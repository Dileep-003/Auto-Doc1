from airflow import DAG
from airflow.operators.python_operator import PythonOperator  
from datetime import datetime

def first_function_execute(**context):
    print("First function executed")

def second_function_execute(**context):
    print("Second function executed") 

def third_function_execute(**context):
    print("Third function executed")

with DAG(dag_id="my_sample_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily") as dag:

    first_function = PythonOperator(task_id="first_function", python_callable=first_function_execute)

    second_function = PythonOperator(task_id="second_function", python_callable=second_function_execute)

    third_function = PythonOperator(task_id="third_function", python_callable=third_function_execute)

    first_function >> second_function >> third_function
