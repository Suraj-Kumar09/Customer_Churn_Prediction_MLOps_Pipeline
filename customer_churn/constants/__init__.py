import os
from datetime import date

DATABASE_NAME = "Churn_Prediction"

COLLECTION_NAME = "Churn_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "customer_churn"
ARTIFACT_DIR: str = "artifact"


TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "customer_churn.csv"
MODEL_FILE_NAME = "model.pkl"

#  Schema file ka code likhe ke bad me ye constant add krna hai
TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")



#  model evaluation aur model pusher ke liye constant hai jo ki model evaluation me change.
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"



"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Churn_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



# Data validation ke liye constant hai jo ki shema file update krne ke bad me add krna hai 
# ye code run krne ke bad artifact folder ke andar data_validation folder create hoga jisme drift_report folder hoga aur usme report.file create hoga 

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"



# Artifact folder ke andar data_transformation folder create hoga jisme transformation folder create hoga jisme tranformed aur transformed_object file bange 
# Ab entity/config_entity jana hai aur code likha hai uske bad entity/artifact_entity file me jana hai aur code likhna hai  folder me jana hai aur 
"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"




# Artifact folder ke andar model_trainer folder create hoga,  aur trained_model folder banega aur uske andarmodel.pkl file create hoga
# ab entity/config_entity file me jana hai aur code likhna hai uske bad entity/artifact_entity file me jana hai aur code likhna hai 

"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")



#  Model evaluation ke liye constant hai jo model ko evaluate krega.
"""
MODEL EVALUATION related constant 
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "customer_churn-model20026"
MODEL_PUSHER_S3_KEY = "model-registry"

# Model ko S3 bucket me push krne ke bad esko run karenge apne local host me 
APP_HOST = "0.0.0.0"
APP_PORT = 9090