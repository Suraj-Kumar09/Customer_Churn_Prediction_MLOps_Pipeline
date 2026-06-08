import os
from customer_churn.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()



@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME


# Data validation ke liye liy jo data validation vala part add krne ke bad me ye code add krna hai 
#  Ab entity/artifact_entity me jao aur vala code add kro
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    drift_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                               DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)
    
    validation_report_file_path: str = os.path.join(data_validation_dir, "report.yaml")   




# # Path hai jo data transformation ke bad hoga 
# # Ab entity/artifact_entity me jao aur code add kro
# @dataclass
# class DataTransformationConfig:
#     data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
#     transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
#                                                     TRAIN_FILE_NAME.replace("csv", "npy"))
#     transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
#                                                    TEST_FILE_NAME.replace("csv", "npy"))
#     transformed_object_file_path: str = os.path.join(data_transformation_dir,
#                                                      DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
#                                                      PREPROCSSING_OBJECT_FILE_NAME)



# # Model trainer ka code hai jo model trainer folder ke andar banega
# # Ab entity/artifact_entity me jana hai aur code add krna hai.

# @dataclass
# class ModelTrainerConfig:
#     model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
#     trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME)
#     expected_accuracy: float = MODEL_TRAINER_EXPECTED_SCORE
#     model_config_file_path: str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH






# # Model evaluation ke liye code hai 
# # Ab entity/artifact_entity me jana hai aur code add krna hai

# @dataclass
# class ModelEvaluationConfig:
#     changed_threshold_score: float = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
#     bucket_name: str = MODEL_BUCKET_NAME
#     s3_model_key_path: str = MODEL_FILE_NAME


# # Model pusher ke liy code hai 
# # Ab entity/artifact_entity me jana hai aur code add krna hai
# @dataclass
# class ModelPusherConfig:
#     bucket_name: str = MODEL_BUCKET_NAME
#     s3_model_key_path: str = MODEL_FILE_NAME




# @dataclass
# class USvisaPredictorConfig:
#     model_file_path: str = MODEL_FILE_NAME
#     model_bucket_name: str = MODEL_BUCKET_NAME


    