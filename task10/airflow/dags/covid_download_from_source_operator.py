import requests
import os
import pandas as pd
from io import StringIO 

from datetime import datetime

from airflow.models.baseoperator import BaseOperator
from custom_s3_hook import CustomS3Hook

class CovidDownloadFromSourceOperator(BaseOperator):
    def __init__(self, url: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.url = url
        self.custom_s3 = CustomS3Hook(bucket="covid")
        self.current_time = datetime.now()
        self.current_date = self.current_time .strftime("%Y-%m-%d")

    def execute(self, context):
        self.download_file()
        return self.url

    def download_file(self):
        print("Fazendo download do arquivo: " + self.url)
        r = requests.get(self.url, allow_redirects=True)
        
        self.custom_s3.put_object(key=f"datalake/{self.current_date}/{os.path.basename(self.url)}",buffer=r.content)

        