import os
import requests

TOKEN = os.environ.get("8754468863:AAFwWFJU7Z7tekjK43BKtU_5Y7qMGWQEkMg")
CHAT_ID = os.environ.get("-1003526857710")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "МЯУ"}

response = requests.post(url, data=data)
print(response.status_code, response.text)
