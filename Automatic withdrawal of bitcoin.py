python
import requests

api_key = 'key_api'
api_secret = 'secret_key_API'

def withdraw_bitcoin(amount, destination_address):
    url = 'https://api.exchange.com/withdraw'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'amount': amount,
        'destination_address': destination_address,
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Success!')
    else:
        print('rejected.')

withdraw_bitcoin(0.5, 'Your_destination_address')



python
import ccxt

exchange = ccxt.binance({
    'apiKey': 'Your_key_API',
    'secret': 'Your_secret_key_API',
})

def withdraw_bitcoin(amount, destination_address):
    try:
        exchange.withdraw('BTC', amount, destination_address)
        print('Success!')
    except Exception as e:
        print('rejected:', str(e

))

withdraw_bitcoin(0.5, 'Your_destination_address')