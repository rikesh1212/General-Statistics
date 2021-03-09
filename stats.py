import pandas as pd
import numpy as np

print("Enter rolling window \t")
i = int(input())

df = pd.read_csv("GOOG.csv")
df['Date'] = pd.to_datetime(df['Date'],format='%Y/%m/%d')

def myinp(i,dataframe,datecol):
    freq_d = {'m':'m','w':'U'}
    return dataframe.groupby(dataframe[datecol]
          .dt.strftime(f"%{freq_d.get(i)}").rename(i)).mean()

if(i==20):
    print("Mean")
    print("By month: \n",myinp('m',df,'Date'))
elif(i==5):
    print("Mean")
    print("By week: \n",myinp('w',df,'Date'))
else:
    print("Rolling window out of range")


def myinp2(i,dataframe,datecol):
    freq_d = {'m': 'm', 'w': 'U'}
    return dataframe.groupby(dataframe[datecol]
                             .dt.strftime(f"%{freq_d.get(i)}").rename(i)).std()
if(i==20):
    print("Standard deviation")
    print("By month: \n",myinp2('m',df,'Date'))
elif(i==5):
    print("Standard deviation")
    print("By week: \n",myinp2('w',df,'Date'))


def myinp3(i,dataframe,datecol):
    freq_d = {'m': 'm', 'w': 'U'}
    return dataframe.groupby(dataframe[datecol]
                             .dt.strftime(f"%{freq_d.get(i)}").rename(i)).median()
if(i==20):
    print("Median")
    print("By month: \n",myinp3('m',df,'Date'))
elif(i==5):
    print("Median")
    print("By week: \n",myinp3('w',df,'Date'))


def myinp4(i,dataframe,datecol):
    freq_d = {'m': 'm', 'w': 'U'}
    return dataframe.groupby(dataframe[datecol]
                             .dt.strftime(f"%{freq_d.get(i)}").rename(i)).agg(['min','max'])
if(i==20):
    print("Range")
    print("By month: \n",myinp4('m',df,'Date'))
elif(i==5):
    print("Range")
    print("By week: \n",myinp4('w',df,'Date'))












