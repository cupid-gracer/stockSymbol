from stocksymbol import StockSymbol
import csv  
from alive_progress import alive_bar

api_key = '0e7ac2a7-6591-4a7a-aa59-b1fa079e312a'
ss = StockSymbol(api_key)

# symbol_list = json.loads(symbol_list_us)

header = ['symbol', 'shortName', 'longName', 'exchange', 'market', 'quoteType']

market_list = ss.market_list


with open('result.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    with alive_bar(len(market_list)) as market_bar:

        for market in market_list:
            market_name = market.get('abbreviation')

        
            symbol_list_us = ss.get_symbol_list(market = market_name)


            for line in symbol_list_us:
                data = [line.get('symbol'), line.get('shortName'), line.get('longName'), line.get('exchange'), line.get('market'), line.get('quoteType')]

        	    # write the data
                writer.writerow(data)
                    
            market_bar()