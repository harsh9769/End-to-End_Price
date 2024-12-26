from src.house_reg.config.configuration import ConfigurationManager
from src.house_reg.components.data_ingestion import DataIngestion
from src.house_reg import logger

STAGE_NAME="Data Ingestion"

class DataIngestionPipeline:

    def __init__(self):
        pass

    def main(self):
        
        config= ConfigurationManager()
        data_ingestion_config= config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e