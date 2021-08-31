import os
from binance.spot import Spot as Client

key = os.environ['key']
secret = os.environ['secret']

base_url = 'https://api.binance.com'

client = Client(key, secret, base_url=base_url)


def create_market_buy_order(symbol=None, quantity=None):
    if symbol is None or quantity is None:
        print('symbol or quantity not found')
        return
    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'MARKET',
        'quantity': quantity,
    }
    response = client.new_order(**params)
    print(response)


def create_market_sell_order(symbol=None, quantity=None):
    if symbol is None or quantity is None:
        print('symbol or quantity not found')
        return
    params = {
        'symbol': symbol,
        'side': 'SELL',
        'type': 'MARKET',
        'quantity': quantity,
    }
    response = client.new_order(**params)
    print(response)
