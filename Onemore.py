import csv
import requests
import json
from datetime import date
import calendar
my_date = date.today()



url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY&limit=7'
headers = {'X-CoinAPI-Key' : 'B1F03F85-01B1-408C-A128-F39602EEB90D'}
response = requests.get(url, headers=headers)

text_parsed = json.loads(response.text)
c=0

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ["Date", "OpenPrice", "ClosePrice", "Difference"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in text_parsed:
        y = (my_date.weekday()-c)%7
        writer.writerow({'Date': calendar.day_name[y][0:3], 'OpenPrice': x['price_open'],'ClosePrice':x['price_close'],'Difference':x['price_open']-x['price_close']})
        c= c+1


