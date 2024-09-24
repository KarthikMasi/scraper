from helium import start_firefox, find_all, kill_browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

# Start Firefox in headless mode
browser = start_firefox('https://www.realclearpolling.com/polls/president/general/2024/trump-vs-harris', headless=True)

# Wait for the table to load
time.sleep(5)  # Alternatively, implement explicit waits

# Get the page source
content = browser.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find the table
table = soup.find('table')

if table:
    # Extract table headers
    headers = [th.text.strip() for th in table.find_all('th')]

    # Extract table rows
    rows = []
    for tr in table.find_all('tr')[1:]:  # Skip header row
        cells = tr.find_all('td')
        row = [cell.text.strip() for cell in cells]
        if row:
            rows.append(row)
    df = pd.DataFrame(rows, columns=headers)
    time_of_pull = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['DateTime of query'] = time_of_pull
    # Create a DataFrame
    print(df.to_csv(index=False,header=False))
else:
    print("Table not found in the rendered HTML.")

# Close the browser
kill_browser()

