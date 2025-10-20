import os
from train.train import train_model  

def test_train_smoke():
    model_path = "model/test_model.joblib"
    os.makedirs("model", exist_ok=True)
    train_model(model_path)
    assert os.path.exists(model_path)
