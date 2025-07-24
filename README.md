
# 📧 Phishing Email Detector

A hybrid phishing email detection system that uses both **rule-based heuristics** and a **machine learning model** to identify suspicious emails. Built with Python and scikit-learn, this tool processes `.eml` email files and flags phishing attempts.

---

## 🚀 Features

- 🧠 Machine Learning detection using TF-IDF + Random Forest
- 🛡️ Rule-based detection based on keywords, hyperlinks, and sender domain
- 📂 Parses and analyzes `.eml` email files
- 📊 Full classification report during model training
- 💾 Saves trained model and vectorizer for reuse

---

## 📁 Project Structure

```
phishing_email_detector/
│
├── dataset/
│   └── emails.csv               # Dataset file (you provide)
│
├── phishing_model.pkl           # Trained model (auto-generated)
├── vectorizer.pkl               # TF-IDF vectorizer (auto-generated)
├── train_model.py               # Trains ML model
├── ml_detector.py               # Handles ML prediction logic
├── main.py                      # Email analysis (rule + ML)
├── sample_email.eml             # Email file to analyze (you provide)
└── README.md                    # Project documentation
```

---

## 🧠 How to Train the Model

### 1. Add the Dataset

Place your dataset CSV file in the `dataset` folder:

```
phishing_email_detector/dataset/emails.csv
```

The CSV file should have at least two columns:

- `text` → the body content of the email
- `label` → either `Phishing Email` or `Safe Email`

### 2. Run the Training Script

Open a terminal and run:

```bash
python train_model.py
```

This script will:

- Load and preprocess the dataset
- Train a Random Forest classifier using TF-IDF features
- Save the trained model and vectorizer as:
  - `phishing_model.pkl`
  - `vectorizer.pkl`

You’ll also get a full classification report printed in the terminal.

---

## 🧪 How to Run the Email Detector

### 1. Add an Email File

Place the `.eml` file you want to analyze at:

```
phishing_email_detector/sample_email.eml
```

You can export `.eml` files from most email clients like Outlook, Thunderbird, or Gmail (via download).

### 2. Run the Analysis Script

From terminal:

```bash
python main.py
```

This will:

- Parse the email's subject, sender, and body
- Apply rule-based checks (e.g., suspicious keywords, domain, hyperlinks)
- Run ML-based prediction (phishing or not)

### ✅ Sample Output

```
📧 Email Subject: Update Your Account Now
📤 From: alert@strange-domain.com
📄 Email body snippet:
 Please verify your login details immediately...

🔍 Rule-Based Detection:
 - ⚠️ Untrusted sender domain: strange-domain.com
 - ⚠️ Suspicious keywords found in body.
 - ⚠️ Contains hyperlinks.

🤖 ML Prediction: 🚨 Phishing email detected by model!
```

---

## ⚙️ Setup & Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
pandas
scikit-learn
joblib
tldextract
```

---

## ✅ Quick Summary of Steps

| Step                          | Command / Location                                 |
|-------------------------------|-----------------------------------------------------|
| 📥 Add dataset                | `dataset/emails.csv`                                |
| 🧠 Train model                | `python train_model.py`                             |
| 📩 Add test email (.eml)     | `sample_email.eml`                                  |
| 🚀 Run detector               | `python main.py`                                    |

---

## 🔒 Notes

- Only `.eml` format emails are supported.
- You must run `train_model.py` before using `main.py` (unless model files already exist).
- You can customize the trusted domain and suspicious keywords in `main.py`.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by Hirula Abesingha 
Feel free to fork and improve!
