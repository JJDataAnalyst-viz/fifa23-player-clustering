from src.Fifa23.components.data_modeling import XgboostModel
import wandb
from logs import logger,setup_logging
from src.Fifa23.utils.common import read_yaml
from src.Fifa23.constants import PARAMS_FILE_PATH

try:
    setup_logging()
    logger.info("Logging setup correctly in data_conversion_pipeline file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_conversion_pipeline file %s",e)


STAGE_NAME = "Data Modeling Stage"

class DataModelingPipeline():
    def __init__(self):
        self.model = XgboostModel()
        
    def initiate_data_modeling(self):
        return self.model.xgboost_user()


if __name__ == "__main__":
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataModelingPipeline()
    xgb = obj.initiate_data_modeling()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)