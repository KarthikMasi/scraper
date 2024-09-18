import requests
import pandas as pd
from datetime import datetime
r = requests.get('https://www.realclearpolling.com/betting-odds/2024/president')

from bs4 import BeautifulSoup

html_content = r.text

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table')

if table:
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    data = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if not cells:
            continue
        cell_data = [cell.text.strip() for cell in cells]
        data.append(cell_data)

    df = pd.DataFrame(data, columns=headers)
    time_of_pull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Add the "Time of Pull" column
    df['DateTime of query'] = time_of_pull

    # Print the DataFrame without the index
    print(df.to_csv(index=False,header=False))
else:
    print("Table not found in the HTML content.")

