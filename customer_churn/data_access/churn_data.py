import os
import sys
import pandas as pd
import numpy as np
from typing import Optional
from pymongo import MongoClient # <-- Ye import zaroori hai
from customer_churn.constants import DATABASE_NAME
from customer_churn.exception import ChurnException

class ChurnData:
    """
    This class helps to export entire mongodb record as pandas dataframe
    """
    def __init__(self):
        try:
            # MONGODB_URL ko environment variable se load karein
            self.mongodb_url = os.environ.get("MONGODB_URL")
            if self.mongodb_url is None:
                raise Exception(f"Environment variable: MONGODB_URL is not set.")
            
            # Client initialize karein
            self.client = MongoClient(
                self.mongodb_url, 
                tls=True, 
                tlsAllowInvalidCertificates=True
            )
        except Exception as e:
            raise ChurnException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            # Database selection
            if database_name is None:
                database = self.client[DATABASE_NAME]
            else:
                database = self.client[database_name]
            
            collection = database[collection_name]

            # Data fetch karein
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise ChurnException(e, sys)