from house_reg._utils.common import read_yaml,create_directories
from house_reg.constant import *
from house_reg.entity.config_entity import (DataIngestionConfig,PrepareTrainModelConfig,EvaluationConfig)
import os
                                                
class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_PATH, params_file_path=PARAMS_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        dataingestionconfig = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=str(config.source_url),
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return dataingestionconfig

    def get_train_model_config(self)->PrepareTrainModelConfig:
        config=self.config.prepare_base_model
        os.makedirs(config.root_dir,exist_ok=True)

        prepare_train_model=PrepareTrainModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path)
        )

        return prepare_train_model
    
    def get_evaluation_config(self)-> EvaluationConfig:

        eval_config=EvaluationConfig(
            path_of_model="artifacts\prepare_base_model\model.pkl",
            training_data="artifacts\data_ingestion\Housing.csv",
            mlflow_uri="https://dagshub.com/harsh9769/End-to-End_Price.mlflow")
        
        return eval_config
    
    
    
