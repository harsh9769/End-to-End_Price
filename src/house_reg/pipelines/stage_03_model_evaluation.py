from src.house_reg.components.model_evaluation import Evaluation
from src.house_reg.config.configuration import ConfigurationManager
from src.house_reg import logger

STAGE_NAME="Model Evaluation"

class ModelEvaluationPipeline:

    def __init__(self):
        
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__=="__main__":

    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e