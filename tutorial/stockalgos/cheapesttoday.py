import requests
import time


inp = input("Type G for Growth and D for dividend")

fileloc = ''

if inp == 'G':
  fileloc = '/Users/udaydeshpande/Downloads/VTI/growth'
elif inp == 'D':
  fileloc = '/Users/udaydeshpande/Downloads/VTI/divg' #dividend_champians'
else:
  print('Invalid option')
  exit(-1)

tickers = [line.rstrip() for line in open(fileloc)]

print(tickers)

for ticker in tickers:

    r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token=c0crljn48v6tuf296qk0')
    #print(r.json())

    f = requests.get(f'https://finnhub.io/api/v1/stock/metric?symbol={ticker}&metric=all&token=c0crljn48v6tuf296qk0')

    try:
        change = ((r.json()['c'] - r.json()['pc']) * 100 )/r.json()['pc']

        if change < 0:
            print(r.json(), f.json())
            print(ticker, r.json()['c'], r.json()['pc'], change )

        week52hi = f.json()['metric']['52WeekHigh']
        week52low = f.json()['metric']['52WeekLow']

        if r.json()['c'] < week52low:
            print(ticker, week52hi, week52low, r.json()['c'])
    except Exception as e:
        print(e, ticker, r, f)

    time.sleep(1)


