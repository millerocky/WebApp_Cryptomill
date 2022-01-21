from django.shortcuts import render


def show_main_page(request):
    return render(request, 'main/main_page.html')


def cryptoprojects_page(request):
    # Use CoinGecko API in order to get cryptocurrencies data
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    '''Getting all the data about Bitcoin from API'''
    BTC_current_price_API = cg.get_coins_markets(vs_currency='usd')
    BTC_current_price = str(BTC_current_price_API[0]['current_price']) + ' $'
    # Final formatted BTC current price output
    BTC_current_price = BTC_current_price[:2] + ',' + BTC_current_price[2:]

    # Final formatted BTC market cap output
    BTC_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    BTC_market_cap = str(BTC_market_cap_API[0]['market_cap']) + ' $'

    BTC_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    BTC_price_change_percentage_24h = str(BTC_price_change_percentage_24h_API[0]['price_change_percentage_24h']) + ' %'

    BTC_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    BTC_high_24h = str(BTC_high_24h_API[0]['high_24h']) + ' $'


    BTC_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    BTC_low_24h = str(BTC_low_24h_API[0]['low_24h']) + ' $'



    ETH_current_price_API = cg.get_coins_markets(vs_currency='usd')
    ETH_current_price = str(ETH_current_price_API[1]['current_price']) + ' $'

    ETH_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    ETH_market_cap = str(ETH_market_cap_API[1]['market_cap']) + ' $'

    ETH_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    ETH_price_change_percentage_24h = str(ETH_price_change_percentage_24h_API[1]['price_change_percentage_24h']) + ' %'

    ETH_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    ETH_high_24h = str(ETH_high_24h_API[1]['high_24h']) + ' $'

    ETH_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    ETH_low_24h = str(ETH_low_24h_API[1]['low_24h']) + ' $'


    USDT_current_price_API = cg.get_coins_markets(vs_currency='usd')
    USDT_current_price = str(USDT_current_price_API[2]['current_price']) + ' $'

    USDT_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    USDT_market_cap = str(USDT_market_cap_API[2]['market_cap']) + ' $'

    USDT_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDT_price_change_percentage_24h = str(USDT_price_change_percentage_24h_API[2]['price_change_percentage_24h']) + ' %'

    USDT_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDT_high_24h = str(USDT_high_24h_API[2]['high_24h']) + ' $'

    USDT_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDT_low_24h = str(USDT_low_24h_API[2]['low_24h']) + ' $'


    BNB_current_price_API = cg.get_coins_markets(vs_currency='usd')
    BNB_current_price = str(BNB_current_price_API[3]['current_price']) + ' $'

    BNB_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    BNB_market_cap = str(BNB_market_cap_API[3]['market_cap']) + ' $'

    BNB_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    BNB_price_change_percentage_24h = str(BNB_price_change_percentage_24h_API[3]['price_change_percentage_24h']) + ' %'

    BNB_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    BNB_high_24h = str(BNB_high_24h_API[3]['high_24h']) + ' $'

    BNB_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    BNB_low_24h = str(BNB_low_24h_API[3]['low_24h']) + ' $'


    USDC_current_price_API = cg.get_coins_markets(vs_currency='usd')
    USDC_current_price = str(USDC_current_price_API[4]['current_price']) + ' $'

    USDC_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    USDC_market_cap = str(USDC_market_cap_API[4]['market_cap']) + ' $'

    USDC_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDC_price_change_percentage_24h = str(USDC_price_change_percentage_24h_API[4]['price_change_percentage_24h']) + ' %'

    USDC_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDC_high_24h = str(USDC_high_24h_API[4]['high_24h']) + ' $'

    USDC_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    USDC_low_24h = str(USDC_low_24h_API[4]['low_24h']) + ' $'

    ADA_current_price_API = cg.get_coins_markets(vs_currency='usd')
    ADA_current_price = str(ADA_current_price_API[5]['current_price']) + ' $'

    ADA_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    ADA_market_cap = str(ADA_market_cap_API[5]['market_cap']) + ' $'

    ADA_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    ADA_price_change_percentage_24h = str(ADA_price_change_percentage_24h_API[5]['price_change_percentage_24h']) + ' %'

    ADA_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    ADA_high_24h = str(ADA_high_24h_API[5]['high_24h']) + ' $'

    ADA_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    ADA_low_24h = str(ADA_low_24h_API[5]['low_24h']) + ' $'



    return render(request, 'main/ftp.html', {
        'BTC_current_price': BTC_current_price,
        'BTC_market_cap': BTC_market_cap,
        'BTC_price_change_percentage_24h': BTC_price_change_percentage_24h,
        'BTC_high_24h': BTC_high_24h,
        'BTC_low_24h': BTC_low_24h,

        'ETH_current_price': ETH_current_price,
        'ETH_market_cap': ETH_market_cap,
        'ETH_price_change_percentage_24h': ETH_price_change_percentage_24h,
        'ETH_high_24h': ETH_high_24h,
        'ETH_low_24h': ETH_low_24h,

        'USDT_current_price': USDT_current_price,
        'USDT_market_cap': USDT_market_cap,
        'USDT_price_change_percentage_24h': USDT_price_change_percentage_24h,
        'USDT_high_24h': USDT_high_24h,
        'USDT_low_24h': USDT_low_24h,

        'BNB_current_price': BNB_current_price,
        'BNB_market_cap': BNB_market_cap,
        'BNB_price_change_percentage_24h': BNB_price_change_percentage_24h,
        'BNB_high_24h': BNB_high_24h,
        'BNB_low_24h': BNB_low_24h,

        'USDC_current_price': USDC_current_price,
        'USDC_market_cap': USDC_market_cap,
        'USDC_price_change_percentage_24h': USDC_price_change_percentage_24h,
        'USDC_high_24h': USDC_high_24h,
        'USDC_low_24h': USDC_low_24h,

        'ADA_current_price': ADA_current_price,
        'ADA_market_cap': ADA_market_cap,
        'ADA_price_change_percentage_24h': ADA_price_change_percentage_24h,
        'ADA_high_24h': ADA_high_24h,
        'ADA_low_24h': ADA_low_24h,


    })

