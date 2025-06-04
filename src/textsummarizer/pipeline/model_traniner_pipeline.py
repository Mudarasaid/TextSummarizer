from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.model_trainer import ModelTrainer, AutoModelForSeq2SeqLM
from src.textsummarizer.logging import logger 

class ModelTrainerPileline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_data_trainer_config()
        model_tranier= ModelTrainer(config=model_trainer_config)
        #data_transformation.convert_examples_to_features()
        model_tranier.train()