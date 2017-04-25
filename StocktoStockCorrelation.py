#Stock to stock correlation

import os
from os import listdir
import psutil
import pandas as pd
import numpy as np
# from itertools import *
# for t in product('ABC', 'DE', 'xyz')

path = "C:/Users/Steel/Projects/Stock-Predictor-master/daily/"

data = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/Columntable_abbv.csv")
data.set_index('Date', inplace=True)
del data['High']
del data['Low']
del data['Close']
del data['Volume']
columnnames = []
for i in os.listdir(path):
    stock = str(i).split("_")[1].split(".")[0]
    try:
        df = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/" + i)
        
        del df['High']
        del df['Low']
        del df['Close']
        del df['Volume']
        df= df.rename(columns={'Date':'Date','Adj Close':str(stock)})
        df.set_index('Date', inplace=True)
        
        data = pd.concat([data, df], axis = 1)
    except Exception as e:
        continue
data.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/dailydaily/output.csv")
data.reindex()
data.fillna(value=.1, inplace = True)
series1=data['Adj Close']

data = data.T
data.columns
s1 = pd.Series(series1.values, index=data.columns)
data.fillna(value=0,inplace=True)
df = (data.corrwith(s1, axis=1))
print(df.nlargest(n=5))