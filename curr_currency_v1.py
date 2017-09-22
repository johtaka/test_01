#calculating currency v1
import json,requests,sys

pairs = {'1': 'USDJPY', '2':'EURJPY', '3':'EURUSD'}

def setDefault(value, default):
    if value == '':
        print('default ' + str(default) + ' is set')
        return  default
    else:
        return float(value)

def getrate(pair,spread):
    pair_text = pairs.get(pair)
    url = "https://www.gaitameonline.com/rateaj/getrate"
    response = requests.get(url)
    response.raise_for_status()
    currency_data = json.loads(response.text)
    quotes = currency_data['quotes']
    for quote in quotes:
        if quote.get('currencyPairCode') == pair_text:
            return float(quote.get(spread))    

def losscut_straight(pair, exchange_rate, lot , leverage, equity):
    pair_text = pairs.get(pair)
#margin_requirement : Shoko kin    
    margin_requirement = exchange_rate * lot * 1000 / leverage
    print('Margin: ' + str(margin_requirement))
    if margin_requirement > equity:
        print('WARNING: MARGIN EXCEEDS EQUITY')
    margin_level = equity / margin_requirement
    print('Available margin: ' + str(int(equity) - float(margin_requirement)))
    print('Margin level: ' + str(margin_level * 100)+'%')
    print('+ 1 JPY(100 pips) => '+ str( 1 * int(lot * 1000) ) + ' benefit')
    losscut = float(exchange_rate)
    print('calculating..')
    while True:
        losscut = losscut - float(0.001)
#        for num in range(100):
#            if num % 10000 == 0:
#                print('.', end='')
        if float(losscut_rate) > ( int(equity) - ( float(exchange_rate) - float(losscut) ) * int(lot) * 1000 ) \
        / (float(losscut) * int(lot) / int(leverage)) * 100 :
            print ('If rate will be less than ' + str(losscut) + ', You will encounter loss cut.')
            break
        
def losscut_cross(pair, exchange_rate, lot , leverage, equity):
    pair_text = pairs.get(pair)
    margin_requirement = exchange_rate * lot * 1000 * getrate('1', 'bid') / leverage
    print('Margin Requirement(JPY): ' + str(margin_requirement))
    if margin_requirement > equity:
        print('WARNING: MARGIN EXCEEDS EQUITY')
    margin_level = equity / margin_requirement
    print('Available margin: ' + str(int(equity) - float(margin_requirement)))
    print('Margin level: ' + str(margin_level * 100)+'%')
    print('+ 100 pips(USD:1 cent) => '+ str( (0.01 ) * int(lot * 1000) * getrate('1', 'bid') ) + ' (JPY)benefit')
    losscut = float(exchange_rate)
    print('calculating..')
    while True:
        losscut = losscut - float(0.01)
        if float(losscut_rate) > ( int(equity) - (( float(exchange_rate) - float(losscut)) * int(lot) * 1000 * getrate('1', 'bid')  )) / (float(losscut) * int(lot) / int(leverage)) * getrate('1', 'bid') * 100 :
            print ('If rate will be less than ' + str(losscut) + ', You will encounter loss cut.')
            break        

print('which pair? default:1', pairs)
pair = input()
pair = str(int(setDefault(pair, 1)))

print('current exchange rate for ' + pairs.get(pair) + '. ask: '+ str(getrate(pair, 'ask'))+ " bid:" + str(getrate(pair,'bid')))
exchange_rate = input()
exchange_rate = setDefault(exchange_rate, getrate(pair, 'ask'))

print('number of lot?(default:1=1000 currencies)')
lot = input()
lot = setDefault(lot, 1)

print('leverage?(default:100)')
leverage = input()
leverage = setDefault(leverage, 100)

print('loss cut rate?(default:20%)')
losscut_rate = input()
losscut_rate = setDefault(losscut_rate, 20)

print('Equity?(default:100,000)')
equity = input()
equity = setDefault(equity, 100000)

if str(pair) == '1' or str(pair) == '2':
    losscut_straight(pair, exchange_rate, lot, leverage, equity)
else:
    losscut_cross(pair, exchange_rate, lot, leverage, equity)

