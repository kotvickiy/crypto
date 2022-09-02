from binance import Client

from api import API_KEY, SECRET_KEY


client = Client(API_KEY, SECRET_KEY)

usdtrub = float(client.get_historical_trades(symbol="USDTRUB")[-1]['price'])
btcrub = float(client.get_historical_trades(symbol="BTCRUB")[-1]['price'])
