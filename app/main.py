from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

class Features(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

app = FastAPI()

# Use environment variable for model path
MODEL_PATH = os.getenv("MODEL_PATH", "model/model_v0.2.joblib")
model_bundle = joblib.load(MODEL_PATH)
model = model_bundle["model"]
MODEL_VERSION = model_bundle.get("version", "unknown")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}

@app.post("/predict")
def predict(features: Features):
    try:
        x = [[features.age, features.sex, features.bmi, features.bp,
              features.s1, features.s2, features.s3, features.s4, features.s5, features.s6]]
        pred = float(model.predict(x)[0])
        return {"prediction": pred}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
