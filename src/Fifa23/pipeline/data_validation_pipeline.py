from src.Fifa23.components.data_validation import Validator
from logs import logger,setup_logging

try:
    setup_logging()
    logger.info("Logging setup correctly in data_conversion_pipeline file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_conversion_pipeline file %s",e)



STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline():
    def __init__(self):
        self.obj = Validator()
  
    def initiate_data_validation(self):
        return self.obj.validate_data()



if __name__ == "__main__":
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)