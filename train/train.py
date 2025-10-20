# train/train.py
import joblib
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import os

# Fixem una seed per garantir que sempre dona els mateixos resultats
SEED = 42
np.random.seed(SEED)

# Carreguem el dataset obert de sklearn
Xy = load_diabetes(as_frame=True)
X = Xy.frame.drop(columns=["target"])
y = Xy.frame["target"]

# Dividim en train i test
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

# Creem pipeline: escalem + regressió lineal
pipe = make_pipeline(StandardScaler(), LinearRegression())
pipe.fit(X_train, y_train)

# Avaluem el model
pred = pipe.predict(X_val)
rmse = sqrt(mean_squared_error(y_val, pred))
print(f"RMSE del modelo: {rmse:.2f}")

# Guardem el model entrenat
os.makedirs("model", exist_ok=True)
joblib.dump({"model": pipe, "rmse": rmse, "version": "v0.1"}, "model/model_v0.1.joblib")
print("✅ Modelo guardado en model/model_v0.1.joblib")
