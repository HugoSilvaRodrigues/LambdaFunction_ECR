import joblib
import pandas as pd
import json
import sklearn 

def lambda_handler(event,context):
    
    try:
        model=joblib.load("model.pkl")
    except  Exception as e:
        print(e)
    try:
        pipeline=joblib.load("pipeline.pkl")
    except Exception as e:
        print(e)
    
    try:
        sample=pd.DataFrame({"calories":[event["x1"]],"carbohydrate":[event["x2"]],"sugar":[event["x3"]],"protein":[event["x4"]],"servings":[event["x5"]],"category":[event["x6"]]})
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