# tests/test_train.py
import os
import joblib
from train.train import train_model  # ajusta según tu función real

def test_train_creates_model():
    model_path = "model/test_model.joblib"
    if os.path.exists(model_path):
        os.remove(model_path)
    train_model(model_path=model_path)
    assert os.path.exists(model_path)
    model = joblib.load(model_path)
    assert model is not None
