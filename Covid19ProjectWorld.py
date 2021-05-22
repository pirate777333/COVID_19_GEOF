import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from folium.plugins import HeatMap
import folium

worldometer=pd.read_csv('D:/udemy_kurs_py/DataScienceProjects/Project4/Covid-19/worldometer_data.csv')

print(worldometer.head())
print(worldometer.isnull().sum())
print(worldometer.dtypes)
print(worldometer.describe())
print(worldometer.shape)
print(worldometer.columns)

# ANALYSIS BY COUNTRY

worldometer=worldometer.sort_values(by='TotalCases', ascending=False)
topTotalCase=worldometer.iloc[:10,:]
fig=px.bar(topTotalCase,x='Country/Region',y='TotalCases',color='Country/Region',
           template='plotly_dark',title='Top Total Cases')
fig.show()

worldometer=worldometer.sort_values(by='TotalDeaths', ascending=False)
topTotalDeaths=worldometer.iloc[:10,:]
fig=px.bar(topTotalDeaths,x='Country/Region',y='TotalDeaths',color='Country/Region',
           template='plotly_dark',title='Top Total Deaths')
fig.show()

worldometer=worldometer.sort_values(by='TotalRecovered', ascending=False)
topTotalRecovered=worldometer.iloc[:10,:]
fig=px.bar(topTotalRecovered,x='Country/Region',y='TotalRecovered',color='Country/Region',
           template='plotly_dark',title='Top Total Recovered')
fig.show()

worldometer=worldometer.sort_values(by='ActiveCases', ascending=False)
topActiveCases=worldometer.iloc[:10,:]
fig=px.bar(topActiveCases,x='Country/Region',y='ActiveCases',color='Country/Region',
           template='plotly_dark',title='Top Active Cases')
fig.show()

# DAILY ANALYSIS

daily=pd.read_csv('D:/udemy_kurs_py/DataScienceProjects/Project4/Covid-19/day_wise.csv', parse_dates=['Date'])

print(daily.head())
print(daily.isnull().sum())
print(daily.dtypes)
print(daily.describe())
print(daily.shape)
print(daily.columns)

columns=['Confirmed','Deaths','Recovered','Active']

for i in columns:
    fig=px.line(daily, x='Date', y=i, template='plotly_dark', title=i)
    fig.show()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=daily.Date,
    y=daily.Confirmed,
    name = 'Confirmed',
    mode='lines'
))
fig.add_trace(go.Scatter(
    x=daily.Date,
    y=daily.Active,
    name='Active',
    mode='lines'       
))
fig.update_layout(template='plotly_dark', title='Confirmed vs Active')
fig.show()


# Population vs Total Tests

worldometer['Pop_TotTst']=worldometer['Population']/worldometer['TotalTests']

worldometer=worldometer.sort_values(by='Pop_TotTst', ascending=False)
Pop_TotTst=worldometer.iloc[:10,:]
fig=px.bar(Pop_TotTst,x='Country/Region',y='Pop_TotTst',color='Country/Region',
           template='plotly_dark',title='Top Population / Test ratio')
fig.show()

# CRITICAL CASES

worldometer=worldometer.sort_values(by='Serious,Critical', ascending=False)
SerCrit=worldometer.iloc[:10,:]
fig=px.bar(SerCrit,x='Country/Region',y='Serious,Critical',color='Country/Region',
           template='plotly_dark',title='Top Worst affected')
fig.show()

stupci=['Tot Cases/1M pop','Deaths/1M pop']

for i in stupci:
    bad=worldometer.sort_values(by=i, ascending=False)
    bad=bad.iloc[:10,:]
    fig=px.bar(bad,x=i,y='Country/Region',color=i,
           template='plotly_dark',title=i)
    fig.show()

# PICK A COUNTRY

def get_stats(country):
        
    cdf=worldometer[worldometer['Country/Region']==country]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=cdf['Country/Region'],
        y=cdf.TotalCases,
        name = 'Total Cases'
    ))
    fig.add_trace(go.Bar(
        x=cdf['Country/Region'],
        y=cdf.TotalDeaths,
        name='Total Deaths'      
    ))
    fig.add_trace(go.Bar(
        x=cdf['Country/Region'],
        y=cdf.TotalRecovered,
        name='Total Recovered'      
    ))
    fig.add_trace(go.Bar(
        x=cdf['Country/Region'],
        y=cdf.ActiveCases,
        name='Active Cases'      
    ))
    fig.update_layout(template='plotly_dark', title='Stats for '+country)
    fig.show()

a=input('Pick a Country:  ')
get_stats(a)
