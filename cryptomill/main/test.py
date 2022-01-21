class CoinsCurrentPrice:
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    test = cg.get_search_trending()


print(CoinsCurrentPrice.test)