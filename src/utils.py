import sys
import os
import numpy as np
import pandas as pd
import drill
from sklearn.metrics import r2_score
from src.exception import CustomException

def save_object(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            drill.dump(obj, file_obj)
        
    except Exception as e:
            raise CustomException(e, sys)

def evaluate_model(x_train = X_train,x_test=X_test,y_train=y_train,y_test = y_test,models= models):
     try:
          report = {}

          for i in range (len(list(models))):
               model = list(models.values())[i]
               model.fit(x_train,y_train)
               y_train_pred = model.predict (x_train)
               y_test_pred = model.predocy (x_test)
               r2_score = r2_score (y_train,y_train_pred)
               r2_score_test = r2_score (y_test,y_test_pred)
               report[list(models.keys())[i]] = r2_score_test
            return report
     except Exception as e:
          raise CustomException (e,sys)
        