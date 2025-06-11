import shutil
import os
from pathlib import Path
from typing import Optional
import yaml
import kagglehub
from logs import setup_logging, logger
from ..constants import CONFIG_FILE_PATH


try:
    setup_logging()
    logger.info("Logging setup correctly in data_ingestion file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_ingestion file %s", e)

try:
    with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as config_file:
        content = yaml.safe_load(config_file)["data_ingestion"]
        logger.info("Data Ingestion paths load from config_yaml")
except yaml.YAMLError as e:
    logger.error("File config.yaml found error %s", e)
except FileNotFoundError as e:
    logger.error("config.yaml file not found %s", e)
except Exception as e:
    logger.error(
        "Unexpected errorduring opening config.yaml in data_ingestion file %s", e
    )


def data_ingestion() -> None:
    """
    Run data loading from Kaggle and move the dataset into 'data/raw' folder.

    Returns :
       None

    """
    try:
        path = load_data_from_kaggle(content["source_URL"])
        if path is None:
            logger.error("Path was not found in config file")
            return
        logger.info("Local path for dataset: %s ", path)
        move_data(path)
        logger.info("Data was moved")
    except FileNotFoundError as e:
        logger.error("File was not found! %s", e)
    except Exception as e:
        logger.error("Unexpected error during data ingestion : %s", e)


def load_data_from_kaggle(source: Path) -> Optional[Path]:
    """
    Load dataset from Kaggle, e.g. 'bryanb/fifa-player-stats-database'.

     Args:
         source (Path): Path or identifier for the Kaggle dataset.

     Returns:
         Optional[Path]: Local path to the downloaded dataset, or None if loading failed.
    """

    try:
        path = kagglehub.dataset_download(Path(source))
        logger.info("Path for dataset : %s", path)
        return path
    except ConnectionError as e:
        logger.error("Connection was lost %s", e)
        return None
    except ConnectionRefusedError as e:
        logger.error("Connection refused %s", e)
        return None


def move_data(path: Path) -> None:
    """
    Moves a dataset from a given local path to the 'data/raw' directory.

    If the subdirectory 'data/raw/35' does not exist, the dataset is moved
    to 'data/raw'. If the directory already exists, the file will not be moved.

    Args:
        path (Path): Local path to the dataset to be moved.

    Returns:
        None
    """
    raw_folder = Path("data/raw")

    os.makedirs(raw_folder, exist_ok=True)
    try:
        if not os.path.exists("data/raw/35"):

            shutil.move(
                Path(path),
                "data/raw",
            )
            logger.info("Path was moved to data/raw/35")
    except FileNotFoundError as e:
        logger.error("File was not found %s", e)
    except OSError as e:
        logger.error("Other error related to OS System %s", e)
    except PermissionError as e:
        logger.error("Permission denied %s", e)


if __name__ == "__main__":
    data_ingestion()
