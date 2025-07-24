# ml_detector.py

import joblib
import os

# Paths
BASE_DIR = r"D:\phishing_email_detector"
MODEL_FILE = os.path.join(BASE_DIR, "phishing_model.pkl")
VECTORIZER_FILE = os.path.join(BASE_DIR, "vectorizer.pkl")

# Load model and vectorizer
try:
    clf = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)
except FileNotFoundError:
    clf = None
    vectorizer = None
    print("❌ Model or vectorizer not found. Please train the model first using train_model.py.")

# Predict function
def predict_email(body_text):
    if clf is None or vectorizer is None:
        return None
    features = vectorizer.transform([body_text])
    prediction = clf.predict(features)[0]
    return prediction  # 1 = phishing, 0 = safe
