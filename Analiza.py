import pandas as pd
import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import seaborn as sns
import openpyxl as op
import scipy as scp

#%matplotlib inline
#
df = pdr.get_data_yahoo('SONY', '2021-01-01')
# #
#print(df.head)
# # a = 'abc'
# # b = 'xyz'
#
plt.plot(df['Close'], label='Sony')
plt.legend()
plt.title("Sony historical Prices per share")
plt.show()
#
df['MA_30'] = df['Close'].rolling(30).mean()
df['MA_60'] = df['Close'].rolling(60).mean()
df['MA_90'] = df['Close'].rolling(90).mean()
# print(df.head)
# print(df.tail)
#
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='SONY')
plt.plot(df['MA_30'], label='MA_30')
plt.plot(df['MA_60'], label='MA_60')
plt.plot(df['MA_90'], label='MA_90')
plt.legend(loc=2)
plt.show()

df['Change'] = df['Close'] - df['Open']
df['Change percent'] = ((df['Close']*100/df['Open'])-100)
#print(df.head)

plt.hist(df['Change percent'])

#df['my_dates'] = df.index
#df['my_dates'] = pd.to_datetime(df['my_dates'])


#df['Day of week'] = df['my_dates'].dt.day_name()
#print(df.head)
plt.show()

#print(df.shape())
df1 = pd.DataFrame(df)

df1.to_csv('C:/Users/lukas/Desktop/Sony_2022.csv')
#print(df[df['Change percent'] > 0].shape(0))

