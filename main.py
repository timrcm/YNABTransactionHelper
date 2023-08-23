from fastmail import Fastmail
from ynab import YNAB

if __name__ == '__main__':
    ynab = YNAB()
    fastmail = Fastmail()
    print(ynab.get_budgets())
    print(fastmail.get_account())
