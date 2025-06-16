from src.Fifa23.components.data_ingestion import data_ingestion_files
from logs import logger,setup_logging

try:
    setup_logging()
    logger.info("Logging setup correctly in %s file",__name__)
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in %s file %s", __name__,e)



STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline():
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        data_ingestion_files()



if __name__ == "__main__":
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)