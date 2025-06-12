import os
import yaml
from logs import logger, setup_logging
from box import ConfigBox
import joblib
from pathlib import Path
from typing import Any

try:
    setup_logging()
    logger.info("Logging setup correctly in common.py file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in common file %s", e)


def read_yaml(path: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path (Path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox object containing the parsed YAML content,
                   allowing attribute-style access to dictionary keys.

    """
    try:
        with open(path, "r", encoding="utf-8") as yaml_file:

            content = yaml.safe_load(yaml_file)
            logger.info("Yaml file correctly loaded!")
            return ConfigBox(content)

    except yaml.YAMLError as e:
        logger.error("Yaml wasn't loaded correctly %s", e)
    except FileNotFoundError as e:
        logger.error("File not found! %s", e)


def save_bin(data, path: Path) -> None:
    """
    Save data to a binary file using joblib.

    Args:
        data (Any): The object to be saved (e.g., model, pipeline, or dataset).
        path (Path): The file path where the .pkl file will be saved.

    Returns:
        None

    """
    try:
        joblib.dump(data, path)
        logger.info("File sucessfully loaded into %s!", path)
    except FileNotFoundError as e:
        logger.error("Directory not found %s!", e)


def load_bin(path: Path) -> Any:
    """
    Load data from binary format using joblib

    Args:
        path (Path) : The object to be loaded (e.g., model,pipeline or dataset)

    Returns :
        Any

    """
    try:
        content = joblib.load(path)
        logger.info("Content of binary file loaded sucessfully!")
        return content
    except FileNotFoundError as e:
        logger.error("Path for .pkl file was not found %s!", e)
