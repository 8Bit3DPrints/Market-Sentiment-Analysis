import requests
from bs4 import BeautifulSoup
import tkinter as tk

url = 'https://www.marketwatch.com/investing/fund/spy/holdings'

def fetch_holdings():
    response = requests.get(url)
    response.raise_for_status()  # Check for any errors in the request

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table using different methods
    table = None

    # Method 1: Select by class name
    table = soup.select_one('.topHoldings table')

    # Method 2: Select by table ID
    if table is None:
        table = soup.select_one('#holdingsTab .snapshot')

    # Method 3: Find table with specific caption text
    if table is None:
        tables = soup.find_all('table')
        for t in tables:
            caption = t.caption
            if caption and 'Top 10 Holdings' in caption.text:
                table = t
                break

    # Method 4: Find table by position
    if table is None:
        tables = soup.find_all('table')
        if len(tables) > 1:
            table = tables[1]

    # Check if the table exists
    if table is None:
        print("Unable to locate the holdings table on the webpage.")
        return []

    # Find all rows in the table
    rows = table.select('tr')

    # Extract the top 10 holdings dynamically using CSS selectors
    holdings = []
    for row in rows[1:11]:  # Start from index 1 to skip the header row
        name_element = row.select_one('.symbol')
        percentage_element = row.select_one('.percentage')

        if name_element is not None and percentage_element is not None:
            name = name_element.text.strip()
            percentage = percentage_element.text.strip()
            holdings.append((name, percentage))

    return holdings

def update_holdings(holdings_list):
    holdings = fetch_holdings()

    # Clear the existing list
    holdings_list.delete(0, tk.END)

    # Add each holding to the list
    for name, percentage in holdings:
        holdings_list.insert(tk.END, f'{name}: {percentage}%')
