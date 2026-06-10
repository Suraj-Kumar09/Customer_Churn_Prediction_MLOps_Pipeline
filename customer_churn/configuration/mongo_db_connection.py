import os
import sys
import pymongo
import certifi
from customer_churn.constants import DATABASE_NAME, MONGODB_URL_KEY
from customer_churn.exception import ChurnException
from customer_churn.logger import logging

# certifi ka path load karna SSL handshake ke liye zaroori hai
ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :  Yeh class MongoDB database ke saath connection establish karti hai.
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                
                # tlsAllowInvalidCertificates=True add kiya hai taaki SSL/TLS handshake error bypass ho sake
                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url, 
                    tlsCAFile=ca,
                    tlsAllowInvalidCertificates=True 
                )
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
            
        except Exception as e:
            raise ChurnException(e, sys)