import csv
import requests
import json
url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY'
headers = {'X-CoinAPI-Key' : 'B1F03F85-01B1-408C-A128-F39602EEB90D'}
response = requests.get(url, headers=headers)

text_parsed = json.loads(response.text)

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ["Date", "OpenPrice", "ClosePrice", "Difference"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in text_parsed:
        writer.writerow({'Date': x['time_period_start'], 'OpenPrice': x['price_open'],'ClosePrice':x['price_close'],'Difference':x['price_open']-x['price_close']})



