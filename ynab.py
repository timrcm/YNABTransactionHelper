from os import getenv
import requests


class YNAB:
    def __init__(self):
        self.token = getenv('YNAB_TOKEN')
        self.endpoint = 'https://api.ynab.com/v1/budgets'
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }
        self.budget_id = self.get_budget_id()

    def get_budget_id(self):
        response = requests.get(url=self.endpoint,
                                headers=self.headers)
        return response.json()['data']['budgets'][0]['id']

    def create_transaction(self):
        data = {
            'transaction': {
                'account_id': None,
                'date': None,
                'amount': None,
                'payee_id': None,
                'payee_name': None,
                'category_id': None,
                'memo': None,
                'cleared': None,
                'approved': None,
                'flag_color': None,
                'import_id': None
            }
        }
        response = requests.post(url=f'{self.endpoint}/{self.budget_id}/transactions', headers=self.headers, data=data)
        print(response.json())
