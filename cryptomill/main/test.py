class CoinsCurrentPrice:
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    test = cg.get_coins_markets(vs_currency='usd')
    test = test[0]['name']



print(CoinsCurrentPrice.test)