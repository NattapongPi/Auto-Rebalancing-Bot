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
    _symbol = symbol.split('USDT')
    _symbol = _symbol[0]
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


# {'symbol': 'ETHUSDT', 'orderId': 5632014913, 'orderListId': -1, 'clientOrderId': 'FLOlroyDs6kTWoJqHTfFF2', 'transactTime': 1630490874042, 'price': '0.00000000', 'origQty': '0.01390000', 'executedQty': '0.01390000', 'cummulativeQuoteQty': '49.04670600', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '3528.54000000', 'qty': '0.01390000', 'commission': '0.00001390', 'commissionAsset': 'ETH', 'tradeId': 583003675}]}