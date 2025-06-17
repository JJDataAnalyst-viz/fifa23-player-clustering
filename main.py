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

