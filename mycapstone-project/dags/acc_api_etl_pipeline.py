from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

from airflow.utils import timezone
from datetime import datetime

import os
import json
import csv
import requests

from google.cloud import bigquery
from google.oauth2 import service_account

import logging
from airflow.models import Connection
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


def _get_files_api():
    api_key = "dUJUhi3y5MkxpSEhT5Xtthxan6fxxLI4"
    headers = {"api-key": api_key}
    params1 = {"resource_id": "d1ab8a36-c5f7-4efb-b613-63310054b0bc", "limit": 10000}
    params2 = {"resource_id": "5af00f52-ed10-409e-b549-cbf169f52b0d", "limit": 2500}
    params3 = {"resource_id": "5f4061d3-c9b3-455e-aa46-b04f0d85d6e2", "limit": 2500}

    response1 = requests.get("https://opend.data.go.th/get-ckan/datastore_search", params=params1, headers=headers)
    data1 = response1.json()
    records1 = data1.get("result", {}).get("records", [])
    logging.info(records1)

    response2 = requests.get("https://opend.data.go.th/get-ckan/datastore_search", params=params2, headers=headers)
    data2 = response2.json()
    records2 = data2.get("result", {}).get("records", [])
    logging.info(records2)

    response3 = requests.get("https://opend.data.go.th/get-ckan/datastore_search", params=params3, headers=headers)
    data3 = response3.json()
    records3 = data3.get("result", {}).get("records", [])
    logging.info(records3)

    # Combine records from both APIs
    all_records = records1 + records2 + records3

    # Extract date from current timestamp
    current_datetime = datetime.now().strftime("%Y-%m-%d")

    file_name = f"RoadAccident_{current_datetime}.csv"
    file_path = os.path.join("/opt/airflow/dags", file_name)

    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        # Extract field names from the first record
        fieldnames = all_records[0].keys() if all_records else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # Write the header
        writer.writeheader()
        # Write the records
        writer.writerows(all_records)

    return file_path

