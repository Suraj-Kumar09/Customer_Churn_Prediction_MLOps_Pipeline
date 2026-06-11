import os
import sys
import numpy as np
import dill
import yaml
from pandas import DataFrame

from customer_churn.exception import ChurnException
from customer_churn.logger import logging

# YAML file read karne ke liye function
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ChurnException(e, sys) from e

# Ye alias hai taaki 'read_yaml' call karne par 'read_yaml_file' chale
def read_yaml(file_path: str) -> dict:
    return read_yaml_file(file_path)

# YAML file write karne ke liye function
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise ChurnException(e, sys) from e

# Object load karne ke liye function
def load_object(file_path: str) -> object:
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        return obj
    except Exception as e:
        raise ChurnException(e, sys) from e

# Numpy array save karne ke liye function 
def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise ChurnException(e, sys) from e

# Numpy array load karne ke liye function 
def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ChurnException(e, sys) from e

# Model/Object save karne ke liye function
def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise ChurnException(e, sys) from e