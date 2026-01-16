import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("Phishing_Email.csv")

# Use only required columns
data = data[['Email Text', 'Email Type']]

# Rename for simplicity
data.columns = ["text", "label"]

# Convert labels to numbers
data["label"] = data["label"].map({
    "Safe Email": 0,
    "Phishing Email": 1
})

# Remove any empty rows
data = data.dropna()

X = data["text"]
y = data["label"]

# Convert text to numerical features
vectorizer = TfidfVectorizer(stop_words='english')

X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

# Test accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model Trained and Saved Successfully!")
