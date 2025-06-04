from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_transformation import DataTransformation
from src.textsummarizer.logging import logger 

class DataTransformationPileline:
    def __init__(self):
        pass
    def initiate_data_Transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation= DataTransformation(config=data_transformation_config)
        #data_transformation.convert_examples_to_features()
        data_transformation.convert()
        
    