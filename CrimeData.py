# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 17:18:52 2019

@author: Quintero
"""

#Test1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfCrime = pd.read_csv('Crime_Data.csv', parse_dates=True)

#print(dfCrime['Report Number'])

dfCrime['Precinct'].value_counts()

#plot_data= dfCrime['Crime Subcategory']

#plot_data=plot_data.groupby['Neighborhood'].value_counts()

#plot_data.sort_values()[-10:].plot(kind='bar')
#plt.title("Top 10 Crimes")#

#dfCrime['Occurred Time'].plot(kind='hist', bins=100)
#plt.xlabel('Crime Precinct')

print(dfCrime['Occurred Date'].value_counts()[:10])#.sort_index(axis=0, ascending=False)

dfCrime_Date=dfCrime['Occurred Date']
#Newdf=dfCrime_Date.value_counts().sort_values(ascending=False)[:10]
#Newdf.plot(kind='bar')
plt.xlabel('Date')
plt.ylabel('Total of Crimes ocurred')
plt.title('Top ten dates')

#Newdf.to_csv('Test1.csv', encoding='utf-8')

#Reordered by date occurred
#print(dfCrime.sort_values(by='Occurred Date', ascending=False))







