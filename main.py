from src.house_reg.pipelines.stage_01_data_ingestion import DataIngestionPipeline

from src.house_reg import logger

STAGE_NAME="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e