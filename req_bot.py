import requests
from dotenv import load_dotenv
import os
import fire

class Webhooks_setttings():
    load_dotenv()
    BOTTOKEN = os.getenv('BOTTOKEN')
    def registation(self):
        #нужно передать самоподписной сертификат
        try:
            file = open('/etc/ssl/certs/nginx_test.pem', 'rb')
        except:
            return None
        req = requests.post(f'https://api.telegram.org/bot{self.BOTTOKEN}/setWebhook',
                            headers={'Content-Type': 'application/json'},
                            json={'url':'https://176.119.157.117'},
                            certificate=file,
                            )


        print(req.json)
        print(req.headers)
        print(req.text)

    def get_webhook_info(self):
        req = requests.post(f'https://api.telegram.org/bot{self.BOTTOKEN}/getWebhookInfo',
                            headers={'Content-Type': 'application/json'},
                            )

        print(req.json)
        print(req.headers)
        print(req.text)

    def del_webhook(self):
        req = requests.post(f'https://api.telegram.org/bot{self.BOTTOKEN}/deleteWebhook',
                            headers={'Content-Type': 'application/json'},
                            )

        print(req.json)
        print(req.headers)
        print(req.text)


if __name__=='__main__':
    fire.Fire(Webhooks_setttings)
