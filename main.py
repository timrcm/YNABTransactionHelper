import json
from fastmail import Fastmail
from ynab import YNAB

if __name__ == '__main__':
    fastmail = Fastmail()
    ynab = YNAB()
    # with open('fastmail.json', 'w') as f:
    #     f.write(json.dumps(fastmail.get_account(), indent=2))
    # with open('ynab.json', 'w') as f:
    #     f.write(json.dumps(ynab.get_budgets(), indent=2))

    with open('mail.json', 'w') as f:
        f.write(json.dumps(fastmail.get_mail(), indent=2))
