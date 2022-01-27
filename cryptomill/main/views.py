from django.shortcuts import render


def show_main_page(request):
    return render(request, 'main/main_page.html')


def cryptoprojects_page(request):
    # Use CoinGecko API in order to get cryptocurrencies data
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()

    '''Getting all the data about cryptocurrencies from CoinGecko API'''
    coin_name_rank_1 = cg.get_coins_markets(vs_currency='usd')[0]['name']
    coin_symbol_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['symbol']).upper()
    coin_current_price_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['current_price']) + ' $'
    coin_current_price_rank_1 = coin_current_price_rank_1[:2] + ',' + coin_current_price_rank_1[2:]
    coin_market_cap_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['high_24h']) + ' $'
    coin_low_24h_rank_1 = str(cg.get_coins_markets(vs_currency='usd')[0]['low_24h']) + ' $'

    coin_name_rank_2 = cg.get_coins_markets(vs_currency='usd')[1]['name']
    coin_symbol_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['symbol']).upper()
    coin_current_price_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['current_price']) + ' $'
    coin_market_cap_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['high_24h']) + ' $'
    coin_low_24h_rank_2 = str(cg.get_coins_markets(vs_currency='usd')[1]['low_24h']) + ' $'

    coin_name_rank_3 = cg.get_coins_markets(vs_currency='usd')[2]['name']
    coin_symbol_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['symbol']).upper()
    coin_current_price_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['current_price']) + ' $'
    coin_market_cap_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['high_24h']) + ' $'
    coin_low_24h_rank_3 = str(cg.get_coins_markets(vs_currency='usd')[2]['low_24h']) + ' $'

    coin_name_rank_4 = cg.get_coins_markets(vs_currency='usd')[3]['name']
    coin_symbol_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['symbol']).upper()
    coin_current_price_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['current_price']) + ' $'
    coin_market_cap_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['high_24h']) + ' $'
    coin_low_24h_rank_4 = str(cg.get_coins_markets(vs_currency='usd')[3]['low_24h']) + ' $'

    coin_name_rank_5 = cg.get_coins_markets(vs_currency='usd')[4]['name']
    coin_symbol_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['symbol']).upper()
    coin_current_price_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['current_price']) + ' $'
    coin_market_cap_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['high_24h']) + ' $'
    coin_low_24h_rank_5 = str(cg.get_coins_markets(vs_currency='usd')[4]['low_24h']) + ' $'

    coin_name_rank_6 = cg.get_coins_markets(vs_currency='usd')[5]['name']
    coin_symbol_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['symbol']).upper()
    coin_current_price_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['current_price']) + ' $'
    coin_market_cap_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['high_24h']) + ' $'
    coin_low_24h_rank_6 = str(cg.get_coins_markets(vs_currency='usd')[5]['low_24h']) + ' $'

    coin_name_rank_7 = cg.get_coins_markets(vs_currency='usd')[6]['name']
    coin_symbol_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['symbol']).upper()
    coin_current_price_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['current_price']) + ' $'
    coin_market_cap_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['high_24h']) + ' $'
    coin_low_24h_rank_7 = str(cg.get_coins_markets(vs_currency='usd')[6]['low_24h']) + ' $'

    coin_name_rank_8 = cg.get_coins_markets(vs_currency='usd')[7]['name']
    coin_symbol_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['symbol']).upper()
    coin_current_price_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['current_price']) + ' $'
    coin_market_cap_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['high_24h']) + ' $'
    coin_low_24h_rank_8 = str(cg.get_coins_markets(vs_currency='usd')[7]['low_24h']) + ' $'

    coin_name_rank_9 = cg.get_coins_markets(vs_currency='usd')[8]['name']
    coin_symbol_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['symbol']).upper()
    coin_current_price_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['current_price']) + ' $'
    coin_market_cap_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['high_24h']) + ' $'
    coin_low_24h_rank_9 = str(cg.get_coins_markets(vs_currency='usd')[8]['low_24h']) + ' $'

    coin_name_rank_10 = cg.get_coins_markets(vs_currency='usd')[9]['name']
    coin_symbol_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['symbol']).upper()
    coin_current_price_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['current_price']) + ' $'
    coin_market_cap_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['high_24h']) + ' $'
    coin_low_24h_rank_10 = str(cg.get_coins_markets(vs_currency='usd')[9]['low_24h']) + ' $'

    coin_name_rank_11 = cg.get_coins_markets(vs_currency='usd')[10]['name']
    coin_symbol_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['symbol']).upper()
    coin_current_price_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['current_price']) + ' $'
    coin_market_cap_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['high_24h']) + ' $'
    coin_low_24h_rank_11 = str(cg.get_coins_markets(vs_currency='usd')[10]['low_24h']) + ' $'

    coin_name_rank_12 = cg.get_coins_markets(vs_currency='usd')[11]['name']
    coin_symbol_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['symbol']).upper()
    coin_current_price_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['current_price']) + ' $'
    coin_market_cap_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['high_24h']) + ' $'
    coin_low_24h_rank_12 = str(cg.get_coins_markets(vs_currency='usd')[11]['low_24h']) + ' $'

    coin_name_rank_13 = cg.get_coins_markets(vs_currency='usd')[12]['name']
    coin_symbol_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['symbol']).upper()
    coin_current_price_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['current_price']) + ' $'
    coin_market_cap_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['high_24h']) + ' $'
    coin_low_24h_rank_13 = str(cg.get_coins_markets(vs_currency='usd')[12]['low_24h']) + ' $'

    coin_name_rank_14 = cg.get_coins_markets(vs_currency='usd')[13]['name']
    coin_symbol_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['symbol']).upper()
    coin_current_price_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['current_price']) + ' $'
    coin_market_cap_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['market_cap']) + ' $'
    coin_price_change_percentage_24h_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['price_change_percentage_24h']) + ' %'
    coin_high_24h_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['high_24h']) + ' $'
    coin_low_24h_rank_14 = str(cg.get_coins_markets(vs_currency='usd')[13]['low_24h']) + ' $'

    return render(request, 'main/cryptoprojects.html', {
        'coin_name_rank_1': coin_name_rank_1,
        'coin_symbol_rank_1': coin_symbol_rank_1,
        'coin_current_price_rank_1': coin_current_price_rank_1,
        'coin_price_change_percentage_24h_rank_1': coin_price_change_percentage_24h_rank_1,
        'coin_high_24h_rank_1': coin_high_24h_rank_1,
        'coin_low_24h_rank_1': coin_low_24h_rank_1,
        'coin_market_cap_rank_1': coin_market_cap_rank_1,
        
        'coin_name_rank_2': coin_name_rank_2,
        'coin_symbol_rank_2': coin_symbol_rank_2,
        'coin_current_price_rank_2': coin_current_price_rank_2,
        'coin_price_change_percentage_24h_rank_2': coin_price_change_percentage_24h_rank_2,
        'coin_high_24h_rank_2': coin_high_24h_rank_2,
        'coin_low_24h_rank_2': coin_low_24h_rank_2,
        'coin_market_cap_rank_2': coin_market_cap_rank_2,

        'coin_name_rank_3': coin_name_rank_3,
        'coin_symbol_rank_3': coin_symbol_rank_3,
        'coin_current_price_rank_3': coin_current_price_rank_3,
        'coin_price_change_percentage_24h_rank_3': coin_price_change_percentage_24h_rank_3,
        'coin_high_24h_rank_3': coin_high_24h_rank_3,
        'coin_low_24h_rank_3': coin_low_24h_rank_3,
        'coin_market_cap_rank_3': coin_market_cap_rank_3,

        'coin_name_rank_4': coin_name_rank_4,
        'coin_symbol_rank_4': coin_symbol_rank_4,
        'coin_current_price_rank_4': coin_current_price_rank_4,
        'coin_price_change_percentage_24h_rank_4': coin_price_change_percentage_24h_rank_4,
        'coin_high_24h_rank_4': coin_high_24h_rank_4,
        'coin_low_24h_rank_4': coin_low_24h_rank_4,
        'coin_market_cap_rank_4': coin_market_cap_rank_4,

        'coin_name_rank_5': coin_name_rank_5,
        'coin_symbol_rank_5': coin_symbol_rank_5,
        'coin_current_price_rank_5': coin_current_price_rank_5,
        'coin_price_change_percentage_24h_rank_5': coin_price_change_percentage_24h_rank_5,
        'coin_high_24h_rank_5': coin_high_24h_rank_5,
        'coin_low_24h_rank_5': coin_low_24h_rank_5,
        'coin_market_cap_rank_5': coin_market_cap_rank_5,

        'coin_name_rank_6': coin_name_rank_6,
        'coin_symbol_rank_6': coin_symbol_rank_6,
        'coin_current_price_rank_6': coin_current_price_rank_6,
        'coin_price_change_percentage_24h_rank_6': coin_price_change_percentage_24h_rank_6,
        'coin_high_24h_rank_6': coin_high_24h_rank_6,
        'coin_low_24h_rank_6': coin_low_24h_rank_6,
        'coin_market_cap_rank_6': coin_market_cap_rank_6,

        'coin_name_rank_7': coin_name_rank_7,
        'coin_symbol_rank_7': coin_symbol_rank_7,
        'coin_current_price_rank_7': coin_current_price_rank_7,
        'coin_price_change_percentage_24h_rank_7': coin_price_change_percentage_24h_rank_7,
        'coin_high_24h_rank_7': coin_high_24h_rank_7,
        'coin_low_24h_rank_7': coin_low_24h_rank_7,
        'coin_market_cap_rank_7': coin_market_cap_rank_7,

        'coin_name_rank_8': coin_name_rank_8,
        'coin_symbol_rank_8': coin_symbol_rank_8,
        'coin_current_price_rank_8': coin_current_price_rank_8,
        'coin_price_change_percentage_24h_rank_8': coin_price_change_percentage_24h_rank_8,
        'coin_high_24h_rank_8': coin_high_24h_rank_8,
        'coin_low_24h_rank_8': coin_low_24h_rank_8,
        'coin_market_cap_rank_8': coin_market_cap_rank_8,

        'coin_name_rank_9': coin_name_rank_9,
        'coin_symbol_rank_9': coin_symbol_rank_9,
        'coin_current_price_rank_9': coin_current_price_rank_9,
        'coin_price_change_percentage_24h_rank_9': coin_price_change_percentage_24h_rank_9,
        'coin_high_24h_rank_9': coin_high_24h_rank_9,
        'coin_low_24h_rank_9': coin_low_24h_rank_9,
        'coin_market_cap_rank_9': coin_market_cap_rank_9,

        'coin_name_rank_10': coin_name_rank_10,
        'coin_symbol_rank_10': coin_symbol_rank_10,
        'coin_current_price_rank_10': coin_current_price_rank_10,
        'coin_price_change_percentage_24h_rank_10': coin_price_change_percentage_24h_rank_10,
        'coin_high_24h_rank_10': coin_high_24h_rank_10,
        'coin_low_24h_rank_10': coin_low_24h_rank_10,
        'coin_market_cap_rank_10': coin_market_cap_rank_10,

        'coin_name_rank_11': coin_name_rank_11,
        'coin_symbol_rank_11': coin_symbol_rank_11,
        'coin_current_price_rank_11': coin_current_price_rank_11,
        'coin_price_change_percentage_24h_rank_11': coin_price_change_percentage_24h_rank_11,
        'coin_high_24h_rank_11': coin_high_24h_rank_11,
        'coin_low_24h_rank_11': coin_low_24h_rank_11,
        'coin_market_cap_rank_11': coin_market_cap_rank_11,

        'coin_name_rank_12': coin_name_rank_12,
        'coin_symbol_rank_12': coin_symbol_rank_12,
        'coin_current_price_rank_12': coin_current_price_rank_12,
        'coin_price_change_percentage_24h_rank_12': coin_price_change_percentage_24h_rank_12,
        'coin_high_24h_rank_12': coin_high_24h_rank_12,
        'coin_low_24h_rank_12': coin_low_24h_rank_12,
        'coin_market_cap_rank_12': coin_market_cap_rank_12,

        'coin_name_rank_13': coin_name_rank_13,
        'coin_symbol_rank_13': coin_symbol_rank_13,
        'coin_current_price_rank_13': coin_current_price_rank_13,
        'coin_price_change_percentage_24h_rank_13': coin_price_change_percentage_24h_rank_13,
        'coin_high_24h_rank_13': coin_high_24h_rank_13,
        'coin_low_24h_rank_13': coin_low_24h_rank_13,
        'coin_market_cap_rank_13': coin_market_cap_rank_13,

        'coin_name_rank_14': coin_name_rank_14,
        'coin_symbol_rank_14': coin_symbol_rank_14,
        'coin_current_price_rank_14': coin_current_price_rank_14,
        'coin_price_change_percentage_24h_rank_14': coin_price_change_percentage_24h_rank_14,
        'coin_high_24h_rank_14': coin_high_24h_rank_14,
        'coin_low_24h_rank_14': coin_low_24h_rank_14,
        'coin_market_cap_rank_14': coin_market_cap_rank_14,

        'coin_name_rank_15': coin_name_rank_15,
        'coin_symbol_rank_15': coin_symbol_rank_15,
        'coin_current_price_rank_15': coin_current_price_rank_15,
        'coin_price_change_percentage_24h_rank_15': coin_price_change_percentage_24h_rank_15,
        'coin_high_24h_rank_15': coin_high_24h_rank_15,
        'coin_low_24h_rank_15': coin_low_24h_rank_15,
        'coin_market_cap_rank_15': coin_market_cap_rank_15,
    })

