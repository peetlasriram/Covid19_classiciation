import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any
import base64
from Classification import logger

#1 read yaml file
@ensure_annotations
def read_yaml_file(path_to_yaml:Path)->config_box:
    try:
        with open(path_to_yaml)as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file{path_to_yaml}loaded successfully")
            return config_box(content)
    except BoxValueError:
        raise ValueError("yaml file empty")
    except Exception as e:
        raise e

@ensure_annotations
def creating_dir(path_to_dir:list,verbose= True):
    for file in path_to_dir:
        os.makedirs(file, exist_ok=True)
        if verbose:
            logger.info(f"creating directory{file}")
            
@ensure_annotations
def savejson(path:Path,data:dict):
    
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
        logger.info(f"json file saved at{path}")
        
@ensure_annotations
def load_json(path:Path)->config_box:
    with open(path) as f:
        content=json.load(f)
        logger.info(f"json file successfully from:{path}")
        return config_box(content)
@ensure_annotations
def save_bin(data:Any,path:Path):
    with open(path, "wb") as f:
        joblib.dump(data, f)
        logger.info(f"binary file saved at{path}")
@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

    