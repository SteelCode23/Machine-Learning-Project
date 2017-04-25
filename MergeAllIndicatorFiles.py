import os
import pandas as pd
from os import listdir
outputc = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/501.csv")
try:
    del outputc['Unnamed: 0']
except Exception as e:
    print(e)
for i in os.listdir("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/"):
    data = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/" + str(i), skiprows=0)
    try:
        outputc = pd.merge(data, outputc, how = 'outer')
    except Exception as e:
        outputc.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators2/"+str(i)+"checkpoint.csv")
        outputc =  pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/501.csv")
#     outputc.reindex()
outputc.to_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/finisheddata2.csv")
data = pd.read_csv("C:/Users/Steel/Projects/Stock-Predictor-master/indicators/finisheddata2.csv")
