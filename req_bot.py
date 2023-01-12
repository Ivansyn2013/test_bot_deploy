import requests
from dotenv import load_dotenv
import os

load_dotenv()
BOTTOKEN = os.getenv('BOTTOKEN')
req = requests.post(f'https://api.telegram.org/bot{BOTTOKEN}/setWebhook',
                    headers={'Content-Type': 'application/json'},
                    json={'url':'https://176.119.157.117'})


print(req.json)
print(req.headers)
print(req.text)