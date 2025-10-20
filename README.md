# MLOps Diabetes API

This repository contains a FastAPI service for predicting diabetes progression. The service currently has two versions of the model: v0.1 and v0.2. 

## Setup

Clone the repository:  
```bash
git clone https://github.com/helenaamerigo/mlops-diabetes.git
cd mlops-diabetes
```

Create a virtual environment and install dependencies:

python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate
pip install -r requirements.txt

## Running with Docker

Both model versions are Dockerized.

Run v0.1:
docker stop mlops-test || true
docker rm mlops-test || true
docker run -d -p 8000:8000 --name mlops-test ghcr.io/helenaamerigo/mlops-diabetes:v0.1
curl http://127.0.0.1:8000/health

Run v0.2:
docker stop mlops-test || true
docker rm mlops-test || true
docker run -d -p 8000:8000 --name mlops-test ghcr.io/helenaamerigo/mlops-diabetes:v0.2
curl http://127.0.0.1:8000/health

The health check endpoint /health returns:
{ "status": "ok", "model_version": "v0.1" }
or
{ "status": "ok", "model_version": "v0.2" }


## Making Predictions

Send a POST request to /predict with JSON data like:
{
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

Response:
{ "prediction": 235.9496372217627 }
