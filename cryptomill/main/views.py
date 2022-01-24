from django.shortcuts import render


def show_main_page(request):
    return render(request, 'main/main_page.html')


def cryptoprojects_page(request):
    # Use CoinGecko API in order to get cryptocurrencies data
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    '''Getting all the data about cryptocurrencies from CoinGecko API'''
    BTC_name_API = cg.get_coins_markets(vs_currency='usd')
    BTC_name = BTC_name_API[0]['name']

    BTC_symbol_API = cg.get_coins_markets(vs_currency='usd')
    BTC_symbol= str(BTC_name_API[0]['symbol']).upper()

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



    ETH_name_API = cg.get_coins_markets(vs_currency='usd')
    ETH_name = ETH_name_API[1]['name']

    ETH_symbol_API = cg.get_coins_markets(vs_currency='usd')
    ETH_symbol = str(ETH_symbol_API[1]['symbol']).upper()

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



    USDT_name_API = cg.get_coins_markets(vs_currency='usd')
    USDT_name = USDT_name_API[2]['name']

    USDT_symbol_API = cg.get_coins_markets(vs_currency='usd')
    USDT_symbol = str(USDT_symbol_API[2]['symbol']).upper()

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



    BNB_name_API = cg.get_coins_markets(vs_currency='usd')
    BNB_name = BNB_name_API[3]['name']

    BNB_symbol_API = cg.get_coins_markets(vs_currency='usd')
    BNB_symbol = str(BNB_symbol_API[3]['symbol']).upper()

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



    USDC_name_API = cg.get_coins_markets(vs_currency='usd')
    USDC_name = USDC_name_API[4]['name']

    USDC_symbol_API = cg.get_coins_markets(vs_currency='usd')
    USDC_symbol = str(USDC_symbol_API[4]['symbol']).upper()

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



    ADA_name_API = cg.get_coins_markets(vs_currency='usd')
    ADA_name = ADA_name_API[5]['name']

    ADA_symbol_API = cg.get_coins_markets(vs_currency='usd')
    ADA_symbol = str(ADA_symbol_API[5]['symbol']).upper()

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



    SOL_name_API = cg.get_coins_markets(vs_currency='usd')
    SOL_name = SOL_name_API[6]['name']

    SOL_symbol_API = cg.get_coins_markets(vs_currency='usd')
    SOL_symbol = str(SOL_symbol_API[6]['symbol']).upper()

    SOL_current_price_API = cg.get_coins_markets(vs_currency='usd')
    SOL_current_price = str(SOL_current_price_API[6]['current_price']) + ' $'

    SOL_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    SOL_market_cap = str(SOL_market_cap_API[6]['market_cap']) + ' $'

    SOL_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    SOL_price_change_percentage_24h = str(SOL_price_change_percentage_24h_API[6]['price_change_percentage_24h']) + ' %'

    SOL_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    SOL_high_24h = str(SOL_high_24h_API[6]['high_24h']) + ' $'

    SOL_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    SOL_low_24h = str(SOL_low_24h_API[6]['low_24h']) + ' $'



    XRP_name_API = cg.get_coins_markets(vs_currency='usd')
    XRP_name = XRP_name_API[7]['name']

    XRP_symbol_API = cg.get_coins_markets(vs_currency='usd')
    XRP_symbol = str(XRP_symbol_API[7]['symbol']).upper()

    XRP_current_price_API = cg.get_coins_markets(vs_currency='usd')
    XRP_current_price = str(XRP_current_price_API[7]['current_price']) + ' $'

    XRP_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    XRP_market_cap = str(XRP_market_cap_API[7]['market_cap']) + ' $'

    XRP_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    XRP_price_change_percentage_24h = str(XRP_price_change_percentage_24h_API[7]['price_change_percentage_24h']) + ' %'

    XRP_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    XRP_high_24h = str(XRP_high_24h_API[7]['high_24h']) + ' $'

    XRP_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    XRP_low_24h = str(XRP_low_24h_API[7]['low_24h']) + ' $'



    LUNA_name_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_name = LUNA_name_API[8]['name']

    LUNA_symbol_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_symbol = str(LUNA_symbol_API[8]['symbol']).upper()

    LUNA_current_price_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_current_price = str(LUNA_current_price_API[8]['current_price']) + ' $'

    LUNA_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_market_cap = str(LUNA_market_cap_API[8]['market_cap']) + ' $'

    LUNA_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_price_change_percentage_24h = str(LUNA_price_change_percentage_24h_API[8]['price_change_percentage_24h']) + ' %'

    LUNA_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_high_24h = str(LUNA_high_24h_API[8]['high_24h']) + ' $'

    LUNA_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    LUNA_low_24h = str(LUNA_low_24h_API[8]['low_24h']) + ' $'



    DOT_name_API = cg.get_coins_markets(vs_currency='usd')
    DOT_name = DOT_name_API[9]['name']

    DOT_symbol_API = cg.get_coins_markets(vs_currency='usd')
    DOT_symbol = str(DOT_symbol_API[9]['symbol']).upper()

    DOT_current_price_API = cg.get_coins_markets(vs_currency='usd')
    DOT_current_price = str(DOT_current_price_API[9]['current_price']) + ' $'

    DOT_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    DOT_market_cap = str(DOT_market_cap_API[9]['market_cap']) + ' $'

    DOT_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOT_price_change_percentage_24h = str(DOT_price_change_percentage_24h_API[9]['price_change_percentage_24h']) + ' %'

    DOT_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOT_high_24h = str(DOT_high_24h_API[9]['high_24h']) + ' $'

    DOT_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOT_low_24h = str(DOT_low_24h_API[9]['low_24h']) + ' $'



    DOGE_name_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_name = DOGE_name_API[10]['name']

    DOGE_symbol_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_symbol = str(DOGE_symbol_API[10]['symbol']).upper()

    DOGE_current_price_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_current_price = str(DOGE_current_price_API[10]['current_price']) + ' $'

    DOGE_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_market_cap = str(DOGE_market_cap_API[10]['market_cap']) + ' $'

    DOGE_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_price_change_percentage_24h = str(DOGE_price_change_percentage_24h_API[10]['price_change_percentage_24h']) + ' %'

    DOGE_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_high_24h = str(DOGE_high_24h_API[10]['high_24h']) + ' $'

    DOGE_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    DOGE_low_24h = str(DOGE_low_24h_API[10]['low_24h']) + ' $'



    BUSD_name_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_name = BUSD_name_API[11]['name']

    BUSD_symbol_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_symbol = str(BUSD_symbol_API[11]['symbol']).upper()

    BUSD_current_price_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_current_price = str(BUSD_current_price_API[11]['current_price']) + ' $'

    BUSD_market_cap_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_market_cap = str(BUSD_market_cap_API[11]['market_cap']) + ' $'

    BUSD_price_change_percentage_24h_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_price_change_percentage_24h = str(BUSD_price_change_percentage_24h_API[11]['price_change_percentage_24h']) + ' %'

    BUSD_high_24h_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_high_24h = str(BUSD_high_24h_API[11]['high_24h']) + ' $'

    BUSD_low_24h_API = cg.get_coins_markets(vs_currency='usd')
    BUSD_low_24h = str(BUSD_low_24h_API[11]['low_24h']) + ' $'

    return render(request, 'main/cryptoprojects.html', {
        'BTC_name': BTC_name,
        'BTC_symbol': BTC_symbol,
        'BTC_current_price': BTC_current_price,
        'BTC_market_cap': BTC_market_cap,
        'BTC_price_change_percentage_24h': BTC_price_change_percentage_24h,
        'BTC_high_24h': BTC_high_24h,
        'BTC_low_24h': BTC_low_24h,

        'ETH_name': ETH_name,
        'ETH_symbol': ETH_symbol,
        'ETH_current_price': ETH_current_price,
        'ETH_market_cap': ETH_market_cap,
        'ETH_price_change_percentage_24h': ETH_price_change_percentage_24h,
        'ETH_high_24h': ETH_high_24h,
        'ETH_low_24h': ETH_low_24h,

        'USDT_name': USDT_name,
        'USDT_symbol': USDT_symbol,
        'USDT_current_price': USDT_current_price,
        'USDT_market_cap': USDT_market_cap,
        'USDT_price_change_percentage_24h': USDT_price_change_percentage_24h,
        'USDT_high_24h': USDT_high_24h,
        'USDT_low_24h': USDT_low_24h,

        'BNB_name': BNB_name,
        'BNB_symbol': BNB_symbol,
        'BNB_current_price': BNB_current_price,
        'BNB_market_cap': BNB_market_cap,
        'BNB_price_change_percentage_24h': BNB_price_change_percentage_24h,
        'BNB_high_24h': BNB_high_24h,
        'BNB_low_24h': BNB_low_24h,

        'USDC_name': USDC_name,
        'USDC_symbol': USDC_symbol,
        'USDC_current_price': USDC_current_price,
        'USDC_market_cap': USDC_market_cap,
        'USDC_price_change_percentage_24h': USDC_price_change_percentage_24h,
        'USDC_high_24h': USDC_high_24h,
        'USDC_low_24h': USDC_low_24h,

        'ADA_name': ADA_name,
        'ADA_symbol': ADA_symbol,
        'ADA_current_price': ADA_current_price,
        'ADA_market_cap': ADA_market_cap,
        'ADA_price_change_percentage_24h': ADA_price_change_percentage_24h,
        'ADA_high_24h': ADA_high_24h,
        'ADA_low_24h': ADA_low_24h,

        'SOL_name': SOL_name,
        'SOL_symbol': SOL_symbol,
        'SOL_current_price': SOL_current_price,
        'SOL_market_cap': SOL_market_cap,
        'SOL_price_change_percentage_24h': SOL_price_change_percentage_24h,
        'SOL_high_24h': SOL_high_24h,
        'SOL_low_24h': SOL_low_24h,

        'XRP_name': XRP_name,
        'XRP_symbol': XRP_symbol,
        'XRP_current_price': XRP_current_price,
        'XRP_market_cap': XRP_market_cap,
        'XRP_price_change_percentage_24h': XRP_price_change_percentage_24h,
        'XRP_high_24h': XRP_high_24h,
        'XRP_low_24h': XRP_low_24h,

        'LUNA_name': LUNA_name,
        'LUNA_symbol':LUNA_symbol,
        'LUNA_current_price': LUNA_current_price,
        'LUNA_market_cap': LUNA_market_cap,
        'LUNA_price_change_percentage_24h': LUNA_price_change_percentage_24h,
        'LUNA_high_24h': LUNA_high_24h,
        'LUNA_low_24h': LUNA_low_24h,

        'DOT_name': DOT_name,
        'DOT_symbol': DOT_symbol,
        'DOT_current_price': DOT_current_price,
        'DOT_market_cap': DOT_market_cap,
        'DOT_price_change_percentage_24h': DOT_price_change_percentage_24h,
        'DOT_high_24h': DOT_high_24h,
        'DOT_low_24h': DOT_low_24h,

        'DOGE_name': DOGE_name,
        'DOGE_symbol': DOGE_symbol,
        'DOGE_current_price': DOGE_current_price,
        'DOGE_market_cap': DOGE_market_cap,
        'DOGE_price_change_percentage_24h': DOGE_price_change_percentage_24h,
        'DOGE_high_24h': DOGE_high_24h,
        'DOGE_low_24h': DOGE_low_24h,

        'BUSD_name': BUSD_name,
        'BUSD_symbol': BUSD_symbol,
        'BUSD_current_price': BUSD_current_price,
        'BUSD_market_cap': BUSD_market_cap,
        'BUSD_price_change_percentage_24h': BUSD_price_change_percentage_24h,
        'BUSD_high_24h': BUSD_high_24h,
        'BUSD_low_24h': BUSD_low_24h,
    })

