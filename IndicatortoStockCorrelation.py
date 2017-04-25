import pandas as pd
from datetime import datetime

#This Code can take a stock and look up the most highly correlated economic indicators
#Stock to look up
stock = 'acan'
#Economic Indicator Data to lookup
EconomicIndicatorData = "C:/Users/Steel/Projects/Stock-Predictor-master/indicators2/26801.csvcheckpoint.csv"
df = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/Columntable_"+str(stock)+".csv")


def SplitDate(val):
    val = str(val)
    year = val[:4]
    month = val[4:6].lstrip("0")
    day = val[6:]
    return datetime(int(year), int(month), int(day))


def FormalizeDate(val):
    val = str(val)
    year = val[:4]
    month = val[5:7].lstrip("0")
    day = "01"
    return (year+"-" + month + "-" + day)


df['Date'] = df['Date'].apply(lambda x:SplitDate(x))        
df = df.set_index('Date')
df = df.resample('M').mean()
df = df.reindex()
df['Date'] = df.index.values
df['Date'] = df['Date'].apply(lambda x:FormalizeDate(str(x)))     
del df['High']
del df['Low']
del df['Close']
del df['Adj Close']


data = pd.read_csv(EconomicIndicatorData)
def convertint(val):
    try:
        return round(val * 10,0)
    except:
        disregard = True

        
#data to check correlations with
df= df.rename(columns={'Date':'date','Volume':'Adj Close'})
data = pd.merge(data, df, how = 'outer')
data.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/daily/closingdata1.csv")
series1=data['Adj Close']
data = data.T
s1 = pd.Series(series1.values, index=data.columns)
data = data.applymap(lambda x: convertint(x))
data.reindex()
df = data.corrwith(s1, axis =1)
print(df.nlargest(n=10))