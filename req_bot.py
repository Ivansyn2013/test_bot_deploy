import requests
from dotenv import load_dotenv
import os
import fire

class Webhooks_setttings():
    '''
    registration: for connect to api.telegrambot and set weebhook, sent self singet cert from
        '/etc/ssl/certs/nginx_test.pem'
    get_webhook_info: get info from api.telegrambot
    del_webhook: unset weebhook

    '''
    load_dotenv()
    BOTTOKEN = os.getenv('BOTTOKEN')
    def registration(self):
        #нужно передать самоподписной сертификат
        try:
            file = open('/home/common_user/test_bot_app/test_bot_deploy/ssl/bot_pub.pem','rb') 
        except:
            return 'Error File not Found' 
        req = requests.post(f'https://api.telegram.org/bot{self.BOTTOKEN}/setWebhook',
                   
                            json={'url':'https://176.119.157.117',
                                'certificate':f'{file}'},
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

