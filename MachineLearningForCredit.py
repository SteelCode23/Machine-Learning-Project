import pandas
import matplotlib

import os
import tarfile
from six.moves import urllib
import xlrd
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def load_housing_data(housing_path=HOUSING_PATH):
    ContractAnalysis2016 = pd.read_excel("C:\\Users\\ricci\\Desktop\\Projects\\Machine Learning\\ContractAnalysis2016.xlsx")    
    return ContractAnalysis2016
    
data = pd.get_dummies(housing)
data.describe()
%matplotlib inline
import matplotlib.pyplot as plt
data.hist(bins=50, figsize=(20,15))
plt.show()
import numpy as np

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
    
import hashlib

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]\
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(train_set)
housing = strat_train_set.copy()
housing.plot(kind="scatter", x="longitude", y="latitude")

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
from pandas.tools.plotting import scatter_matrix
attributes = ["DaystoCash", "Store", "AGE",
              "income_cat"]
scatter_matrix(housing[attributes], figsize=(12, 8))
corr_matrix = housing.corr()
print(corr_matrix)
