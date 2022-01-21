class CoinsCurrentPrice:
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    test = cg.get_coins_markets(vs_currency='usd')




print(CoinsCurrentPrice.test)