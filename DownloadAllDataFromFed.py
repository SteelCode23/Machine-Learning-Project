#This script generates all the data

import multiprocessing
import pandas
import threading
import pandas as pd
from os import listdir
import os
import requests
import json
import asyncio
import urllib
import csv
import pdb
import ssl
import datetime


# engine = create_engine('postgresql://admin:admin@localhost:5433/postgres')
# conn = engine.connect()
# client = MongoClient()
# client = MongoClient('mongodb://localhost:27017/')
# db = client.FRED_DATABASE
# lm = LinearRegression()
# lm.fit(x, y)
# fc = zip(features, lm.coef_)
# list(fc)
# lm.score(x, y)


# #from string import rsplit
API_KEY = "17188a6953269ab608ba14c3e3d8fb02"
path = "C:/FREDDATA/somedata"

        
def InitialObject():
    a = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id=00XALCCZM086NEST&api_key=17188a6953269ab608ba14c3e3d8fb02&realtime_start=2013-08-14&observation_start=2013-08-14&frequency=m&file_type=json")
    output1 = json.loads(a.text)
    outputa = pd.DataFrame.from_dict(output1['observations'])
    del outputa["realtime_start"]
    del outputa["realtime_end"]
    outputa.head()
    try:
        outputa.rename(columns={'Date':'date','value':"00XALCCZM086NEST"}, inplace = 'True')
        return outputa  
    except Exception as e:
        print(e)


       
series_id = pd.read_csv("C:\\Users\\Steel\\Projects\\Stock-Predictor-master\\Months.csv",encoding = "ISO-8859-1")
series= []
for value in series_id["File"]:
    value = value.split(".csv")[0]
    value = value.rpartition("\\")[-1]
    series.append(value)


@asyncio.coroutine
def run(start, end):
    series_id = pd.read_csv("C:\\Users\\Steel\\Projects\\Stock-Predictor-master\\Months.csv",encoding = "ISO-8859-1")
    series= []
    for value in series_id["File"]:
        value = value.split(".csv")[0]
        value = value.rpartition("\\")[-1]
        series.append(value)

    outputc = InitialObject()
    #outputc = outputc.set_index('date', inplace=True)  
    for i in range(start,end):
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
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    outputc.to_csv("C:\\Users\\Steel\\Projects\\Stock-Predictor-master\\indicators2\\" + str(start) + ".csv")



