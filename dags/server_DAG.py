# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'fraud_detector',
    'start_date': days_ago(0),
    'email': ['test@test.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_Fraud',
    default_args=default_args,
    description='ETL Download DAG',
    schedule_interval=timedelta(minutes=5),
)

# define the tasks

# define the first task

database_connection = BashOperator(
    task_id='database_connection',
    bash_command='echo "database_connection"',
    dag=dag,
)

# define the second task
gRPC_connection = BashOperator(
    task_id='gRPC_connection',
    bash_command='echo "gRPC_connection"',
    dag=dag,
)


# task pipeline
database_connection >> gRPC_connection
