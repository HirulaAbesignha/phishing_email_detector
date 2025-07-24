# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Define paths
DATASET_PATH = r"D:\phishing_email_detector\dataset\emails.csv"
MODEL_PATH = r"D:\phishing_email_detector\phishing_model.pkl"
VECTORIZER_PATH = r"D:\phishing_email_detector\vectorizer.pkl"

# Load dataset
try:
    df = pd.read_csv(DATASET_PATH)
    print("📝 Total rows before filtering:", len(df))
except Exception as e:
    print("❌ Failed to read dataset:", e)
    exit()

# Preprocess
df['text'] = df['text'].fillna('').astype(str)
df = df[df['text'].str.strip() != '']
print("✅ Total rows after filtering empty text:", len(df))

# Label encoding: 1 = phishing, 0 = safe
df['label'] = df['label'].apply(lambda x: 1 if str(x).strip().lower() == 'phishing email' else 0)
print("🔍 Label counts:\n", df['label'].value_counts())

# Features and labels
X = df['text']
y = df['label']

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)
print(f"🧪 Train size: {X_train.shape[0]} | Test size: {X_test.shape[0]}")

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluation
y_pred = clf.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=["Safe Email", "Phishing Email"]))

# Save model and vectorizer
joblib.dump(clf, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)
print("\n✅ Model and vectorizer saved successfully!")
