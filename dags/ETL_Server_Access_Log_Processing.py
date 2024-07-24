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
    'owner': 'ETL',
    'start_date': days_ago(0),
    'email': ['test@test.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL-download',
    default_args=default_args,
    description='ETL Download DAG',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task

download = BashOperator(
    task_id='download',
    bash_command='curl "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt" -o /home/airflow/web-server-access-log.txt',
    dag=dag,
)

# define the second task
extract = BashOperator(
    task_id='extract',
    bash_command='cut -f1,4 -d"#" /home/airflow/web-server-access-log.txt > /home/airflow/extracted.txt',
    dag=dag,
)

transform = BashOperator(
    task_id='transform',
    bash_command='tr "[a-z]" "[A-Z]" < /home/airflow/extracted.txt > /home/airflow/capitalized.txt',
    dag=dag,
)

load = BashOperator(
    task_id='load',
    bash_command='zip log.zip /home/airflow/capitalized.txt' ,
    dag=dag,
)
# task pipeline
download >> extract >> transform >> load
