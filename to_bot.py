import requests
import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ['BOTTOKEN'])
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
def send_mes(chat_id, text):
    method = 'sendMessage'
    token = os.getenv('BOTTOKEN')
    url = 'http://127.0.0.1:5000'
    data = 1
    requests.post(url, data=data,)

r = requests.post(f'{WEBHOOK_URL}', json={'chat_id':'176.119.157.117'}, verify=False)
print(r.json)
print(r.text)