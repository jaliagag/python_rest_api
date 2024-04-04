import requests as rq
from datetime import datetime

BASE_URL = "http://jaliagaent.pythonanywhere.com"

payload = {"input": "this be a test"}
response = rq.get(BASE_URL, params=payload)

json_values = response.json()

rq_input = json_values["input"]
rq_timestamp = json_values["timestamp"]
rq_char_count = json_values["character_count"]

print(f"Le Input: {rq_input}")
print(f"Datetime: {datetime.fromtimestamp(rq_timestamp)}")
print(f"Character count: {rq_char_count}")
