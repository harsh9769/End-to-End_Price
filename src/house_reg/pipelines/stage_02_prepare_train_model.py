from src.house_reg.components.prepare_train_model import PrepareTrainModel
from src.house_reg.config.configuration import ConfigurationManager
from src.house_reg import logger

STAGE_NAME="Prepare Train Model"

class PrepareTrainModelPipeline:

    def __init__(self):
        pass

    def main(self):

        config=ConfigurationManager()
        prepare_train_config=config.get_train_model_config()
        prepare_train=PrepareTrainModel(config=prepare_train_config)
        prepare_train.data_set()
        prepare_train.train_model()

if __name__=="__main__":

    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj=PrepareTrainModelPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e




