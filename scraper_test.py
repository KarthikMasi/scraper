import requests
r = requests.get("https://gamma-api.polymarket.com/events?closed=false")
response = r.json()

election_events = {}
for event in response:
  if 'Presidential Election Winner 2024' in event['title']:
    id = event['id']
    election_events[event['id']] = event

trump_percentage = ''
Kamala_percentage = ''

for events in election_events[id]['markets']:

    if 'Donald Trump' in events['question']:
        trump_at = events['createdAt']+': '
        trump_percentage = float(events['outcomePrices'].replace('[', '').replace(']', '').replace('"', '').split(',')[0])

    if 'Kamala Harris' in events['question']:
        Kamala_at=events['createdAt']+':'
        Kamala_percentage = float(events['outcomePrices'].replace('[', '').replace(']', '').replace('"', '').split(',')[0])

print(f'{trump_at} Trump win percentage {trump_percentage* 100:.2f}%')
print(f'{Kamala_at} Kamala win percentage {Kamala_percentage* 100:.2f}%')
