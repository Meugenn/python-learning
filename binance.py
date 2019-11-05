import requests

def get_btc():
	url = 'https://api.binance.com/api/v3/ticker/price'
	r = requests.get(url).json()
	for dict in r:
		Value = dict.get('symbol')
		if Value == 'BTCUSDT':
			price = dict['price']
			return price + ' usd'
			break
	
def get_eth():
	url = 'https://api.binance.com/api/v3/ticker/price'
	r = requests.get(url).json()
	for dict in r:
		Value = dict.get('symbol')
		if Value == 'ETHUSDT':
			price = dict['price']
			return price + ' usdt'
			break

def get_ltc():
	url = 'https://api.binance.com/api/v3/ticker/price'
	r = requests.get(url).json()
	for dict in r:
		Value = dict.get('symbol')
		if Value == 'LTCUSDT':
			price = dict['price']
			return price + ' usdt'
			break



