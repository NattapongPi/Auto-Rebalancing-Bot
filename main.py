from keep_alive import keep_alive

from calculate import cal_amount
from calculate import cal_amount_to_sell

from coins import coins

from spot_trade import create_market_buy_order
from spot_trade import create_market_sell_order

from account import get_balance_usdt
from account import get_balance_in_usdt
from account import get_balances_as_dict

from discord_webhook import trigger_webhook

import asyncio


async def main():
    hour = 60*60
    time_multiplier = 4
    time_wait = hour*time_multiplier

    if get_balance_usdt() < 10:
        # not enough usdt ==> waiting to sell
        state = 1
    else:
        # much usdt waiting to buy
        state = 0

    while True:
        print('====================')
        if state == 0:
            # buy
            amount = cal_amount()
            for i in range(len(coins)):
                create_market_buy_order(f'{coins[i]}USDT', amount[i])
            print('====================')
            print('====================')
            print('bought')
            print(f'waiting for {time_wait} hr')
            state = 1
            trigger_webhook(get_balances_as_dict(), get_balance_in_usdt(), 'BUY')

        # sell all
        elif state == 1:
            for i in range(time_multiplier):
              print(f'passed {i+1} hours')
              await asyncio.sleep(hour)
            amount_to_sell = cal_amount_to_sell()
            for i in range(len(coins)):
                create_market_sell_order(f'{coins[i]}USDT', amount_to_sell[i])
            print('====================')
            print('====================')
            print('sold')
            state = 0
            trigger_webhook(get_balances_as_dict(), get_balance_in_usdt(), 'SELL')


keep_alive()

asyncio.run(main())
