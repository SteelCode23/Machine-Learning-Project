import multiprocessing
import pandas
import threading
import pandas as pd
from os import listdir
import requests
import json
import asyncio
import urllib
import csv
import pdb
import dask.dataframe as dd
from dask.distributed import progress
from distributed import Client
import ssl
import datetime



# engine = create_engine('postgresql://admin:admin@localhost:5433/postgres')
# conn = engine.connect()


# client = MongoClient()
# lm = LinearRegression()
# lm.fit(x, y)
# fc = zip(features, lm.coef_)
# list(fc)
# lm.score(x, y)


#from string import rsplit
API_KEY = "17188a6953269ab608ba14c3e3d8fb02"
path = "C:/FREDDATA/somedata"
# client = MongoClient('mongodb://localhost:27017/')
# db = client.FRED_DATABASE

        
def InitialObject():
    a = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id=00XALCCZM086NEST&api_key=17188a6953269ab608ba14c3e3d8fb02&realtime_start=2013-08-14&observation_start=2013-08-14&frequency=m&file_type=json")
    output1 = json.loads(a.text)
    outputa = pd.DataFrame.from_dict(output1['observations'])
    del outputa["realtime_start"]
    del outputa["realtime_end"]
    outputa.head()
    try:
        outputa.rename(columns={'Date':'date','value':"00XALCCZM086NEST"}, inplace = 'True')
        # outputa.head()
        # outputc = dd.from_pandas(outputa, npartitions=10)
        return outputa  
    except Exception as e:
        print(e)


       
series_id = pd.read_csv("C:\\Users\\ricci\Desktop\\Projects\\FRED\\Months.csv",encoding = "ISO-8859-1")
series= []
for value in series_id["File"]:
    value = value.split(".csv")[0]
    value = value.rpartition("\\")[-1]
    series.append(value)


@asyncio.coroutine
def run(start, end):
    series_id = pd.read_csv("C:\\Users\\ricci\Desktop\\Projects\\FRED\\Months.csv",encoding = "ISO-8859-1")
    series= []
    for value in series_id["File"]:
        value = value.split(".csv")[0]
        value = value.rpartition("\\")[-1]
        series.append(value)

    outputc = InitialObject()
    #outputc = outputc.set_index('date', inplace=True)  
    for i in range(start,end):
        print(i)
        try:
            a = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id="+str(series[i])+"&api_key=17188a6953269ab608ba14c3e3d8fb02&realtime_start=2015-04-15&observation_start=2015-04-15&frequency=m&file_type=json")
            output1 = json.loads(a.text)
            #print(output1)
            try:
                outputa = pd.DataFrame.from_dict(output1['observations'])
                del outputa["realtime_start"]
                del outputa["realtime_end"]
                outputa = outputa.rename(columns={'date':'date1','value':str(series[i])})
                #outputa = outputa.set_index('date', inplace=True)
                outputc = pd.concat([outputc, outputa], axis=1)
                del outputc['date1']
                print(outputc.head())
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    outputc.to_csv("C:/Projects/finallysomebigdata" + str(start) + ".csv")
#Uncomment if below code is not working


# a = threading.Thread(target=run, args=(dask,dask + 50,))
# a.start()
# dask = dask + 1001

# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


# a = threading.Thread(target=run, args=(dask,dask + 1000,))
# a.start()
# dask = dask + 1001


loop = asyncio.get_event_loop()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[run(i, i+1) for i in range(1,100)]))
loop.close()
# loop.run_until_complete(asyncio.gather(
#     run(0, 1000),
#     #run(10, 20)
#     # run(20, 30),
#     # run(30, 40),
#     # run(40, 50),
#     ))
# loop.close()


data = pd.read_csv("C:\\Projects\\finallysomebigdata10.csv", skiprows=0)
data.reindex()
del data['Unnamed: 0']
data.head()
data
data.fillna(value=.1, inplace = True)
series1 = data['00XALCGBM086NEST']
data
data.reindex()
del data['date']
data = data.T
data.columns
s1 = pd.Series(series1.values, index=data.columns)
data.fillna(value=0,inplace=True)
df = (data.corrwith(s1, axis=1))
print(df.nlargest(n=5))
