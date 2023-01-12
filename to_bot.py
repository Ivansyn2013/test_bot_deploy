import requests
import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ['BOTTOKEN'])

def send_mes(chat_id, text):
    method = 'sendMessage'
    token = os.getenv('BOTTOKEN')
    url = 'http://127.0.0.1:5000'
    data = 1
    requests.post(url, data=data,)

r = requests.post('http://127.0.0.1:5000', json={'chat_id':'76.119.157.117'})
print(r.json)
print(r.text)