with DAG(
    "acc_api_etl_pipeline",
    start_date=timezone.datetime(2024, 5, 10),
    schedule="@quarterly",
    tags=["DS525"],
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    get_files_api = PythonOperator(
        task_id="get_files_api",
        python_callable=_get_files_api,
        dag=dag,
    )

    upload_to_gcs = LocalFilesystemToGCSOperator(
        task_id="upload_to_gcs",
        src=_get_files_api(),  # Using the file path generated by _get_files_api function
        dst="RoadAccident_{{ execution_date.strftime('%Y-%m-%d') }}.csv",
        bucket="swu-ds525-8888",
        gcp_conn_id="my_gcp_conn",
        dag=dag,
    )

    create_bq_raw_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_bq_raw_dataset',
        dataset_id='project_accident_raw',  # specify the dataset ID
        project_id='stalwart-summer-413911',  # specify your BigQuery project ID
        location='asia-southeast1',  # specify the location for the dataset
        gcp_conn_id='my_gcp_conn',  # specify the connection ID for GCP
        dag=dag,
    )

    load_raw_to_bq = GCSToBigQueryOperator(
        task_id='load_raw_to_bq',
        bucket='swu-ds525-8888',
        source_objects=['RoadAccident_{{ execution_date.strftime("%Y-%m-%d") }}*.csv'],  # Use wildcard pattern
        destination_project_dataset_table='stalwart-summer-413911.project_accident_raw.accident_case_original',
        source_format='CSV',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
        gcp_conn_id="my_gcp_conn",
        dag=dag,
    )

    create_bq_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_bq_dataset',
        dataset_id='project_accident',  # specify the dataset ID
        project_id='stalwart-summer-413911',  # specify your BigQuery project ID
        location='asia-southeast1',  # specify the location for the dataset
        gcp_conn_id='my_gcp_conn',  # specify the connection ID for GCP
        dag=dag,
    )

    load_to_bq = GCSToBigQueryOperator(
        task_id='load_to_bq',
        bucket='swu-ds525-8888',
        source_objects=['RoadAccident_{{ execution_date.strftime("%Y-%m-%d") }}*.csv'],  # Use wildcard pattern
        destination_project_dataset_table='stalwart-summer-413911.project_accident.accident_case_full',
        source_format='CSV',
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
        gcp_conn_id="my_gcp_conn",
        dag=dag,
    )

    follow_create_dataset = EmptyOperator(task_id='follow_create_dataset')

    table_prep_sql = f"""
    ALTER TABLE `project_accident.accident_case_full`
    DROP COLUMN _id,
    DROP COLUMN Dead_Year___________________________________________,
    DROP COLUMN Date_Rec,
    DROP COLUMN Risk_Helmet,
    DROP COLUMN Risk_Safety_Belt;

    ALTER TABLE `project_accident.accident_case_full`
    RENAME COLUMN Dead_Conso_Id TO acc_case_id,
    RENAME COLUMN DEAD_YEAR TO psn_dead_year,
    RENAME COLUMN Age TO psn_age,
    RENAME COLUMN Sex TO psn_sex,
    RENAME COLUMN Nationality_Id TO psn_nationality,
    RENAME COLUMN Tumbol TO psn_tumbol,
    RENAME COLUMN District TO psn_district,
    RENAME COLUMN Province TO psn_province,
    RENAME COLUMN Dead_Date_Final TO actual_dead_date,
    RENAME COLUMN Time_Rec TO case_time,
    RENAME COLUMN Acc_Sub_Dist TO case_tumbol,
    RENAME COLUMN Acc_Dist TO case_district,
    RENAME COLUMN ________________________________________ TO case_province,
    RENAME COLUMN Acc_La TO case_lat,
    RENAME COLUMN Acclong TO case_long,
    RENAME COLUMN Ncause TO icd_code,
    RENAME COLUMN Vehicle_Merge_Final TO vehicle_name;

    CREATE OR REPLACE TABLE `project_accident.accident_case_full_with_id` AS
    SELECT *,
       CAST(ROW_NUMBER() OVER(ORDER BY acc_case_id) AS STRING) AS personal_id
    FROM `project_accident.accident_case_full`;

    DROP TABLE `project_accident.accident_case_full`;

    ALTER TABLE `project_accident.accident_case_full_with_id`
    RENAME TO `accident_case_full`;
    """

    create_case_sql = f"""
    CREATE TABLE `project_accident.case_info`
    PARTITION BY DATE(actual_dead_date)
    AS (
        SELECT 
            acc_case_id, 
            actual_dead_date, 
            case_time, 
            case_tumbol, 
            case_district, 
            case_province,
            case_lat,
            case_long,
            icd_code,
            personal_id,
        FROM `project_accident.accident_case_full`
    );
    """
    
    create_person_sql = f"""
    CREATE OR REPLACE TABLE `project_accident.personal_info`
    PARTITION BY RANGE_BUCKET(psn_dead_year, GENERATE_ARRAY(2000, 2050, 1))
    AS (
        SELECT 
            personal_id,
            psn_dead_year, 
            psn_age, 
            psn_sex, 
            psn_nationality, 
            psn_tumbol, 
            psn_district,
            psn_province,
        FROM `project_accident.accident_case_full`
    );
    """

    create_vehicle_sql = f"""
    CREATE OR REPLACE TABLE `project_accident.vehicle_info`
    AS (
        SELECT 
            icd_code,
            vehicle_name, 
        FROM `project_accident.accident_case_full`
    );
    """

    table_prep = BigQueryExecuteQueryOperator(
        task_id='table_prep_sql',
        sql=table_prep_sql,
        use_legacy_sql=False,
        gcp_conn_id='my_gcp_conn',
        dag=dag,
    )

    create_case_table = BigQueryExecuteQueryOperator(
        task_id='create_case_table',
        sql=create_case_sql,
        use_legacy_sql=False,
        gcp_conn_id='my_gcp_conn',
        dag=dag,
    )

    create_person_table = BigQueryExecuteQueryOperator(
        task_id='create_person_table',
        sql=create_person_sql,
        use_legacy_sql=False,
        gcp_conn_id='my_gcp_conn',
        dag=dag,
    )

    create_vehicle_table = BigQueryExecuteQueryOperator(
        task_id='create_vehicle_table',
        sql=create_vehicle_sql,
        use_legacy_sql=False,
        gcp_conn_id='my_gcp_conn',
        dag=dag,
    )

    start >> get_files_api >> upload_to_gcs >> [create_bq_raw_dataset, create_bq_dataset] >> follow_create_dataset >> [load_to_bq, load_raw_to_bq] >> table_prep >> [create_case_table, create_person_table, create_vehicle_table] >> end