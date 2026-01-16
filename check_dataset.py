import pandas as pd

data = pd.read_csv("Phishing_Email.csv")

print("Columns in dataset:")
print(data.columns)

print("\nFirst 5 rows:")
print(data.head())
