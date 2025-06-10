from logs import setup_logging, logger
import yaml 


setup_logging()

with open("config/config.yaml","r") as file:
    conent = yaml.safe_load(file)["data_ingestion"]
    logger.info("Data Ingestion paths load from config_yaml")




