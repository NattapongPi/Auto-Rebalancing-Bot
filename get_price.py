import os
from binance.spot import Spot as Client

key = os.environ['key']
secret = os.environ['secret']

base_url = 'https://api.binance.com'

client = Client(key, secret, base_url=base_url)


def get_market_price(coin):
    coin = coin.upper()
    price = client.ticker_price(f'{coin}USDT')
    return float(str(price['price']))
