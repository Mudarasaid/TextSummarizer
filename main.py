from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionPileline
from src.textsummarizer.pipeline.data_transformation_pipeline import DataTransformationPileline
from src.textsummarizer.pipeline.model_traniner_pipeline import ModelTrainerPileline
STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionPileline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationPileline()
    data_transformation_pipeline.initiate_data_Transformation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_training_pipeline=ModelTrainerPileline()
    model_training_pipeline.initiate_model_trainer()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



        