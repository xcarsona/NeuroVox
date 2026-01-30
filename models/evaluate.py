import joblib
import pandas as pd
from sklearn.metrics import classification_report

# Load model
model = joblib.load("models/saved_models/logistic_tfidf.pkl")

# Load data
data = pd.read_csv("data/mental_health.csv")
X = data["text"]
y = data["label"]

# Predict
y_pred = model.predict(X)

# Report
print(classification_report(y, y_pred))
