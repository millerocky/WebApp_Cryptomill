from django.shortcuts import render


def show_main_page(request):
    return render(request, 'main/main_page.html')


def cryptoprojects_page(request):
    # Use CoinGecko API in order to get cryptocurrencies data
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    '''Getting all the data about Bitcoin from API'''
    BTC_current_price_API = cg.get_price(ids='bitcoin', vs_currencies='usd')
    BTC_current_price = str(BTC_current_price_API['bitcoin']['usd']) + ' $'
    # Final formatted BTC current price output
    BTC_current_price = BTC_current_price[:2] + ',' + BTC_current_price[2:]

    



    ETH_current_price_API = cg.get_price(ids='ethereum', vs_currencies='usd')
    ETH_current_price = str(ETH_current_price_API['ethereum']['usd']) + ' $'
    return render(request, 'main/ftp.html', {'BTC_current_price': BTC_current_price, 'ETH_current_price': ETH_current_price})

