import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from folium.plugins import HeatMap
import folium
import warnings
warnings.filterwarnings('ignore')

# URL
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

# IMPORT DATA
try:
    df_potvrdeni=pd.read_csv(url_potvrdeni)
except:
    print('Something went wrong... URL problems')

# COLUMN Country/Region IS NOW INDEX

df_potvrdeni=df_potvrdeni.iloc[:,5:]
df_potvrdeni['Brojke_Dn']=df_potvrdeni.iloc[:,-1]-df_potvrdeni.iloc[:,-2]
df_potvrdeni['Brojke_Uk']=df_potvrdeni.iloc[:,-2]

#print(df_potvrdeni)
#print(df_potvrdeni.groupby('Province_State').count())

dnevno=df_potvrdeni.groupby(['Lat','Long_'])['Brojke_Dn'].sum().reset_index()
ukupno=df_potvrdeni.groupby(['Lat','Long_'])['Brojke_Uk'].sum().reset_index()

dnevno.columns=['Lat','Lon','Daily']
ukupno.columns=['Lat','Lon','Total']
dnevno=dnevno[(dnevno['Lat']!=0)&(dnevno['Lon']!=0)]
ukupno=ukupno[(ukupno['Lat']!=0)&(ukupno['Lon']!=0)]
print(dnevno)
print(ukupno)

basemap=folium.Map()
HeatMap(dnevno,zoom=20,radius=15).add_to(basemap)
basemap.save('daily.html')

basemap=folium.Map()
HeatMap(ukupno,zoom=20,radius=15).add_to(basemap)
basemap.save('total.html')
