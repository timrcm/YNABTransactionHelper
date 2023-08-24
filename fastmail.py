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
        self.account_id = self.get_account()

    def get_account(self):
        response = requests.get(url=f'{self.endpoint}/session',
                                headers=self.headers)
        return response.json()['primaryAccounts']['urn:ietf:params:jmap:core']

    def test_request(self):
        data = {
            'using': ['urn:ietf:params:jmap:core', 'urn:ietf:params:jmap:mail'],
            'methodCalls': [
                ['Core/echo', {
                    'accountId': self.account_id,
                    'hello': True,
                    'blarg': 5
                },
                 'a']
            ]}
        response = requests.post(url=f'{self.endpoint}/api',
                                 headers=self.headers,
                                 data=json.dumps(data))
        print(response)
        print(response.text)
        return response.json()

    def get_mail(self):
        data = {
            'using': ['urn:ietf:params:jmap:core', 'urn:ietf:params:jmap:mail'],
            'methodCalls': [
                ['Email/query', {
                    'accountId': self.account_id,
                    'filter': {
                        'operator': 'OR',
                        'conditions': [
                            {'subject': getenv('MAIL_SUBJECT_ELECTRIC')},
                            {'subject': getenv('MAIL_SUBJECT_GAS')}]},
                    'sort': [{"property": "receivedAt", "isAscending": False}],
                    'limit': 2,  # We only need the latest copy of each bill
                    'calculateTotal': True
                },
                 't0'],
                ['Email/get', {
                    'accountId': self.account_id,
                    '#ids': {
                        'resultOf': 't0',
                        'name': 'Email/query',
                        'path': '/ids'
                    },
                    'properties': ['threadId']
                },
                 't1'],
                ['Thread/get', {
                    'accountId': self.account_id,
                    '#ids': {
                        'resultOf': 't1',
                        'name': 'Email/get',
                        'path': '/list/*/threadId'
                    },
                }, 't2'],
                ['Email/get', {
                    'accountId': self.account_id,
                    '#ids': {
                        'resultOf': 't2',
                        'name': 'Thread/get',
                        'path': '/list/*/emailIds'
                    },
                    # 'properties': ['from', 'receivedAt', 'subject']
                }, 't3']
            ]
        }
        response = requests.post(url=f'{self.endpoint}/api',
                                 headers=self.headers,
                                 data=json.dumps(data))
        print(response.text)
        # print(response.json()['methodResponses'][3][1]['list'][0]['htmlBody'][0]['blobId'])
        blob_ids = [mail['htmlBody'][0]['blobId'] for mail in response.json()['methodResponses'][3][1]['list']]
        print(blob_ids)
