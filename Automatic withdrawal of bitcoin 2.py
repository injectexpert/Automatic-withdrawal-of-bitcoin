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
        print('Rejected:', str(e

))

withdraw_bitcoin(0.5, 'Your_destination_address')