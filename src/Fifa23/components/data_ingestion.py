from logs import setup_logging, logger
import yaml 
import kagglehub
import shutil
import os

setup_logging()



with open("config/config.yaml","r") as file:
    content = yaml.safe_load(file)["data_ingestion"]
    logger.info("Data Ingestion paths load from config_yaml")


def data_ingestion():
    path = load_data_from_kaggle(content["source_URL"])
    move_data(path)

def load_data_from_kaggle(source):
    path = kagglehub.dataset_download(source)
    print(f"Path for dataset : {path}")
    return path


def move_data(path):
    os.makedirs("data/raw", exist_ok=True)

    shutil.move(
            path,
            "data/raw",
        )

if __name__ == "__main__":
    data_ingestion()