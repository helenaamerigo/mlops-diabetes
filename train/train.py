# train/train.py
import joblib
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import os

# Seed for reproducibility
SEED = 42
np.random.seed(SEED)

# Load dataset
Xy = load_diabetes(as_frame=True)
X = Xy.frame.drop(columns=["target"])
y = Xy.frame["target"]

# Split train/val
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

# Pipeline: StandardScaler + Ridge
pipe = make_pipeline(StandardScaler(), Ridge(alpha=1.0, random_state=SEED))
pipe.fit(X_train, y_train)

# Evaluate
pred = pipe.predict(X_val)
rmse = sqrt(mean_squared_error(y_val, pred))
print(f"RMSE for model v0.2: {rmse:.2f}")

# Save v0.2 model
os.makedirs("model", exist_ok=True)
joblib.dump({"model": pipe, "rmse": rmse, "version": "v0.2"}, "model/model_v0.2.joblib")
print("Model saved in model/model_v0.2.joblib")
