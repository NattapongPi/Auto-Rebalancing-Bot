from keep_alive import keep_alive

from calculate import cal_amount
from calculate import cal_amount_to_sell

from coins import coins

from spot_trade import create_market_buy_order
from spot_trade import create_market_sell_order

import asyncio


async def main():
    print('====================')
    # buy 25% each
    amount = cal_amount()
    for i in range(len(coins)):
        create_market_buy_order(f'{coins[i]}USDT', amount[i])

    print('bought')

    # wait 1 hr
    print('waiting for 1 hr')
    await asyncio.sleep(60)

    # sell all
    amount_to_sell = cal_amount_to_sell()
    for i in range(len(coins)):
        create_market_sell_order(f'{coins[i]}USDT', amount_to_sell[i])
    print('sold')

    print('waiting for 1 hr')
    await asyncio.sleep(60)


keep_alive()

asyncio.run(main())
