import requests
import misc
import json
from binance import get_btc, get_eth, get_ltc
token = misc.token
from time import sleep
#https://api	.telegram.org/bot477541777:AAETIJJwXJJJQyWMCibRJjBrCc75fjbpjg4/sendmessage?chat_id=262531049&text=%D0%BE%D1%85%D1%83%D1%97%D0%B2?
URL = 'https://api.telegram.org/bot' + token +'/'

global last_update_id 
last_update_id = 0


def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():
	data = get_updates()
	last_object = data['result'][-1]
	update_id = last_object['update_id']
 
	global last_update_id
	if last_update_id != update_id:
		last_update_id = update_id
		chat_id = last_object['message']['chat']['id']
		message_text= last_object['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}
		return message
	else:
		return None



def send_message(chat_id, text='Wait a second, please...'):
	url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
	requests.get(url)





def main():
	# d = get_updates()
	
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']

			if text == '/btc':
				send_message(chat_id, get_btc())
			if text == '/eth':
				send_message(chat_id, get_eth())	
			if text == '/ltc':
				send_message(chat_id, get_ltc())
			sleep(2)
		else:
			continue


if __name__ == '__main__':
	main()