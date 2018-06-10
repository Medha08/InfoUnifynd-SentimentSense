import requests
import json

def currentPrice():
    url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY&limit=7'
    headers = {'X-CoinAPI-Key' : 'B1F03F85-01B1-408C-A128-F39602EEB90D'}
    response = requests.get(url, headers=headers)
    text_parsed = json.loads(response.text)
    df=[]
    for x in text_parsed:
        data = {}
        data['ClosePrice'] = x['price_close']
        data['OpenPrice'] = x['price_open']
        data['Difference'] = x['price_open'] - x['price_close']
        df.append(data)
    return df

x = currentPrice()
print(x)
