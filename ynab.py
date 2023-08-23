from os import getenv
import requests


class YNAB:
    def __init__(self):
        self.token = getenv('YNAB_TOKEN')
        self.endpoint = 'https://api.ynab.com/v1/budgets'
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }

    def get_budgets(self):
        response = requests.get(url=self.endpoint,
                                headers=self.headers)
        return response.json()
