import os
from datetime import date

# Basic Configuration
DATABASE_NAME = "Churn_Prediction"
COLLECTION_NAME = "Churn_data"
MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "customer_churn"
ARTIFACT_DIR: str = "artifact"

# File Constants
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
FILE_NAME: str = "customer_churn.csv"
MODEL_FILE_NAME = "model.pkl"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
MODEL_CONFIG_FILE_PATH = os.path.join("config", "model.yaml")
CONFIG_FILE_PATH = os.path.join("config", "model.yaml")

# Target Column Configuration (Notebook ke hisaab se)
TARGET_COLUMN = "Churn Label"
CURRENT_YEAR = date.today().year

# AWS Constants (Model Evaluation & Pusher)
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME: str = "Churn_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# Data Validation Constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

# Data Transformation Constants
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# Model Trainer Constants
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

# Model Evaluation Constants
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "customer_churn-model20026"
MODEL_PUSHER_S3_KEY = "model-registry"

# App Constants
APP_HOST = "0.0.0.0"
APP_PORT = 9090