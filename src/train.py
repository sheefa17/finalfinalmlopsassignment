# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("data/health_data.csv")

# Features and target
X = df[["age", "cholesterol_level"]]
y = df["risk_level"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)


joblib.dump(model, "model.pkl")

print("✅ Model trained and saved to model.pkl")

