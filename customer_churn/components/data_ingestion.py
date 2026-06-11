import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

# Imports
from customer_churn.entity.config_entity import DataIngestionConfig
from customer_churn.entity.artifact_entity import DataIngestionArtifact
from customer_churn.exception import ChurnException
from customer_churn.logger import logging
from customer_churn.data_access.churn_data import ChurnData
from customer_churn.configuration.configuration import ConfigurationManager # Naya Import

class DataIngestion:
    def __init__(self):
        try:
            # 1. ConfigurationManager initialize karein
            config_manager = ConfigurationManager()
            
            # 2. Dynamic config fetch karein
            self.data_ingestion_config = config_manager.get_data_ingestion_config()
            
            # 3. Environment Variable (MongoDB URL)
            self.mongodb_url = os.environ.get("MONGODB_URL")
            if self.mongodb_url is None:
                logging.warning("MONGODB_URL not found!")
                
        except Exception as e:
            raise ChurnException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info(f"Exporting data from mongodb")
            churn_data = ChurnData()
            dataframe = churn_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            
            # Static path use karein (ConfigurationManager se aaya hai)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe

        except Exception as e:
            raise ChurnException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split")
            
            # Files save karein
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            
        except Exception as e:
            raise ChurnException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe)
            
            return DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
        except Exception as e:
            raise ChurnException(e, sys) from e

if __name__ == "__main__":
    try:
        ingestion = DataIngestion()
        ingestion.initiate_data_ingestion()
        print("Data Ingestion pipeline execution completed successfully.")
    except Exception as e:
        print(f"Data Ingestion failed with error: {e}")
        sys.exit(1)



# import os
# import sys

# from pandas import DataFrame
# from sklearn.model_selection import train_test_split

# from customer_churn.entity.config_entity import DataIngestionConfig
# from customer_churn.entity.artifact_entity import DataIngestionArtifact
# from customer_churn.exception import ChurnException
# from customer_churn.logger import logging
# from customer_churn.data_access.churn_data import ChurnData
# from customer_churn.configuration.configuration import ConfigurationManager



# class DataIngestion:
#     def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
#         """
#         :param data_ingestion_config: configuration for data ingestion
#         """
#         try:
#             # ENVIRONMENT VARIABLE CHECK YAHAN ADD KAREIN
#             self.mongodb_url = os.environ.get("MONGODB_URL")
#             if self.mongodb_url is None:
#                 # Agar variable nahi mila, toh warning log karein ya hardcode karein
#                 logging.warning("MONGODB_URL not found in environment variables!")
#                 self.mongodb_url = "YOUR_FALLBACK_URL_HERE" 
            
#             self.data_ingestion_config = data_ingestion_config
#         except Exception as e:
#             raise ChurnException(e, sys)
        

    
#     def export_data_into_feature_store(self)->DataFrame:
#         """
#         Method Name :   export_data_into_feature_store
#         Description :   This method exports data from mongodb to csv file
        
#         Output      :   data is returned as artifact of data ingestion components
#         On Failure  :   Write an exception log and then raise an exception
#         """
#         try:
#             logging.info(f"Exporting data from mongodb")
#             churn_data = ChurnData()
#             dataframe = churn_data.export_collection_as_dataframe(collection_name=
#                                                                    self.data_ingestion_config.collection_name)
#             logging.info(f"Shape of dataframe: {dataframe.shape}")
#             feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
#             dir_path = os.path.dirname(feature_store_file_path)
#             os.makedirs(dir_path,exist_ok=True)
#             logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
#             dataframe.to_csv(feature_store_file_path,index=False,header=True)
#             return dataframe

#         except Exception as e:
#             raise ChurnException(e,sys)
        

#     def split_data_as_train_test(self,dataframe: DataFrame) ->None:
#         """
#         Method Name :   split_data_as_train_test
#         Description :   This method splits the dataframe into train set and test set based on split ratio 
        
#         Output      :   Folder is created in s3 bucket
#         On Failure  :   Write an exception log and then raise an exception
#         """
#         logging.info("Entered split_data_as_train_test method of Data_Ingestion class")

#         try:
#             train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
#             logging.info("Performed train test split on the dataframe")
#             logging.info(
#                 "Exited split_data_as_train_test method of Data_Ingestion class"
#             )
#             dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
#             os.makedirs(dir_path,exist_ok=True)
            
#             logging.info(f"Exporting train and test file path.")
#             train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
#             test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

#             logging.info(f"Exported train and test file path.")
#         except Exception as e:
#             raise ChurnException(e, sys) from e
        


    
#     def initiate_data_ingestion(self) ->DataIngestionArtifact:
#         """
#         Method Name :   initiate_data_ingestion
#         Description :   This method initiates the data ingestion components of training pipeline 
        
#         Output      :   train set and test set are returned as the artifacts of data ingestion components
#         On Failure  :   Write an exception log and then raise an exception
#         """
#         logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

#         try:
#             dataframe = self.export_data_into_feature_store()

#             logging.info("Got the data from mongodb")

#             self.split_data_as_train_test(dataframe)

#             logging.info("Performed train test split on the dataset")

#             logging.info(
#                 "Exited initiate_data_ingestion method of Data_Ingestion class"
#             )

#             data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
#             test_file_path=self.data_ingestion_config.testing_file_path)
            
#             logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
#             return data_ingestion_artifact
#         except Exception as e:
#             raise ChurnException(e, sys) from e
        
# if __name__ == "__main__":
#     try:
#         # DataIngestion class ko initialize karna
#         ingestion = DataIngestion()
#         # Data ingestion initiate karna
#         ingestion.initiate_data_ingestion()
#         print("Data Ingestion pipeline execution completed successfully.")
#     except Exception as e:
#         print(f"Data Ingestion failed with error: {e}")
#         # DVC ko signal dene ke liye ki process fail hua hai
#         sys.exit(1)