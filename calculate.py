#Auto rebalancing
#BTC, ETH, BNB, ADA
#25% each asset
from account import get_balances_as_list
from account import get_balance_in_usdt

from coins import coins
from coins import min_amount

from get_price import get_market_price


def cal_weight():
    # each asset same weight
    balance = get_balance_in_usdt()
    amount = len(coins)
    weight = balance / amount
    weight *= 100
    weight = int(weight)
    weight /= 100
    return weight


def cal_amount():
    amounts = []
    for i in range(len(coins)):
        amount = cal_weight() / get_market_price(coins[i])
        amounts.append(amount)
    for i in range(len(coins)):
        amounts[i] *= 10**min_amount[i]
        amounts[i] = int(amounts[i])
        amounts[i] /= 10**min_amount[i]
    return amounts

def cal_amount_to_sell():
  amounts = get_balances_as_list()
  for i in range(len(coins)):
        amounts[i] *= 10**min_amount[i]
        amounts[i] = int(amounts[i])
        amounts[i] /= 10**min_amount[i]
  return amounts