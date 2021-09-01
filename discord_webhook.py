import os
from discord import Webhook, RequestsWebhookAdapter, Embed


def trigger_webhook(coins, balance, _type):
    url = os.environ['dc_webhook_url']

    balances_list = get_balances_as_list(coins)
    coins_list = get_asset(coins)

    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(colour=0xffff, description="amount of each asset.")

    if _type == 'BUY':
        embed.set_author(name="BUY")
        embed.clear_fields()
        for i in range(len(balances_list)):
            embed.add_field(name=f"{coins_list[i]}",
                            value=f"{balances_list[i]}",
                            inline=True)
        embed.add_field(name=f"Total", value=f"{balance}", inline=False)

    elif _type == 'SELL':
        embed.set_author(name="SELL")
        embed.clear_fields()
        embed.add_field(
            name=f"Total",
            value=f"{round_balance(balance)}$",
        )
    response = webhook.send(embed=embed)
    print(response)


def get_balances_as_list(coins):
    balances = coins
    balance_use = []
    for i in range(len(balances)):
        amount = float(str(balances[i]['free']))
        balance_use.append(amount)
    return balance_use


def get_asset(coins):
    assets = []
    for i in range(len(coins)):
        asset = str(coins[i]['asset'])
        assets.append(asset)
    return assets


def round_balance(balance):
    balance *= 100
    balance = int(balance)
    balance /= 100
    return balance
