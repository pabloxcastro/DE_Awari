import os
from airflow import DAG
from datetime import datetime

from covid_download_from_source_operator import CovidDownloadFromSourceOperator

URLS_COVID = {
   'covid_codebook': 'https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-codebook.csv'
}


dag1 =  DAG(dag_id=f"ingest_covid_codebook_dag",start_date=datetime(2021,1,1),schedule_interval=None, catchup=False)
      
download_task = CovidDownloadFromSourceOperator(
   task_id=f"download_{os.path.basename(URLS_COVID['covid_codebook'])}", url=URLS_COVID['covid_codebook'],dag=dag1
)

# TASKS
download_task
