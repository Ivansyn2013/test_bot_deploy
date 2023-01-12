import requests
from dotenv import load_dotenv
import os

load_dotenv()
BOTTOKEN = os.getenv('BOTTOKEN')
def registation():
    #нужно передать самоподписной сертификат
    req = requests.post(f'https://api.telegram.org/bot{BOTTOKEN}/setWebhook',
                        headers={'Content-Type': 'application/json'},
                        json={'url':'https://176.119.157.117'},
                        certificate=)


    print(req.json)
    print(req.headers)
    print(req.text)

def get_webhook_info():
    req = requests.post(f'https://api.telegram.org/bot{BOTTOKEN}/getWebhookInfo',
                        headers={'Content-Type': 'application/json'},
                        )

    print(req.json)
    print(req.headers)
    print(req.text)

def del_webhook_():
    req = requests.post(f'https://api.telegram.org/bot{BOTTOKEN}/getWebhookInfo',
                        headers={'Content-Type': 'application/json'},
                        )

    print(req.json)
    print(req.headers)
    print(req.text)

get_webhook_info()

get_webhook_info()