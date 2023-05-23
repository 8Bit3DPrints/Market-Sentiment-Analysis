import requests
from bs4 import BeautifulSoup

class Holdings:
    def __init__(self):
        self.url = 'https://www.marketwatch.com/investing/fund/spy/holdings'

    def fetch_holdings(self):
        response = requests.get(self.url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.select_one('.topHoldings table')

        if table is None:
            table = soup.select_one('#holdingsTab .snapshot')

        if table is None:
            tables = soup.find_all('table')
            for t in tables:
                caption = t.caption
                if caption and 'Top 10 Holdings' in caption.text:
                    table = t
                    break

        if table is None:
            print("Unable to locate the holdings table on the webpage.")
            return []

        rows = table.select('tr')

        holdings = []
        for row in rows[1:11]:
            name_element = row.select_one('.symbol')
            percentage_element = row.select_one('.percentage')

            if name_element is not None and percentage_element is not None:
                name = name_element.text.strip()
                percentage = percentage_element.text.strip()
                holdings.append((name, percentage))

        return holdings
