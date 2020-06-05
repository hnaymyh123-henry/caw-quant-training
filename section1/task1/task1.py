import pandas as pd
import json
import requests
import time

def get_candle(fsym='ETH', tsym='BTC', freq="1h", start_time="2018-01-01 00:00:00", end_time="2018-06-01 00:00:00", exchange='binance'):
    
    time1 = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    end_time = time.mktime(time1)
    end_time_real = end_time
    time2 = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    start_time = time.mktime(time2)

    while end_time > start_time: 
      a={'fsym': fsym, 'tsym': tsym, 'limit': 2000, 'toTs': end_time, 'e': exchange}
      r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour', params=a)
      r2 = json.loads(r.text)
      r3 = r2['Data']['Data']
      df = pd.DataFrame(r3)
      df = df[['close', 'high', 'low', 'open', 'volumefrom', 'volumeto', 'time']]
      if end_time == end_time_real:
        data = df
      else:
        data = pd.concat([df, data], axis=0)
      time3 = data.iloc[0, 6]
      end_time = time3-3600
    
    data1 = data[data['time']>=start_time]

    data1['time'] = data1['time'].apply(lambda x : time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(x)))

    data1['volume'] = data1['volumeto']-data1['volumefrom']
    data1['basevolume']=data1['volumefrom']
    data2 = data1[['close', 'high', 'low', 'open', 'volume', 'basevolume', 'time']]

    data2 = data2.set_index(['time'])
    
    return data2.to_csv('task1')
  


get_candle(fsym='ETH', tsym='BTC', freq="1h", start_time="2018-01-01 00:00:00", end_time="2018-06-01 00:00:00", exchange='binance')

    
