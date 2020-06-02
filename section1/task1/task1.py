import pandas as pd
import json
import requests
import time
a={'fsym': 'BTC', 'tsym': 'USDT', 'limit': 1680, 'toTs': '1585713600', 'e': 'binance'}
r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params=a)
r2 = json.loads(r.text)
r3 = r2['Data']['Data']
df = pd.DataFrame(r3)
data = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
#print (data.head())
t = data.loc[0, 'time']
#print (t)

while t>1490932800:
    t = data.iloc[0, 6]
    #print (t)
    t2 = t-3600
    #print (t2)
    a={'fsym': 'BTC', 'tsym': 'USDT', 'limit': 1680, 'toTs': t2, 'e': 'binance'}
    r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params=a)
    r2 = json.loads(r.text)
    r3 = r2['Data']['Data']
    df = pd.DataFrame(r3)
    df = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
    data = pd.concat([df, data], axis=0)
    

data1 = data[data['time']>=1491019200]

date = [ ]
for i in data1['time']:  
    time_obj = time.localtime(i)      
    i=time.strftime('%Y-%m-%d %H:%M:%S',time_obj)
    date.append(i)
data1[['time']] = date

data1['volume'] = data1['volumeto']-data1['volumefrom']
data1['basevolume']=data1['volumefrom']
data2 = data1[['close', 'high', 'low', 'open', 'volume', 'basevolume', 'time']]

print (data2.head())
data2.to_csv('task1')
