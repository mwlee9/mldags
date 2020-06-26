from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
from airflow import AirflowException

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'mathew',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 2),
    'email': 'mwlee9@gmail.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Helloworld', default_args=default_args)

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(
    task_id='task_1',
    bash_command='exit 123',
    dag=dag)


t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello World from Task 2"',
    dag=dag)


t2.set_upstream(t1)