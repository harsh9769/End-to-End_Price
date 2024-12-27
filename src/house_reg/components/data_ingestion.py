import gdown
import zipfile
from house_reg import logger
import os
from house_reg.config.configuration import DataIngestionConfig


class DataIngestion:

    def __init__(self,config:DataIngestionConfig):
        self.config= config

    def download_file(self)->str:
        '''fetch Data from url
        '''
        try:
            dataset_url=self.config.source_url
            zip_download_dir= self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading the dataset:{dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
            gdown.download(download_url, str(zip_download_dir), quiet=False)

            logger.info(f"Downloaded Data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the data directory

        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)