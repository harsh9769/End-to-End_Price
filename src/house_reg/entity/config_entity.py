from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareTrainModelConfig:
    root_dir: Path
    base_model_path:Path

from dataclasses import dataclass
@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    mlflow_uri: str