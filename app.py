from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re

app = Flask(__name__)
CORS(app)

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "Phishing Detection API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email = data["email"]

    # Convert text to vector
    vec = vectorizer.transform([email])

    # Prediction
    prediction = model.predict(vec)[0]

    # Confidence Score
    probability = model.predict_proba(vec)[0]
    confidence = round(max(probability) * 100, 2)

    result = "Phishing Email" if prediction == 1 else "Safe Email"

    # Keyword Reasoning
    suspicious_words = [
        "verify", "password", "bank", "urgent",
        "click", "login", "account", "security",
        "suspended", "confirm", "immediately", "hurry"
    ]

    found_words = [word for word in suspicious_words if word in email.lower()]

    # URL Detection
    urls = re.findall(r'(https?://\S+)', email)

    url_warning = []
    for url in urls:
        if "http://" in url:
            url_warning.append(url + " (Not Secure HTTP)")
        else:
            url_warning.append(url)

    return jsonify({
        "result": result,
        "confidence": confidence,
        "reasons": found_words,
        "urls_found": url_warning
    })


if __name__ == "__main__":
    app.run(debug=True)
