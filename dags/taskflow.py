# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.operators.python import PythonOperator
# import random
 
# def generate_random_number(**context):
#     ti = context['ti']
#     number = random.randint(1, 100)
#     ti.xcom_push(key='random_number', value=number)
#     print(f"Generated random number: {number}")
 
# def check_even_odd(**context):
#     ti = context['ti']
#     number = ti.xcom_pull(task_ids='generate_number', key='random_number')
#     result = "even" if number % 2 == 0 else "odd"
#     print(f"The number {number} is {result}.")
 
# with DAG(
#     'random_number_checker',
#     start_date=datetime(2024, 1, 1),
#     schedule="@daily",
#     description='A simple DAG to generate and check random numbers',
#     catchup=False
# ) as dag:
 
#     generate_task = PythonOperator(
#         task_id='generate_number',
#         python_callable=generate_random_number,
#     )
 
#     check_task = PythonOperator(
#         task_id='check_even_odd',
#         python_callable=check_even_odd,
#     )
 
#     generate_task >> check_task 

# Transform dag 

from airflow.decorators import dag, task 
from datetime import datetime, timedelta
import random

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    description='A simple DAG to generate and check random numbers',
    catchup=False, 
    tags=['rand_num_check']
) 

def random_number_checker_taskflow(): 
    
    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number
    
    @task
    def check_even_odd(number: int):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")
 
    check_even_odd(generate_random_number())

random_number_checker_taskflow()