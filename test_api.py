import requests

url = "http://127.0.0.1:5000/predict"

sample_email = """
Dear user,
Your bank account has been suspended.
Click the link below to verify immediately.
"""

response = requests.post(url, json={"email": sample_email})

print(response.json())
