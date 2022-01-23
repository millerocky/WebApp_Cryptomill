class CoinsCurrentPrice:
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    test = cg.get_exchanges_tickers_by_id(id='bitcoin')




print(CoinsCurrentPrice.test)