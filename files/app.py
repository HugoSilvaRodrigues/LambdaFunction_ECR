import joblib
import pandas as pd
import json
import sklearn 

def lambda_handler(data):
    
    try:
        model=joblib.load("model.pkl")
    except  Exception as e:
        print(e)
    try:
        pipeline=joblib.load("pipeline.pkl")
    except Exception as e:
        print(e)
    
    try:
        sample=pd.DataFrame({"calories":[data["x1"]],"carbohydrate":[data["x2"]],"sugar":[data["x3"]],"protein":[data["x4"]],"servings":[data["x5"]],"category":[data["x6"]]})
    except Exception as e:
        print(e)
        
    try:
        formated_data=pipeline.transform(sample)
    except Exception as e:
        print(e)

    try:
        pred=model.predict(formated_data)
    except Exception as e:
        print(e)
    
    return {
        'statusCode':200,
        'body':json.dumps({'Prediction': pred.tolist()}) }