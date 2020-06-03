import pandas as pd
import json
import requests
import time

def get_candle(fsym='ETH', tsym='BTC', freq="1h", start_time="2018-01-01 00:00:00", end_time="2018-06-01 00:00:00", exchange='binance'):
    
    time1 = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    end_time = time.mktime(time1)
    time2 = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    start_time = time.mktime(time2)

    paramter = {'close':0, 'high':0, 'low':0, 'open':0, 'volumefrom':0, 'volumeto':0, 'time':end_time}
    data = pd.DataFrame(paramter,index=[0])

    while end_time > start_time: 
      time3 = data.iloc[0, 6]
      end_time = time3
      a={'fsym': fsym, 'tsym': tsym, 'limit': 2000, 'toTs': end_time, 'e': exchange}
      r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params=a)
      r2 = json.loads(r.text)
      r3 = r2['Data']['Data']
      df = pd.DataFrame(r3)
      df = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
      data = pd.concat([df, data], axis=0)
    
    data1 = data[data['time']>=start_time]
    data1.drop_duplicates(subset='time', keep='first', inplace=False)
    data1.drop(data1.index[-1], inplace=True)

    date = [ ]
    for i in data1['time']:  
        time_obj = time.localtime(i)      
        i=time.strftime('%Y-%m-%d %H:%M:%S',time_obj)
        date.append(i)
    data1[['time']] = date

    data1['volume'] = data1['volumeto']-data1['volumefrom']
    data1['basevolume']=data1['volumefrom']
    data2 = data1[['close', 'high', 'low', 'open', 'volume', 'basevolume', 'time']]

    data2 = data2.set_index(['time'])
    
    return data2.to_csv('task1-v2')
    #return data2.head()


print (get_candle(fsym='ETH', tsym='BTC', freq="1h", start_time="2018-01-01 00:00:00", end_time="2018-06-01 00:00:00", exchange='binance'))

    
