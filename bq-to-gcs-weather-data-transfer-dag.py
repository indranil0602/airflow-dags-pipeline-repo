from socket import timeout
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.bigquery_to_gcs import BigQueryToGCSOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from datetime import datetime, timedelta

def _print_func():
	print("Hello world")

args = {
	'owner':'Indranil Pal',
	'start_date':datetime(2022, 7, 19),
	'retry':1,
	'retry_delay':timedelta(seconds=10)
}

with DAG('bq-to-gcs-weather-data-transfer-dag', default_args=args, schedule_interval=None, catchup=False) as dag:
	
    start_task=BashOperator(
        task_id='start_task',
        bash_command='echo "DAG has been started"'
    )
    check_gcs_object_task=GCSObjectExistenceSensor(
        task_id = 'check_gcs_object_task',
        bucket = 'weather-dataflow-destination-bucket',
        object = 'daily-weather-data.csv',
        google_cloud_conn_id = 'google_cloud_default',
        mode = 'poke',
        poke_interval = 10,
        timeout = 30
    )
    transfer_task=BigQueryToGCSOperator(
        task_id = 'transfer_task',
        source_project_dataset_table = 'modern-impulse-355015.transformed_weather_data.weather-data-daily',
        destination_cloud_storage_uris = 'gs://weather-dataflow-destination-bucket/daily-weather-data.csv',
        project_id = 'modern-impulse-355015',
        compression = 'NONE',
        export_format = 'CSV',
        field_delimiter = ',',
        print_header = True,
        gcp_conn_id = 'google_cloud_default',
    )
    print_task=PythonOperator(
        task_id='print_task',
        python_callable=_print_func
    )

    start_task >> check_gcs_object_task >> transfer_task >> print_task
