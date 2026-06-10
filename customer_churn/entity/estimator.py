import sys
import pandas as pd
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from customer_churn.exception import ChurnException
from customer_churn.logger import logging

class TargetValueMapping:
    """
    Class to map target labels between human-readable format and machine-readable format.
    """
    def __init__(self):
        self.yes: int = 1
        self.no: int = 0
    
    def _asdict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))

class MyModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        :param preprocessing_object: Input Object of preprocessor (Pipeline)
        :param trained_model_object: Input Object of trained model
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, dataframe: pd.DataFrame) -> DataFrame:
        """
        Applies pre-trained transformations and returns model predictions.
        """
        try:
            logging.info("Starting prediction process.")

            # Step 1: Apply transformations stored in preprocessing_object
            # Yeh automatically wahi scaler aur encoder apply karega jo training ke time use huye the
            transformed_feature = self.preprocessing_object.transform(dataframe)

            # Step 2: Perform prediction
            logging.info("Using the trained model for prediction")
            predictions = self.trained_model_object.predict(transformed_feature)

            return predictions

        except Exception as e:
            logging.error("Error occurred in predict method", exc_info=True)
            raise ChurnException(e, sys) from e

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"