# loop = asyncio.get_event_loop()
# #loop.run_until_complete(asyncio.gather(*[run(i, i+1) for i in range(1,100)]))
# loop.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
	run(1,400),
	run(401,800),
	run(801,1200),
	run(1201,1600),
	run(1601,2000),
	run(2001,2400),
	run(2401,2800),
	run(2801,3200),
	run(3201,3600),
	run(3601,4000),
	run(4001,4400),
	run(4401,4800),
	run(4801,5200),
	run(5201,5600),
	run(5601,6000),
	run(6001,6400),
	run(6401,6800),
	run(6801,7200),
	run(7201,7600),
	run(7601,8000),
	run(8001,8400),
	run(8401,8800),
	run(8801,9200),
	run(9201,9600),
	run(9601,10000),
	run(10001,10400),
	run(10401,10800),
	run(10801,11200),
	run(11201,11600),
	run(11601,12000),
	run(12001,12400),
	run(12401,12800),
	run(12801,13200),
	run(13201,13600),
	run(13601,14000),
	run(14001,14400),
	run(14401,14800),
	run(14801,15200),
	run(15201,15600),
	run(15601,16000),
	run(16001,16400),
	run(16401,16800),
	run(16801,17200),
	run(17201,17600),
	run(17601,18000),
	run(18001,18400),
	run(18401,18800),
	run(18801,19200),
	run(19201,19600),
	run(19601,20000),
	run(20001,20400),
	run(20401,20800),
	run(20801,21200),
	run(21201,21600),
	run(21601,22000),
	run(22001,22400),
	run(22401,22800),
	run(22801,23200),
	run(23201,23600),
	run(23601,24000),
	run(24001,24400),
	run(24401,24800),
	run(24801,25200),
	run(25201,25600),
	run(25601,26000),
	run(26001,26400),
	run(26401,26800),
	run(26801,27200),
	run(27201,27600),
	run(27601,28000),
	run(28001,28400),
	run(28401,28800),
	run(28801,29200),
	run(29201,29600),
	run(29601,30000),
	run(30001,30400),
	run(30401,30800),
	run(30801,31200),
	run(31201,31600),
	run(31601,32000),
	run(32001,32400),
	run(32401,32800),
	run(32801,33200),
	run(33201,33600),
	run(33601,34000),
	run(34001,34400),
	run(34401,34800),
	run(34801,35200),
	run(35201,35600),
	run(35601,36000),
	run(36001,36400),
	run(36401,36800),
	run(36801,37200),
	run(37201,37600),
	run(37601,38000),
	run(38001,38400),
	run(38401,38800),
	run(38801,39200),
	run(39201,39600),
	run(39601,40000),
	run(40001,40400),
	run(40401,40800),
	run(40801,41200),
	run(41201,41600),
	run(41601,42000),
	run(42001,42400),
	run(42401,42800),
	run(42801,43200),
	run(43201,43600),
	run(43601,44000),
	run(44001,44400),
	run(44401,44800),
	run(44801,45200),
	run(45201,45600),
	run(45601,46000),
	run(46001,46400),
	run(46401,46800),
	run(46801,47200),
	run(47201,47600),
	run(47601,48000),
	run(48001,48400),
	run(48401,48800),
	run(48801,49200),
	run(49201,49600),
	run(49601,50000),
	run(50001,50400),
	run(50401,50800),
	run(50801,51200),
	run(51201,51600),
	run(51601,52000),
	run(52001,52400),
	run(52401,52800),
	run(52801,53200),
	run(53201,53600),
	run(53601,54000),
	run(54001,54400),
	run(54401,54800),
	run(54801,55200),
	run(55201,55600),
	run(55601,56000),
	run(56001,56400),
	run(56401,56800),
	run(56801,57200),
	run(57201,57600),
	run(57601,58000),
	run(58001,58400),
	run(58401,58800),
	run(58801,59200),
	run(59201,59600),
	run(59601,60000),
	run(60001,60400),
	run(60401,60800),
	run(60801,61200),
	run(61201,61600),
	run(61601,62000),
	run(62001,62400),
	run(62401,62800),
	run(62801,63200),
	run(63201,63600),
	run(63601,64000),
	run(64001,64400),
	run(64401,64800),
	run(64801,65200),
	run(65201,65600),
	run(65601,66000),
	run(66001,66400),
	run(66401,66800),
	run(66801,67200),
	run(67201,67600),
	run(67601,68000),
	run(68001,68400),
	run(68401,68800),
	run(68801,69200),
	run(69201,69600),
	run(69601,70000),
	run(70001,70400),
	run(70401,70800),
	run(70801,71200),
	run(71201,71600),
	run(71601,72000),
	run(72001,72400),
	run(72401,72800),
	run(72801,73200),
	run(73201,73600),
	run(73601,74000),
	run(74001,74400),
	run(74401,74800),
	run(74801,75200),
	run(75201,75600),
	run(75601,76000),
	run(76001,76400),
	run(76401,76800),
	run(76801,77200),
	run(77201,77600),
	run(77601,78000),
	run(78001,78400),
	run(78401,78800),
	run(78801,79200),
	run(79201,79600),
	run(79601,80000),
	run(80001,80400),
	run(80401,80800),
	run(80801,81200),
	run(81201,81600),
	run(81601,82000),
	run(82001,82400),
	run(82401,82800),
	run(82801,83200),
	run(83201,83600),
	run(83601,84000),
	run(84001,84400),
	run(84401,84800),
	run(84801,85200),
	run(85201,85600),
	run(85601,86000),
	run(86001,86400),
	run(86401,86800),
	run(86801,87200),
	run(87201,87600),
	run(87601,88000),
	run(88001,88400),
	run(88401,88800),
	run(88801,89200),
	run(89201,89600),
	run(89601,90000),
	run(90001,90400),
	run(90401,90800),
	run(90801,91200),
	run(91201,91600),
	run(91601,92000),
	run(92001,92400),
	run(92401,92800),
	run(92801,93200),
	run(93201,93600),
	run(93601,94000),
	run(94001,94400),
	run(94401,94800),
	run(94801,95200),
	run(95201,95600),
	run(95601,96000),
	run(96001,96400),
	run(96401,96800),
	run(96801,97200),
	run(97201,97600),
	run(97601,98000),
	run(98001,98400),
	run(98401,98800),
	run(98801,99200),
	run(99201,99600),
	run(99601,100000)
    ))
loop.close()


import os
from os import listdir
outputc = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/501.csv")
try:
    del outputc['Unnamed: 0']
except Exception as e:
    print(e)
for i in os.listdir("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/"):
    data = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/" + str(i), skiprows=0)
    data['date1'] = data['date']
    try:
        del data['Unnamed: 0']
    except Exception as e:
        print(e)
    del data['date']
    outputc = pd.concat([outputc, data], axis=1)
    del outputc['date1']
    outputc.reindex()
outputc.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/finisheddata2.csv")
data = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/finisheddata2.csv")

#Handles Floating Point Error
def convertint(val):
    try:
        return round(val * 10,0)
    except:
        print('e')


print(data.columns)
#data to check correlations with
series1 = data['00XALCCZM086NEST']
data = data.T
s1 = pd.Series(series1.values, index=data.columns)
data = data.applymap(lambda x: convertint(x))
data.reindex()
df = data.corrwith(s1, axis =1)
print(df.nlargest(n=5))