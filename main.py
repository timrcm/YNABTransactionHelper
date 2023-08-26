import json
from fastmail import Fastmail
from scraper import Scraper
from ynab import YNAB

if __name__ == '__main__':
    fastmail = Fastmail()
    ynab = YNAB()
    scraper = Scraper()
    # with open('fastmail.json', 'w') as f:
    #     f.write(json.dumps(fastmail.get_account(), indent=2))
    # with open('ynab.json', 'w') as f:
    #     f.write(json.dumps(ynab.get_budgets(), indent=2))
    # with open('mail.json', 'w') as f:
    #     f.write(json.dumps(fastmail.test_request(), indent=2))

    # mail_ids = fastmail.get_mail_body_ids()
    # fastmail.get_mail(mail_ids)
    # with open(f'{mail_ids[0]}.html', 'r') as f:
    #     scraper.electric_payment_details(f)

    print(ynab.get_budget_id())
