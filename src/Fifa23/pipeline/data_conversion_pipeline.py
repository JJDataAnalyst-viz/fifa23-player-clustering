from src.Fifa23.components.data_conversion import splitter
from logs import logger,setup_logging

try:
    setup_logging()
    logger.info("Logging setup correctly in data_conversion_pipeline file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_conversion_pipeline file %s",e)



STAGE_NAME = "Data Conversion Stage"

class DataConversionPipeline():
    def __init__(self):
        pass
    def initiate_data_conversion(self):
        return splitter(False)



if __name__ == "__main__":
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataConversionPipeline()
    X_train_transformed,X_test_transformed,y_train,y_test = obj.initiate_data_conversion()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)