import sys
import os
import json
import pandas as pd
from pandas import DataFrame
from customer_churn.exception import ChurnException
from customer_churn.logger import logging
from customer_churn.utils.main_utils import read_yaml_file
from customer_churn.entity.artifact_entity import DataValidationArtifact
from customer_churn.entity.config_entity import DataValidationConfig
from customer_churn.constants import SCHEMA_FILE_PATH
from customer_churn.configuration.configuration import ConfigurationManager

class DataValidation:
    def __init__(self):
        try:
            # ConfigurationManager se static path config lo
            config_manager = ConfigurationManager()
            self.data_validation_config = config_manager.get_data_validation_config()
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise ChurnException(e, sys)

    def validate_number_of_columns(self, dataframe: DataFrame) -> bool:
        try:
            status = len(dataframe.columns) == len(self._schema_config["columns"])
            logging.info(f"Is required column present: [{status}]")
            return status
        except Exception as e:
            raise ChurnException(e, sys)

    def is_column_exist(self, df: DataFrame) -> bool:
        try:
            dataframe_columns = df.columns
            missing_numerical_columns = [col for col in self._schema_config["numerical_columns"] if col not in dataframe_columns]
            missing_categorical_columns = [col for col in self._schema_config["categorical_columns"] if col not in dataframe_columns]

            if len(missing_numerical_columns) > 0: logging.info(f"Missing numerical: {missing_numerical_columns}")
            if len(missing_categorical_columns) > 0: logging.info(f"Missing categorical: {missing_categorical_columns}")

            return False if len(missing_categorical_columns) > 0 or len(missing_numerical_columns) > 0 else True
        except Exception as e:
            raise ChurnException(e, sys) from e

    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise ChurnException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            logging.info("Starting data validation")
            # DVC path se direct read (fixed paths)
            train_df = DataValidation.read_data("artifact/data_ingestion/train.csv")
            test_df = DataValidation.read_data("artifact/data_ingestion/test.csv")

            validation_error_msg = ""
            
            # Validation Logic
            for df, name in [(train_df, "training"), (test_df, "testing")]:
                if not self.validate_number_of_columns(df):
                    validation_error_msg += f"Columns missing in {name} dataframe. "
                if not self.is_column_exist(df):
                    validation_error_msg += f"Schema mismatch in {name} dataframe. "

            validation_status = len(validation_error_msg) == 0

            # Artifact Save
            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                message="Data validation successful" if validation_status else validation_error_msg,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
                validation_report_file_path=self.data_validation_config.validation_report_file_path
            )

            # JSON Report save
            os.makedirs(os.path.dirname(self.data_validation_config.validation_report_file_path), exist_ok=True)
            with open(self.data_validation_config.validation_report_file_path, "w") as report_file:
                json.dump({"validation_status": validation_status, "message": validation_error_msg.strip()}, report_file, indent=4)

            logging.info(f"Validation artifact: {data_validation_artifact}")
            return data_validation_artifact

        except Exception as e:
            raise ChurnException(e, sys) from e

if __name__ == "__main__":
    try:
        validator = DataValidation()
        validator.initiate_data_validation()
        print("Data Validation pipeline execution completed successfully.")
    except Exception as e:
        print(f"Data Validation failed: {e}")
        sys.exit(1)





# import json
# import sys
# import os

# import pandas as pd

# from pandas import DataFrame

# from customer_churn.exception import ChurnException
# from customer_churn.logger import logging
# from customer_churn.utils.main_utils import read_yaml_file # utils folder ke andar main_utils file ke andar hm read funtion ko define kiya tha to us read funtion ke help se hm cobfig folder ke andar schema.yaml code ko read kr raahe hai.
# from customer_churn.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
# from customer_churn.entity.config_entity import DataValidationConfig
# from customer_churn.constants import SCHEMA_FILE_PATH


# class DataValidation:
#     def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
#         """
#         :param data_ingestion_artifact: Output reference of data ingestion artifact stage
#         :param data_validation_config: configuration for data validation
#         """
#         try:
#             self.data_ingestion_artifact = data_ingestion_artifact
#             self.data_validation_config = data_validation_config
#             self._schema_config =read_yaml_file(file_path=SCHEMA_FILE_PATH)
#         except Exception as e:
#             raise ChurnException(e,sys)

