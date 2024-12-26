from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import json
from pathlib import Path
from typing import Any
import base64
import os
from src.house_reg import logger
import yaml

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:

    '''reads yaml file and returns

    Args:
        path_to_yaml(str):path like input
    
    Raises:
        ValueError : if yaml file is empty
        e : empty file

    Returns:
        ConfigBox: ConfigBox type

    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except  Exception as e:
        raise e

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json
    
    Args:
        path (Path): path of json file

    Returns:
        ConfigBox : ConfigBox type
    """

    with open(path) as json_file:
        content=json.load(json_file)

    logger.info(f"json file loaded successfully from: {path}")

    return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories

    Args:
        path_to_directories(list): list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory:{path}")

@ensure_annotations
def save_json(path: Path,data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): json data to be save
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at {path}")