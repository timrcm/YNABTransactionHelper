from os import getenv
import requests


class Fastmail:
    def __init__(self):
        self.token = getenv('FASTMAIL_TOKEN')
        self.endpoint = 'https://api.fastmail.com/jmap/session'
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    def get_account(self):
        response = requests.get(url=self.endpoint,
                                headers=self.headers)
        return response.json()