#     def validate_number_of_columns(self, dataframe: DataFrame) -> bool:
#         """
#         Method Name :   validate_number_of_columns
#         Description :   This method validates the number of columns
        
#         Output      :   Returns bool value based on validation results
#         On Failure  :   Write an exception log and then raise an exception
#         """
#         try:
#             status = len(dataframe.columns) == len(self._schema_config["columns"])
#             logging.info(f"Is required column present: [{status}]")
#             return status
#         except Exception as e:
#             raise ChurnException(e, sys)

#     def is_column_exist(self, df: DataFrame) -> bool:
#         """
#         Method Name :   is_column_exist
#         Description :   This method validates the existence of a numerical and categorical columns
        
#         Output      :   Returns bool value based on validation results
#         On Failure  :   Write an exception log and then raise an exception
#         """
#         try:
#             dataframe_columns = df.columns
#             missing_numerical_columns = []
#             missing_categorical_columns = []
#             for column in self._schema_config["numerical_columns"]:
#                 if column not in dataframe_columns:
#                     missing_numerical_columns.append(column)

#             if len(missing_numerical_columns)>0:
#                 logging.info(f"Missing numerical column: {missing_numerical_columns}")


#             for column in self._schema_config["categorical_columns"]:
#                 if column not in dataframe_columns:
#                     missing_categorical_columns.append(column)

#             if len(missing_categorical_columns)>0:
#                 logging.info(f"Missing categorical column: {missing_categorical_columns}")

#             return False if len(missing_categorical_columns)>0 or len(missing_numerical_columns)>0 else True
#         except Exception as e:
#             raise ChurnException(e, sys) from e

#     @staticmethod
#     def read_data(file_path) -> DataFrame:
#         try:
#             return pd.read_csv(file_path)
#         except Exception as e:
#             raise ChurnException(e, sys)
        

#     def initiate_data_validation(self) -> DataValidationArtifact:
#         """
#         Method Name :   initiate_data_validation
#         Description :   This method initiates the data validation component for the pipeline
        
#         Output      :   Returns bool value based on validation results
#         On Failure  :   Write an exception log and then raise an exception
#         """

#         try:
#             validation_error_msg = ""
#             logging.info("Starting data validation")
#             train_df, test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
#                                  DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))

#             # Checking col len of dataframe for train/test df
#             status = self.validate_number_of_columns(dataframe=train_df)
#             if not status:
#                 validation_error_msg += f"Columns are missing in training dataframe. "
#             else:
#                 logging.info(f"All required columns present in training dataframe: {status}")

#             status = self.validate_number_of_columns(dataframe=test_df)
#             if not status:
#                 validation_error_msg += f"Columns are missing in test dataframe. "
#             else:
#                 logging.info(f"All required columns present in testing dataframe: {status}")

#             # Validating col dtype for train/test df
#             status = self.is_column_exist(df=train_df)
#             if not status:
#                 validation_error_msg += f"Columns are missing in training dataframe. "
#             else:
#                 logging.info(f"All categorical/int columns present in training dataframe: {status}")

#             status = self.is_column_exist(df=test_df)
#             if not status:
#                 validation_error_msg += f"Columns are missing in test dataframe."
#             else:
#                 logging.info(f"All categorical/int columns present in testing dataframe: {status}")

#             validation_status = len(validation_error_msg) == 0

#             data_validation_artifact = DataValidationArtifact(
#                 validation_status=validation_status,
#                 message="Data validation successful",
#                 drift_report_file_path=self.data_validation_config.drift_report_file_path,
#                 validation_report_file_path=self.data_validation_config.validation_report_file_path
#             )

#             # Ensure the directory for validation_report_file_path exists
#             report_dir = os.path.dirname(self.data_validation_config.validation_report_file_path)
#             os.makedirs(report_dir, exist_ok=True)

#             # Save validation status and message to a JSON file
#             validation_report = {
#                 "validation_status": validation_status,
#                 "message": validation_error_msg.strip()
#             }

#             with open(self.data_validation_config.validation_report_file_path, "w") as report_file:
#                 json.dump(validation_report, report_file, indent=4)

#             logging.info("Data validation artifact created and saved to JSON file.")
#             logging.info(f"Data validation artifact: {data_validation_artifact}")
#             return data_validation_artifact
#         except Exception as e:
#             raise ChurnException(e, sys) from e