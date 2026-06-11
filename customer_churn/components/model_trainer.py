import sys
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from customer_churn.exception import ChurnException
from customer_churn.logger import logging
from customer_churn.utils.main_utils import load_numpy_array_data, load_object, save_object, read_yaml_file
from customer_churn.entity.artifact_entity import (
    DataTransformationArtifact, 
    ModelTrainerArtifact, 
    ClassificationMetricArtifact
)
from customer_churn.entity.estimator import MyModel
from customer_churn.configuration.configuration import ConfigurationManager

class ModelTrainer:
    def __init__(self):
        try:
            # ConfigurationManager se config fetch karein
            config_manager = ConfigurationManager()
            self.model_trainer_config = config_manager.get_model_trainer_config()
            self._model_config = read_yaml_file(file_path="config/model.yaml")
            
            # Transformation artifact ka path (DVC static path)
            self.data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path="artifact/data_transformation/preprocessing.pkl",
                transformed_train_file_path="artifact/data_transformation/train.npy",
                transformed_test_file_path="artifact/data_transformation/test.npy"
            )
        except Exception as e:
            raise ChurnException(e, sys)

    def get_model_object_and_report(self, train: np.array, test: np.array):
        try:
            logging.info("Training KNN model using best parameters from model.yaml")
            x_train, y_train = train[:, :-1], train[:, -1]
            x_test, y_test = test[:, :-1], test[:, -1]

            params = self._model_config['models']['KNeighborsClassifier']['params']
            
            model = KNeighborsClassifier(
                n_neighbors=params['n_neighbors'][0],
                weights=params['weights'][0],
                algorithm=params['algorithm'][0],
                p=params['p'][0]
            )
            
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            
            metric_artifact = ClassificationMetricArtifact(
                f1_score=f1_score(y_test, y_pred),
                precision_score=precision_score(y_test, y_pred),
                recall_score=recall_score(y_test, y_pred),
                accuracy_score=accuracy_score(y_test, y_pred)
            )
            return model, metric_artifact
        except Exception as e:
            raise ChurnException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Starting Model Trainer Component")
        try:
            train_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_test_file_path)
            
            trained_model, metric_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
            preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

            # Accuracy Threshold Check
            x_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            train_score = accuracy_score(y_train, trained_model.predict(x_train))
            
            if train_score < self.model_trainer_config.expected_accuracy:
                raise Exception(f"Model accuracy {train_score} is below threshold {self.model_trainer_config.expected_accuracy}")

            # Bundling Preprocessing + Model
            my_model = MyModel(preprocessing_object=preprocessing_obj, trained_model_object=trained_model)
            save_object(self.model_trainer_config.trained_model_file_path, my_model)

            return ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                metric_artifact=metric_artifact
            )
        except Exception as e:
            raise ChurnException(e, sys)

if __name__ == "__main__":
    try:
        trainer = ModelTrainer()
        trainer.initiate_model_trainer()
        print("Model Trainer pipeline execution completed successfully.")
    except Exception as e:
        print(f"Model Trainer failed with error: {e}")
        sys.exit(1)





# import sys
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# from customer_churn.exception import ChurnException
# from customer_churn.logger import logging
# from customer_churn.utils.main_utils import load_numpy_array_data, load_object, save_object, read_yaml_file
# from customer_churn.entity.config_entity import ModelTrainerConfig
# from customer_churn.entity.artifact_entity import (
#     DataTransformationArtifact, 
#     ModelTrainerArtifact, 
#     ClassificationMetricArtifact
# )
# from customer_churn.entity.estimator import MyModel

# class ModelTrainer:
#     def __init__(self, data_transformation_artifact: DataTransformationArtifact,
#                  model_trainer_config: ModelTrainerConfig):
#         self.data_transformation_artifact = data_transformation_artifact
#         self.model_trainer_config = model_trainer_config
#         self._model_config = read_yaml_file(file_path=self.model_trainer_config.model_config_file_path)

#     def get_model_object_and_report(self, train: np.array, test: np.array):
#         try:
#             logging.info("Training KNN model using notebook best parameters")
#             x_train, y_train = train[:, :-1], train[:, -1]
#             x_test, y_test = test[:, :-1], test[:, -1]

#             # Notebook ke best params load karna
#             params = self._model_config['models']['KNeighborsClassifier']['params']
            
#             # KNN Model initialization
#             model = KNeighborsClassifier(
#                 n_neighbors=params['n_neighbors'][0], # Note: Tuning logic ko aur advance karne ke liye aap yahan GridSearchCV use kar sakte hain
#                 weights=params['weights'][0],
#                 algorithm=params['algorithm'][0],
#                 p=params['p'][0]
#             )
            
#             model.fit(x_train, y_train)
#             y_pred = model.predict(x_test)
            
#             metric_artifact = ClassificationMetricArtifact(
#                 f1_score=f1_score(y_test, y_pred),
#                 precision_score=precision_score(y_test, y_pred),
#                 recall_score=recall_score(y_test, y_pred),
#                 accuracy_score=accuracy_score(y_test, y_pred)
#             )
#             return model, metric_artifact
#         except Exception as e:
#             raise ChurnException(e, sys)

#     def initiate_model_trainer(self) -> ModelTrainerArtifact:
#         logging.info("Starting Model Trainer Component")
#         try:
#             train_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_train_file_path)
#             test_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_test_file_path)
            
#             trained_model, metric_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
#             preprocessing_obj = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

#             # Accuracy Threshold Check
#             x_train, y_train = train_arr[:, :-1], train_arr[:, -1]
#             train_score = accuracy_score(y_train, trained_model.predict(x_train))
            
#             if train_score < self.model_trainer_config.expected_accuracy:
#                 raise Exception(f"Model accuracy {train_score} is below threshold {self.model_trainer_config.expected_accuracy}")

#             # Bundling Preprocessing + Model
#             my_model = MyModel(preprocessing_object=preprocessing_obj, trained_model_object=trained_model)
#             save_object(self.model_trainer_config.trained_model_file_path, my_model)

#             return ModelTrainerArtifact(
#                 trained_model_file_path=self.model_trainer_config.trained_model_file_path,
#                 metric_artifact=metric_artifact
#             )
#         except Exception as e:
#             raise ChurnException(e, sys)