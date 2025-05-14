import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    split_ratio: float = 0.2
    random_state: int = 42

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enterd the data ingestion method")
        try:
            df = pd.read_csv('data/stud.csv')
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=self.ingestion_config.split_ratio, random_state=self.ingestion_config.random_state)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info("Ingestion of train data completed")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            raise CustomException(e, sys)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_treansformation.initiate_data_transformation(train_path, test_path)
    

