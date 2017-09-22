'''
from coincheck import market, order

m1 = market.Market()

print(m1.ticker())
print(m1.public_api('rate/etc_jpy'))
#最新市場情報、
print(m1.trades())

#get coincheck data
https://coincheck.com/ja/documents/exchange/api
HTTP REQUEST

GET /api/rate/[pair]

PARAMETERS

*pair 通貨ペア ( "btc_jpy" "eth_jpy" "etc_jpy" "dao_jpy" "lsk_jpy"
"fct_jpy" "xmr_jpy" "rep_jpy" "xrp_jpy" "zec_jpy" "xem_jpy" "ltc_jpy"
"dash_jpy" "bch_jpy" "eth_btc" "etc_btc" "lsk_btc" "fct_btc"
"xmr_btc" "rep_btc" "xrp_btc" "zec_btc" "xem_btc" "ltc_btc"
"dash_btc" "bch_btc" )


https://coincheck.com/api/rate/etc_jpy
{"rate":"1173.81959676"}
'''
import json,requests,sys

jul_data = {"btc_jpy": 0.04145138, "eth_jpy": 0.4582,  "etc_jpy": 5.69245,
            "dao_jpy": 0, "lsk_jpy": 51.656 , "fct_jpy": 5.71537,
            "xmr_jpy": 2.4928, "rep_jpy": 4.8366, "xrp_jpy": 500.03,
            "zec_jpy": 0.48134, "xem_jpy": 657.46, "ltc_jpy": 2.0386,
            "dash_jpy": 0.57463,  "bch_jpy": 0} 

aug_data = {"btc_jpy": 0.02835, "eth_jpy": 0.2882,  "etc_jpy": 5.6925,
            "dao_jpy": 0, "lsk_jpy": 26.6760 , "fct_jpy": 2.5554,
            "xmr_jpy": 1.0928, "rep_jpy": 3.8366, "xrp_jpy": 450.03,
            "zec_jpy": 0.4113, "xem_jpy": 353.46, "ltc_jpy": 2.0386,
            "dash_jpy": 0.3046,  "bch_jpy": 0.1465} 

def getrate(pair):
    url = "https://coincheck.com/api/rate/" + pair
    response = requests.get(url)
    response.raise_for_status()
#    print(response.text)
    dictionary = json.loads(response.text)
    return float(dictionary["rate"])
#    currency_data = json.loads(response.text)
#    quotes = currency_data['quotes']
'''    
    for quote in quotes:
        if quote.get('currencyPairCode') == pair_text:
            return float(quote.get(spread))
'''
total_jpy = 0
print('July')
for k, v in jul_data.items():
    print('pair: '+ k + ' amount:' + ' current rate: ' + str(getrate(k)) \
          + ' total: ' + str(getrate(k) * v))
    total_jpy = getrate(k) * v + total_jpy
print('total jpy: '+str(total_jpy))

total_jpy = 0
print('==================')
print('August')
for k, v in  aug_data.items():
    print('pair: '+ k + ' amount:' + ' current rate: ' + str(getrate(k)) \
          + ' total: ' + str(getrate(k) * v))
    total_jpy = getrate(k) * v + total_jpy
print('total jpy: '+str(total_jpy))



