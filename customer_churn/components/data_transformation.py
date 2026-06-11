import sys
import numpy as np
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from customer_churn.constants import TARGET_COLUMN, SCHEMA_FILE_PATH
from customer_churn.entity.config_entity import DataTransformationConfig
from customer_churn.entity.artifact_entity import DataTransformationArtifact
from customer_churn.exception import ChurnException
from customer_churn.logger import logging
from customer_churn.utils.main_utils import (
    save_object,
    save_numpy_array_data,
    read_yaml_file
)
from customer_churn.configuration.configuration import ConfigurationManager

class DataTransformation:
    def __init__(self):
        try:
            # ConfigurationManager se config fetch karein
            config_manager = ConfigurationManager()
            self.data_transformation_config = config_manager.get_data_transformation_config()
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise ChurnException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise ChurnException(e, sys)

    def get_data_transformer_object(self) -> Pipeline:
        try:
            num_features = self._schema_config["num_features"]
            cat_features = self._schema_config["oh_columns"] 

            numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
            categorical_transformer = Pipeline(steps=[
                ("encoder", OneHotEncoder(handle_unknown="ignore", drop="first"))
            ])

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, num_features),
                    ("cat", categorical_transformer, cat_features)
                ]
            )
            return Pipeline(steps=[("Preprocessor", preprocessor)])
        except Exception as e:
            raise ChurnException(e, sys) from e

    def _drop_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            drop_cols = self._schema_config["drop_columns"]
            return df.drop(columns=drop_cols, errors="ignore")
        except Exception as e:
            raise ChurnException(e, sys)

    def _encode_target(self, target_series: pd.Series) -> pd.Series:
        try:
            return target_series.map({"Yes": 1, "No": 0}).astype(int)
        except Exception as e:
            raise ChurnException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info("Data Transformation Started")

            # Ingestion path se data read karein (DVC ke liye fixed path)
            train_df = self.read_data("artifact/data_ingestion/train.csv")
            test_df = self.read_data("artifact/data_ingestion/test.csv")

            train_df = self._drop_columns(train_df)
            test_df = self._drop_columns(test_df)

            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = self._encode_target(train_df[TARGET_COLUMN])

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = self._encode_target(test_df[TARGET_COLUMN])

            preprocessor = self.get_data_transformer_object()

            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)

            smt = SMOTEENN(random_state=42, sampling_strategy="minority")
            input_feature_train_final, target_feature_train_final = smt.fit_resample(
                input_feature_train_arr, target_feature_train_df
            )

            train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)

            return DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

        except Exception as e:
            raise ChurnException(e, sys) from e

if __name__ == "__main__":
    try:
        transformer = DataTransformation()
        transformer.initiate_data_transformation()
        print("Data Transformation pipeline execution completed successfully.")
    except Exception as e:
        print(f"Data Transformation failed with error: {e}")
        sys.exit(1)







# import sys
# import numpy as np
# import pandas as pd

# from imblearn.combine import SMOTEENN

# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import StandardScaler, OneHotEncoder

# from customer_churn.constants import TARGET_COLUMN, SCHEMA_FILE_PATH
# from customer_churn.entity.config_entity import DataTransformationConfig
# from customer_churn.entity.artifact_entity import (
#     DataTransformationArtifact,
#     DataIngestionArtifact,
#     DataValidationArtifact
# )
# from customer_churn.exception import ChurnException
# from customer_churn.logger import logging
# from customer_churn.utils.main_utils import (
#     save_object,
#     save_numpy_array_data,
#     read_yaml_file
# )

# class DataTransformation:
#     def __init__(
#             self,
#             data_ingestion_artifact: DataIngestionArtifact,
#             data_transformation_config: DataTransformationConfig,
#             data_validation_artifact: DataValidationArtifact
#     ):
#         try:
#             self.data_ingestion_artifact = data_ingestion_artifact
#             self.data_transformation_config = data_transformation_config
#             self.data_validation_artifact = data_validation_artifact

#             self._schema_config = read_yaml_file(
#                 file_path=SCHEMA_FILE_PATH
#             )
#         except Exception as e:
#             raise ChurnException(e, sys)

#     @staticmethod
#     def read_data(file_path) -> pd.DataFrame:
#         try:
#             return pd.read_csv(file_path)
#         except Exception as e:
#             raise ChurnException(e, sys)

#     def get_data_transformer_object(self) -> Pipeline:
#         """
#         Creates preprocessing pipeline based on schema.yaml config.
#         """
#         logging.info("Entered get_data_transformer_object method")
#         try:
#             num_features = self._schema_config["num_features"]
#             # Corrected Key: Now using 'oh_columns' from schema.yaml
#             cat_features = self._schema_config["oh_columns"] 

#             logging.info(f"Numerical Features: {num_features}")
#             logging.info(f"Categorical Features: {cat_features}")

#             numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
#             categorical_transformer = Pipeline(steps=[
#                 ("encoder", OneHotEncoder(handle_unknown="ignore", drop="first"))
#             ])

#             preprocessor = ColumnTransformer(
#                 transformers=[
#                     ("num", numeric_transformer, num_features),
#                     ("cat", categorical_transformer, cat_features)
#                 ]
#             )

#             return Pipeline(steps=[("Preprocessor", preprocessor)])

#         except Exception as e:
#             logging.exception("Exception occurred in get_data_transformer_object")
#             raise ChurnException(e, sys) from e

#     def _drop_columns(self, df: pd.DataFrame) -> pd.DataFrame:
#         try:
#             logging.info("Dropping unwanted columns")
#             drop_cols = self._schema_config["drop_columns"]
#             return df.drop(columns=drop_cols, errors="ignore")
#         except Exception as e:
#             raise ChurnException(e, sys)

#     def _encode_target(self, target_series: pd.Series) -> pd.Series:
#         try:
#             logging.info("Encoding target column")
#             return target_series.map({"Yes": 1, "No": 0}).astype(int)
#         except Exception as e:
#             raise ChurnException(e, sys)

#     def initiate_data_transformation(self) -> DataTransformationArtifact:
#         try:
#             logging.info("Data Transformation Started")

#             if not self.data_validation_artifact.validation_status:
#                 raise Exception(self.data_validation_artifact.message)

#             train_df = self.read_data(self.data_ingestion_artifact.trained_file_path)
#             test_df = self.read_data(self.data_ingestion_artifact.test_file_path)

#             train_df = self._drop_columns(train_df)
#             test_df = self._drop_columns(test_df)

#             input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
#             target_feature_train_df = self._encode_target(train_df[TARGET_COLUMN])

#             input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
#             target_feature_test_df = self._encode_target(test_df[TARGET_COLUMN])

#             preprocessor = self.get_data_transformer_object()

#             input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
#             input_feature_test_arr = preprocessor.transform(input_feature_test_df)

#             # Apply SMOTEENN
#             smt = SMOTEENN(random_state=42, sampling_strategy="minority")
#             input_feature_train_final, target_feature_train_final = smt.fit_resample(
#                 input_feature_train_arr, target_feature_train_df
#             )

#             train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final)]
#             test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#             save_object(self.data_transformation_config.transformed_object_file_path, preprocessor)
#             save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
#             save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)

#             return DataTransformationArtifact(
#                 transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
#                 transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
#                 transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
#             )

#         except Exception as e:
#             raise ChurnException(e, sys) from e