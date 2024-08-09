from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore
from airflow.utils.dates import days_ago # type: ignore
# Importing the task function
from extraction.extract_pollution_data import extract_antananarivo_pollution, extract_losangeles_pollution, extract_paris_pollution, extract_tokyo_pollution, extract_nairobi_pollution, extract_lima_pollution
from extraction.extract_local_file import extract_from_demographic_files, extract_from_geographic_file
from transformation.transform_pollutions import get_all_pollutions_data
from loading.load_data import load_demographic_and_pollutions_in_database, load_geographic_and_pollutions_in_database, load_all_datas, aqi_per_location

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'pollution_dag',
    default_args=default_args,
    description='An Air Pollution ETL DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# Define the tasks
extract_antananarivo_pollution = PythonOperator(
    task_id='extract_antananarivo_pollution',
    python_callable=extract_antananarivo_pollution,
    dag=dag,
)

extract_losangeles_pollution = PythonOperator(
    task_id='extract_losangeles_pollution',
    python_callable=extract_losangeles_pollution,
    dag=dag,
)

extract_paris_pollution = PythonOperator(
    task_id='extract_paris_pollution',
    python_callable=extract_paris_pollution,
    dag=dag,
)

extract_tokyo_pollution = PythonOperator(
    task_id='extract_tokyo_pollution',
    python_callable=extract_tokyo_pollution,
    dag=dag,
)

extract_nairobi_pollution = PythonOperator(
    task_id='extract_nairobi_pollution',
    python_callable=extract_nairobi_pollution,
    dag=dag,
)

extract_lima_pollution = PythonOperator(
    task_id='extract_lima_pollution',
    python_callable=extract_lima_pollution,
    dag=dag,
)

extract_from_demographic_files = PythonOperator(
    task_id='extract_from_demographic_files',
    python_callable=extract_from_demographic_files,
    dag=dag,
)

extract_from_geographic_files = PythonOperator(
    task_id='extract_from_geographic_files',
    python_callable=extract_from_geographic_file,
    dag=dag,
)

transform_all = PythonOperator(
    task_id='transform_all',
    python_callable=get_all_pollutions_data,
    dag=dag,
)

load_demographic_and_pollutions = PythonOperator(
    task_id='load_demographic_and_pollutions',
    python_callable=load_demographic_and_pollutions_in_database,
    dag=dag,
)

load_geographic_and_pollutions = PythonOperator(
    task_id='load_geographic_and_pollutions',
    python_callable=load_geographic_and_pollutions_in_database,
    dag=dag,
)

load_all = PythonOperator(
    task_id='load_all',
    python_callable=load_all_datas,
    dag=dag,
)

load_aqi = PythonOperator(
    task_id='load_aqi',
    python_callable=aqi_per_location,
    dag=dag,
)
# Set the task dependencies
[extract_antananarivo_pollution, extract_losangeles_pollution, extract_paris_pollution, extract_tokyo_pollution, extract_nairobi_pollution, extract_lima_pollution, extract_from_demographic_files, extract_from_geographic_files] >>  transform_all >> [load_demographic_and_pollutions, load_geographic_and_pollutions, load_all]