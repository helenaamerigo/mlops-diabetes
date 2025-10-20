# tests/test_api.py
import requests

def test_health():
    # Suponiendo que tu contenedor esté corriendo localmente en el puerto 8000
    response = requests.get("http://127.0.0.1:8000/health")
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert "model_version" in json_data

def test_predict():
    payload = {
        "age": 0.02,
        "sex": -0.044,
        "bmi": 0.06,
        "bp": -0.03,
        "s1": -0.02,
        "s2": 0.03,
        "s3": -0.02,
        "s4": 0.02,
        "s5": 0.02,
        "s6": -0.001
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], (float, int))
