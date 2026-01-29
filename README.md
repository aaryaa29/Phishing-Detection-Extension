# Phishing Detection Extension

An AI-powered phishing email detection system that classifies emails as **Safe** or **Phishing** using Machine Learning.  
The system is integrated with a **Chrome Extension** that allows users to analyze email content in real time through a Flask-based backend API.

---

## Overview
Phishing attacks are a major cybersecurity threat. This project aims to detect phishing emails using Natural Language Processing and Machine Learning techniques, providing quick and automated classification through a browser extension interface.

---

## Dataset
- Source: Kaggle  
- Link: https://www.kaggle.com/datasets/subhajournal/phishingemails  
- File used: `Phishing_Email.csv`

---

## Project Structure

Create a new folder in your project called extensions and add this 4 files under it.
1. manifest.json
2. popop.html
3. popup.js
4. style.css

Phishing detection project/
1. Phishing_Email.csv # Dataset
2. train_model.py # Model training script
3. model.pkl # Trained ML model
4. vectorizer.pkl # TF-IDF vectorizer
5. app.py # Flask API

 extension/

1. manifest.json
2. popup.html
3. popup.js
4. style.css


---

## How It Works
1. Email content is entered via the Chrome Extension popup
2. The text is sent to a Flask API
3. The API preprocesses the text using TF-IDF vectorization
4. A trained Naive Bayes classifier predicts whether the email is **Safe** or **Phishing**
5. The result is displayed instantly in the extension UI

---

## Model Performance
- **Accuracy:** ~92%
- Algorithm: Naive Bayes
- Feature Extraction: TF-IDF Vectorization

---

## Technologies Used
- Python
- Flask
- Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Naive Bayes Classifier
- HTML, CSS, JavaScript
- Chrome Extension APIs

---

## Setup Instructions

### Backend (Flask API)
1. Install dependencies:
   ```bash
   pip install flask scikit-learn pandas numpy
2. Run the API: python app.py

Chrome Extension

Open Chrome → chrome://extensions/

Enable Developer Mode

Click Load unpacked

Select the extension/ folder

Use the popup to analyze email content

Limitations

Model trained on a single dataset

No real-time email client integration

Not production-ready security-wise

License

This project is intended for educational and learning purposes only.

Developed By

Aarya Thengne

