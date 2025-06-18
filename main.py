from src.Fifa23.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Fifa23.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.Fifa23.pipeline.data_conversion_pipeline import DataConversionPipeline
from src.Fifa23.pipeline.data_validation_pipeline import DataValidationPipeline
from src.Fifa23.pipeline.data_modeling_pipeline import DataModelingPipeline
from logs import setup_logging,logger

try:
    setup_logging()
    logger.info("Logging setup correctly in main.py file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in main.py file %s",e)


STAGE_NAME = "Data Ingestion Stage"
try :
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataTransformationPipeline()
    clean_df = obj.initiate_data_transformation()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Conversion Stage"

try:
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataConversionPipeline()
    X_train_transformed,X_test_transformed,y_train,y_test = obj.initiate_data_conversion()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Modeling Stage"

try:
    logger.info(">>>>>>>>>>>>>>>>>{%s}<<<<<<<<<<<<<<",STAGE_NAME)
    obj = DataModelingPipeline()
    xgb = obj.initiate_data_modeling()
    logger.info(">>>>>>>>>>>>>>>> STAGE {%s} COMPLETED <<<<<<<<<<<<<<<<",STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e