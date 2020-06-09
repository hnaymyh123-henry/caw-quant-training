from binance.client import Client
import json
import pandas as pd

client = Client()
orderbook = client.get_order_book(symbol = 'BNBBTC')
traders = client.get_aggregate_trades(symbol = 'BNBBTC')
candle = client.get_klines(symbol ='BNBBTC', interval='1h')

# transform orderbook to dataframe
df1 = pd.DataFrame(orderbook)
df_bid = pd.DataFrame(orderbook['bids'])
df_bid.columns = ['bid_price','bid_QTY']
df_ask = pd.DataFrame(orderbook['asks'])
df_ask.columns = ['ask_price','ask_QTY']
df_id = df1['lastUpdateId']
df_orderbook = pd.concat([df_ask, df_bid], axis=1)
df_orderbook = pd.concat([df_id, df_orderbook], axis=1)
print (df_orderbook.head())
df_orderbook.to_csv('orderbook.csv')

#transform traders to dataframe
df_traders = pd.DataFrame(traders)
df_traders.columns = ['Aggregated TradeId','Price','Quantity','First TradeId', 'Last TradeId', 'Timestamp','Was the buyer the maker?','Was the trade the best price match?']
print (df_traders.head())
df_traders.to_csv('traders.csv')

df_candle = pd.DataFrame(candle)
df_candle.columns = ['Open time','Open','High','Low', 'Close', 'Volume','Closetime','Quote Asset Volume','Number of Traders','Taker Buy Base Asset Volume','Taker Buy Quote Asset Volume','a']
df_candle.drop(['a'], axis=1)
print (df_candle.head())
df_candle.to_csv('candle.csv')