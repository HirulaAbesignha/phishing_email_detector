# main.py

import os
from email import message_from_file
import tldextract
from ml_detector import predict_email

# ---- Rule-Based Heuristics ----
def rule_based_detection(subject, sender, body):
    reasons = []
    suspicious_keywords = ["urgent", "verify", "login", "click here", "account", "password"]

    sender_domain = sender.split("@")[-1]
    domain = tldextract.extract(sender_domain).registered_domain

    if not domain.endswith("yourcompany.com"):  # Change to your trusted domain
        reasons.append(f"⚠️ Untrusted sender domain: {domain}")

    if any(word.lower() in body.lower() for word in suspicious_keywords):
        reasons.append("⚠️ Suspicious keywords found in body.")

    if "http" in body.lower():
        reasons.append("⚠️ Contains hyperlinks.")

    return reasons

# ---- Email File Reader ----
def read_eml_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = message_from_file(f)
    subject = msg.get('Subject', '')
    sender = msg.get('From', '')
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body += part.get_payload(decode=True).decode(errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')
    return subject, sender, body

# ---- Main Analysis ----
def analyze_email(eml_path):
    subject, sender, body = read_eml_file(eml_path)

    print(f"\n📧 Email Subject: {subject}")
    print(f"📤 From: {sender}")
    print("📄 Email body snippet:\n", body[:200], "...\n")

    # Rule-based detection
    rules = rule_based_detection(subject, sender, body)
    print("🔍 Rule-Based Detection:")
    if rules:
        for reason in rules:
            print(f" - {reason}")
    else:
        print(" - ✅ No suspicious patterns found.")

    # ML Detection
    ml_result = predict_email(body)
    print("\n🤖 ML Prediction: ", end="")
    if ml_result is None:
        print("❌ Could not run ML model.")
    elif ml_result == 1:
        print("🚨 Phishing email detected by model!")
    else:
        print("✅ Seems legitimate (according to model).")

# ---- Entry Point ----
if __name__ == "__main__":
    email_path = os.path.join(r"D:\phishing_email_detector", "sample_email.eml")
    if os.path.exists(email_path):
        analyze_email(email_path)
    else:
        print(f"❌ Email file not found at: {email_path}")
