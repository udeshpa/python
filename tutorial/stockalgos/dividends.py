import requests


fileloc = '/Users/udaydeshpande/Downloads/VTI/divg'

tickers = [line.rstrip() for line in open(fileloc)]

for ticker in tickers:
  r = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/dividends/5y?token=sk_921dbc0ba1624e08a2601dc0e0c7ded7')
  q = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=sk_921dbc0ba1624e08a2601dc0e0c7ded7')

  print(f'{ticker}: {r.json()[0]["amount"]} {q.json()["close"]} {400 * (r.json()[0]["amount"] / q.json()["close"])}')
