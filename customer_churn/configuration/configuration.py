import os
from customer_churn.constants import *
from customer_churn.utils.main_utils import read_yaml
from customer_churn.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        # TIMESTAMP HATAYA - Ye static path ban gaya hai
        self.artifact_root = "artifact" 
        os.makedirs(self.artifact_root, exist_ok=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion'] 
        
        dir_path = os.path.join(self.artifact_root, "data_ingestion")
        os.makedirs(dir_path, exist_ok=True)
        
        return DataIngestionConfig(
            collection_name=config['collection_name'],
            feature_store_file_path=os.path.join(dir_path, "churn.csv"),
            training_file_path=os.path.join(dir_path, "train.csv"),
            testing_file_path=os.path.join(dir_path, "test.csv"),
            train_test_split_ratio=config['train_test_split_ratio']
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        dir_path = os.path.join(self.artifact_root, "data_validation")
        os.makedirs(dir_path, exist_ok=True)
        
        return DataValidationConfig(
            data_validation_dir=dir_path,
            validation_report_file_path=os.path.join(dir_path, "report.yaml")
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        dir_path = os.path.join(self.artifact_root, "data_transformation")
        os.makedirs(dir_path, exist_ok=True)
        
        return DataTransformationConfig(
            data_transformation_dir=dir_path,
            transformed_train_file_path=os.path.join(dir_path, "train.npy"),
            transformed_test_file_path=os.path.join(dir_path, "test.npy"),
            transformed_object_file_path=os.path.join(dir_path, "preprocessing.pkl")
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config['model_trainer']
        dir_path = os.path.join(self.artifact_root, "model_trainer")
        os.makedirs(dir_path, exist_ok=True)
        
        return ModelTrainerConfig(
            trained_model_file_path=os.path.join(dir_path, "trained_model", "model.pkl"),
            expected_accuracy=config['expected_accuracy']
        )





# from customer_churn.entity.config_entity import DataValidationConfig


# def get_data_validation_config(self) -> DataValidationConfig:
#     data_validation_dir = os.path.join(self.training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    
#     data_validation_config = DataValidationConfig(
#         data_validation_dir=data_validation_dir,
#         drift_report_file_path=os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR, DATA_VALIDATION_DRIFT_REPORT_FILE_NAME),
#         validation_report_file_path=os.path.join(data_validation_dir, "report.yaml") 
#     )
#     return data_validation_config