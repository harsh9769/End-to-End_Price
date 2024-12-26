from src.house_reg.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from src.house_reg.pipelines.stage_02_prepare_train_model import PrepareTrainModelPipeline
from src.house_reg.pipelines.stage_03_model_evaluation import ModelEvaluationPipeline

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
    
STAGE_NAME="Prepare Train Model"

if __name__=="__main__":

    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=PrepareTrainModelPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Model Evaluation"

if __name__=="__main__":

    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    