from src.house_reg._utils.common import read_yaml,create_directories
from src.house_reg.constant import *
from src.house_reg.entity.config_entity import DataIngestionConfig

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
    
    
    
