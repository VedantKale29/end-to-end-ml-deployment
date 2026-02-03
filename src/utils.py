import os, sys
import numpy as np
import pandas as pd

from src.exception import CoustomException
import dill


def save_object(file_path,obj):
    """
    Docstring for save_object
    
    :param file_path: path to save the object
    :param obj: object to be saved
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CoustomException(e, sys)