import json
from os import getenv
import requests


class Fastmail:
    def __init__(self):
        self.token = getenv('FASTMAIL_TOKEN')
        self.endpoint = 'https://api.fastmail.com/jmap'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }

    def get_account(self):
        response = requests.get(url=f'{self.endpoint}/session',
                                headers=self.headers)
        return response.json()

    def get_mail(self):
        params = {
            'using': ['urn:ietf:params:jmap:core', 'urn:ietf:params:jmap:mail'],
            'methodCalls': [
                ['Core/echo', {
                    'accountId': getenv('FASTMAIL_ACCOUNT_ID'),
                    'hello': True,
                    'blarg': 5
                },
                 'a']
            ]}
        response = requests.post(url=f'{self.endpoint}/api',
                                 headers=self.headers,
                                 data=json.dumps(params))
        print(response)
        print(response.text)
        return response.json()
