import os
from binance.spot import Spot as Client
from coins import coins

from get_price import get_market_price

key = os.environ['key']
secret = os.environ['secret']

base_url = 'https://api.binance.com'

client = Client(key, secret, base_url=base_url)


def get_balances_as_dict():
    balances = client.account()['balances']  #get array of balances
    balance_use = []
    for i in range(len(balances)):
        for j in range(len(coins)):
            if balances[i]['asset'] == coins[j]:
                balance_use.append(balances[i].copy())
                break
    return balance_use


def get_balances_as_list():
    balances = get_balances_as_dict()
    balance_use = []
    for i in range(len(balances)):
        print(float(str(balances[i]['free'])))
        amount = float(str(balances[i]['free']))
        balance_use.append(amount)
    return balance_use


#float
def get_balance_single(coin):
    balances = client.account()['balances']
    for i in range(len(balances)):
        if balances[i]['asset'] == coin:
            balance = balances[i]
            return float(str(balance['free']))
    return f'{coin} not found'


#float
def get_balance_usdt():
    balances = client.account()['balances']
    for i in range(len(balances)):
        if balances[i]['asset'] == 'USDT':
            balance = balances[i]
            return float(str(balance['free']))
    return 'USDT not found'


#float
def get_balance_in_usdt():
    balances = get_balances_as_dict()
    balance_usdt = get_balance_usdt()
    total = 0
    for i in range(len(balances)):
        for j in range(len(coins)):
            if balances[i]['asset'] == coins[j]:
                price = get_market_price(coins[j])
                total += float(str(balances[i]['free'])) * price
    total += balance_usdt
    return total
