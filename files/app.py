import json
import boto3
import pandas as pd
import joblib
import sklearn  

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    s3_bucket = "nome_s3"

    # Baixa os arquivos do modelo e pipeline
    s3.download_file(s3_bucket, "model.pkl", "/tmp/model.pkl")
    s3.download_file(s3_bucket, "pipeline.pkl", "/tmp/pipeline.pkl")

    # Carrega o modelo e o pipeline corretamente
    model = joblib.load("/tmp/model.pkl")
    pipeline = joblib.load("/tmp/pipeline.pkl")

    # Cria DataFrame de exemplo
    sample = pd.DataFrame([{
        "Gender": event["x1"],
        "Age": event["x2"],
        "Avg_BPM": event["x3"],
        "Session_Duration_hours": event["x4"],
        "Workout_Type": event["x5"],
        "Fat_Percentage": event["x6"],
        "Water_Intake_liters": event["x7"],
        "Workout_Frequency_daysweek": event["x8"],
        "Experience_Level": event["x9"]
    }])

    # Transforma e prediz
    sample_transformed = pipeline.transform(sample)
    prediction = model.predict(sample_transformed)

    return {
        'statusCode': 200,
        'body': json.dumps({"Prediction": prediction.tolist()})
    }

