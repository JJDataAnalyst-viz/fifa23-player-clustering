from src.Fifa23.components.data_transformation import data_transform_df
from logs import logger,setup_logging

try:
    setup_logging()
    logger.info("Logging setup correctly in data_transformation_pipeline file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_transformation_pipeline file %s",e)

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline():
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        return data_transform_df()



if __name__ == "__main__":
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataTransformationPipeline()
    clean_df = obj.initiate_data_transformation()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)