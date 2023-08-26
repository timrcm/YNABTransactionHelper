from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.soup = None

    def electric_payment_details(self, email):
        self.soup = BeautifulSoup(email, 'html.parser')
        amount = self.soup.select('body > p:nth-child(4) > span:nth-child(1) > span:nth-child(1)')
        date = self.soup.select('body > p:nth-child(5) > span:nth-child(1) > span:nth-child(1)')
        print(amount, date)
