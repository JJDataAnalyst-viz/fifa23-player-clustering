import os
import yaml
from logs import logger,setup_logging
from box import ConfigBox
import joblib
from pathlib import Path

try:
    setup_logging()
    logger.info("Logging setup correctly in common.py file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_ingestion file %s", e)

def read_yaml(path : Path) -> ConfigBox:
    '''  Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path (Path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox object containing the parsed YAML content, 
                   allowing attribute-style access to dictionary keys.
    
    '''
    try:
        with open(path,"r",encoding="utf-8") as yaml_file:

            content = yaml.safe_load(yaml_file)
            logger.info("Yaml file correctly loaded!")
            return ConfigBox(content)
        
    except yaml.YAMLError as e:
        logger.error("Yaml wasn't loaded correctly %s",e)
    except FileNotFoundError as e:
        logger.error("File not found! %s",e)

def save_bin(data,path : Path):
    joblib.dump(data,path)



def load_bin(path):
    return joblib.load(path)