import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from datetime import datetime
from bokeh.layouts import column, row
from pyproj import Proj, transform
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import HoverTool
import ipywidgets
from bokeh.io import push_notebook
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs

url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

try:
    df_potvrdeni=pd.read_csv(url_potvrdeni)
    df_umrli=pd.read_csv(url_umrli)
    df_oporavljeni=pd.read_csv(url_oporavljeni)

except:
    print('Something went wrong... URL problems')



# STUPAC Country/Region JE SADA INDEX

# POTVRDENI
df_grupirano_potvrdeni=df_potvrdeni.groupby('Country/Region').sum()
df_grupirano_potvrdeni_dates=df_grupirano_potvrdeni.iloc[:,2:]

# UMRLI
df_grupirano_umrli=df_umrli.groupby('Country/Region').sum()
df_grupirano_umrli_dates=df_grupirano_umrli.iloc[:,2:]

# OPORAVLJENI
df_grupirano_oporavljeni=df_oporavljeni.groupby('Country/Region').sum()
df_grupirano_oporavljeni_dates=df_grupirano_oporavljeni.iloc[:,2:]


#########################################################################################################

# POTVRDENI

potvrdeni_df_drz=df_grupirano_potvrdeni_dates.iloc[:,-1].sort_values(ascending=False).to_frame()
potvrdeni_df_drz.reset_index(inplace=True)
potvrdeni_df_drz2=potvrdeni_df_drz.iloc[:10,:]

lista_drzava_top10p=potvrdeni_df_drz2['Country/Region'].to_list()
lista_drzava_top10p_vr=potvrdeni_df_drz2.iloc[:,-1].to_list()

label=lista_drzava_top10p
value=lista_drzava_top10p_vr
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 6500000),
          title='TOP 10 država prema ukupnom broju zaraženih', tools=TOOLS)
p.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p.vbar(x=label, top=value , width=0.5, color = "blue")

p.background_fill_color="#fdffe3"
p.grid.grid_line_color="white"
p.xaxis.axis_label = 'Države'
p.yaxis.axis_label = 'Ukupan broj slučajeva'

first=Panel(child=row(p), title='Potvrdeni')

# UMRLI

umrli_df_drz=df_grupirano_umrli_dates.iloc[:,-1].sort_values(ascending=False).to_frame()
umrli_df_drz.reset_index(inplace=True)
umrli_df_drz2=umrli_df_drz.iloc[:10,:]

lista_drzava_top10u=umrli_df_drz2['Country/Region'].to_list()
lista_drzava_top10u_vr=umrli_df_drz2.iloc[:,-1].to_list()

label=lista_drzava_top10u
value=lista_drzava_top10u_vr
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p1= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 200000),
          title='TOP 10 država prema ukupnom broju umrlih', tools=TOOLS)
p1.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p1.vbar(x=label, top=value , width=0.5, color = "red")

p1.background_fill_color="#fdffe3"
p1.grid.grid_line_color="white"
p1.xaxis.axis_label = 'Države'
p1.yaxis.axis_label = 'Ukupan broj umrlih'

second=Panel(child=row(p1), title='Umrli')

# OPORAVLJENI

oporavljeni_df_drz=df_grupirano_oporavljeni_dates.iloc[:,-1].sort_values(ascending=False).to_frame()
oporavljeni_df_drz.reset_index(inplace=True)
oporavljeni_df_drz2=oporavljeni_df_drz.iloc[:10,:]

lista_drzava_top10o=oporavljeni_df_drz2['Country/Region'].to_list()
lista_drzava_top10o_vr=oporavljeni_df_drz2.iloc[:,-1].to_list()

label=lista_drzava_top10o
value=lista_drzava_top10o_vr
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p2= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 3500000),
          title='TOP 10 država prema ukupnom broju oporavljenih', tools=TOOLS)
p2.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p2.vbar(x=label, top=value , width=0.5, color = "green")

p2.background_fill_color="#fdffe3"
p2.grid.grid_line_color="white"
p2.xaxis.axis_label = 'Države'
p2.yaxis.axis_label = 'Ukupan broj oporavljenih'

third=Panel(child=row(p2), title='Oporavljeni')

# AKTIVNI
prvi=df_grupirano_potvrdeni_dates.iloc[:,-1].to_frame()
prvi.reset_index(inplace=True)
drugi=df_grupirano_umrli_dates.iloc[:,-1].to_frame()
drugi.reset_index(inplace=True)
treci=df_grupirano_oporavljeni_dates.iloc[:,-1].to_frame()
treci.reset_index(inplace=True)
aktivni=pd.DataFrame()
aktivni['Country/Region']=prvi['Country/Region']
aktivni['prvi']=prvi.iloc[:,-1]
aktivni['drugi']=drugi.iloc[:,-1]
aktivni['treci']=treci.iloc[:,-1]
aktivni['razlika']=aktivni['prvi']-aktivni['drugi']-aktivni['treci']
aktivni2=aktivni.loc[:,['Country/Region', 'razlika']]
aktivni3=aktivni2.sort_values('razlika', ascending=False)
aktivni3=aktivni3.iloc[:10,:]

lista_drzava_top10dnevnoak=aktivni3['Country/Region'].to_list()
lista_drzava_top10dnevnoakv=aktivni3['razlika'].to_list()

label=lista_drzava_top10dnevnoak
value=lista_drzava_top10dnevnoakv
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p3= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 3800000),
          title='TOP 10 država prema ukupnom broju aktivnih slučajeva', tools=TOOLS)
p3.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p3.vbar(x=label, top=value , width=0.5, color = "orange")

p3.background_fill_color="#fdffe3"
p3.grid.grid_line_color="white"
p3.xaxis.axis_label = 'Države'
p3.yaxis.axis_label = 'Ukupan broj aktivnih slučajeva'

fourth=Panel(child=row(p3), title='Aktivni')

# DNEVNO POTVRDENI
c=df_grupirano_potvrdeni_dates.columns[-1]
c1=df_grupirano_potvrdeni_dates.columns[-2]
potv_df=df_grupirano_potvrdeni_dates.iloc[:,-2:].sort_values(c,ascending=False)
potv_df.reset_index(inplace=True)
potv_df['Dnevni_novi']=potv_df[c]-potv_df[c1]
potv_df=potv_df.sort_values('Dnevni_novi',ascending=False)
potv_df=potv_df.loc[:,['Country/Region', 'Dnevni_novi']]
potv_df=potv_df.iloc[:10,:]

lista_drzava_top10dnevno=potv_df['Country/Region'].to_list()
lista_drzava_top10dnevnov=potv_df['Dnevni_novi'].to_list()

label=lista_drzava_top10dnevno
value=lista_drzava_top10dnevnov
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p4= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 80000),
          title='TOP 10 država prema ukupnom broju dnevno novih slučajeva', tools=TOOLS)
p4.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p4.vbar(x=label, top=value , width=0.5, color = "blue")

p4.background_fill_color="#fdffe3"
p4.grid.grid_line_color="white"
p4.xaxis.axis_label = 'Države'
p4.yaxis.axis_label = 'Ukupan broj dnevno novih slučajeva'

fifth=Panel(child=row(p4), title='Dnevno novih')

# DNEVNO UMRLI
d=df_grupirano_umrli_dates.columns[-1]
d1=df_grupirano_umrli_dates.columns[-2]
um_df=df_grupirano_umrli_dates.iloc[:,-2:].sort_values(d,ascending=False)
um_df.reset_index(inplace=True)
um_df['Dnevni_umrli']=um_df[d]-um_df[d1]
um_df=um_df.sort_values('Dnevni_umrli',ascending=False)
um_df=um_df.loc[:,['Country/Region', 'Dnevni_umrli']]
um_df=um_df.iloc[:10,:]

lista_drzava_top10dnevnoum=um_df['Country/Region'].to_list()
lista_drzava_top10dnevnoumv=um_df['Dnevni_umrli'].to_list()

label=lista_drzava_top10dnevnoum
value=lista_drzava_top10dnevnoumv
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p5= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 1500),
          title='TOP 10 država prema ukupnom broju dnevno umrlih', tools=TOOLS)
p5.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p5.vbar(x=label, top=value , width=0.5, color = "red")

p5.background_fill_color="#fdffe3"
p5.grid.grid_line_color="white"
p5.xaxis.axis_label = 'Države'
p5.yaxis.axis_label = 'Ukupan broj dnevno umrlih'

sixth=Panel(child=row(p5), title='Dnevno umrlih')

# DNEVNO OPORAVLJENI
e=df_grupirano_oporavljeni_dates.columns[-1]
e1=df_grupirano_oporavljeni_dates.columns[-2]
op_df=df_grupirano_oporavljeni_dates.iloc[:,-2:].sort_values(e,ascending=False)
op_df.reset_index(inplace=True)
op_df['Dnevni_oporavljeni']=op_df[e]-op_df[e1]
op_df=op_df.sort_values('Dnevni_oporavljeni',ascending=False)
op_df=op_df.loc[:,['Country/Region', 'Dnevni_oporavljeni']]
op_df=op_df.iloc[:10,:]

lista_drzava_top10dnevnoop=op_df['Country/Region'].to_list()
lista_drzava_top10dnevnoopv=op_df['Dnevni_oporavljeni'].to_list()

label=lista_drzava_top10dnevnoop
value=lista_drzava_top10dnevnoopv
TOOLS="pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p6= figure(plot_height=850, plot_width=1200, x_range=label, y_range=(0, 80000),
          title='TOP 10 država prema ukupnom broju dnevno oporavljenih', tools=TOOLS)
p6.xaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"
p6.vbar(x=label, top=value , width=0.5, color = "orange")

p6.background_fill_color="#fdffe3"
p6.grid.grid_line_color="white"
p6.xaxis.axis_label = 'Države'
p6.yaxis.axis_label = 'Ukupan broj dnevno oporavljenih'

seventh=Panel(child=row(p6), title='Dnevno oporavljenih')

tabs=Tabs(tabs=[first, second,third, fourth, fifth, sixth, seventh])
output_file('Project19_COVID19.html')

show(tabs)






##source=ColumnDataSource(data={
##    'x' : x_drzavni_potvrdeni_dates,
##    'broj' : ny})
##TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
##p_potvrdeni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
##                   title='Dnevne brojke novih slučajeva')
##p_potvrdeni.background_fill_color="#fdffe3"
##p_potvrdeni.grid.grid_line_color="white"
##p_potvrdeni.xaxis.axis_label = 'Date'
##p_potvrdeni.yaxis.axis_label = 'Broj novozaraženih'
##p_potvrdeni.axis.axis_line_color = None
##
##p_potvrdeni.line(x='x', y='broj', line_width=2, line_color='blue', source=source) # line_width=3
##p_potvrdeni.circle(x='x', y='broj', size=5,color='blue', fill_color='white', source=source) # line_width=3
##
##p_potvrdeni.add_tools(HoverTool(
##    tooltips=[
##        ('datum', '@x{%m/%d/%y}'),
##        ('broj', '@broj')],
##    formatters={
##        '@x':'datetime',
##        'broj':'numeral'},
##    mode='vline'))
##
############################################################################################
##
### UMRLI
##
### X OS
##x_drzavni_umrli=df_drzavni_umrli.index[-v5:].tolist()
##
### Y OS
##y_drzavni_umrli=[]
##for i in df_drzavni_umrli.iloc[-v5:].values:
##    for j in i:
##        y_drzavni_umrli.append(j)
##
##y_drzavni_umrli2=[]
##for i in df_drzavni_umrli.iloc[-v2:-1].values:
##    for j in i:
##        y_drzavni_umrli2.append(j)
##
##
### REVERSED 2 DEFINIRANE LISTE        
##yr=list(reversed(y_drzavni_umrli))
##print(list(yr))
##
##yrc=list(reversed(y_drzavni_umrli2))
##
### ZAPIS KAO ARRAY
##yra=np.array(yr)
##yrca=np.array(yrc)
##
###RAZLIKA 2 ARRAYA
##ny=yra-yrca
##print(ny)
##
### PREBACIVANJE U LISTU, OBRNUTA LISTA
##ny=list(reversed(ny))
##
##x_drzavni_umrli_dates=[]
##for s in x_drzavni_umrli: #'8/29/20'
##    x_drzavni_umrli_dates.append(datetime.strptime(s, '%m/%d/%y'))
##
##source1=ColumnDataSource(data={
##    'x' : x_drzavni_potvrdeni_dates,
##    'broj' : ny})
##
##p_umrli=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
##                   title='Dnevne brojke umrlih')
##p_umrli.background_fill_color="#fdffe3"
##p_umrli.grid.grid_line_color="white"
##p_umrli.xaxis.axis_label = 'Date'
##p_umrli.yaxis.axis_label = 'Broj umrlih'
##p_umrli.axis.axis_line_color = None
##
##p_umrli.circle(x='x', y='broj', size=5, fill_color='white' ,color='red', source=source1) # line_width=3
##
##p_umrli.vbar(x='x', top='broj', color='red', width=0.5,source=source1)
##p_umrli.y_range=Range1d(0,10)
##
##p_umrli.add_tools(HoverTool(
##    tooltips=[
##        ('datum', '@x{%m/%d/%y}'),
##        ('broj', '@broj')],
##    formatters={
##        '@x':'datetime',
##        'broj':'numeral'},
##    mode='vline'))
##
##
##
############################################################################################
##
### OPORAVLJENI
##
##
### X OS
##x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-v6:].tolist()
##
### Y OS
##y_drzavni_oporavljeni=[]
##for i in df_drzavni_oporavljeni.iloc[-v6:].values:
##    for j in i:
##        y_drzavni_oporavljeni.append(j)
##
##y_drzavni_oporavljeni2=[]
##for i in df_drzavni_oporavljeni.iloc[-v3:-1].values:
##    for j in i:
##        y_drzavni_oporavljeni2.append(j)
##
##
### REVERSED 2 DEFINIRANE LISTE        
##yr=list(reversed(y_drzavni_oporavljeni))
##print(list(yr))
##
##yrc=list(reversed(y_drzavni_oporavljeni2))
##
### ZAPIS KAO ARRAY
##yra=np.array(yr)
##yrca=np.array(yrc)
##
###RAZLIKA 2 ARRAYA
##ny=yra-yrca
##print(ny)
##
### PREBACIVANJE U LISTU, OBRNUTA LISTA
##ny=list(reversed(ny))
##
##x_drzavni_oporavljeni_dates=[]
##for s in x_drzavni_oporavljeni: #'8/29/20'
##    x_drzavni_oporavljeni_dates.append(datetime.strptime(s, '%m/%d/%y'))
##
##source2=ColumnDataSource(data={
##    'x' : x_drzavni_oporavljeni_dates,
##    'broj' : ny})
##
##p_oporavljeni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
##                   title='Dnevne brojke oporavljenih')
##p_oporavljeni.background_fill_color="#fdffe3"
##p_oporavljeni.grid.grid_line_color="white"
##p_oporavljeni.xaxis.axis_label = 'Date'
##p_oporavljeni.yaxis.axis_label = 'Broj oporavljenih'
##p_oporavljeni.axis.axis_line_color = None
##
##p_oporavljeni.line(x='x', y='broj', line_color='green',line_width=2, source=source2) # line_width=3
##p_oporavljeni.circle(x='x', y='broj', size=5,color='green', fill_color='white', source=source2) # line_width=3
##
##p_oporavljeni.add_tools(HoverTool(
##    tooltips=[
##        ('datum', '@x{%m/%d/%y}'),
##        ('broj', '@broj')],
##    formatters={
##        '@x':'datetime',
##        'broj':'numeral'},
##    mode='vline'))
##
##
############################################################################################
##
### AKTIVNI
##
### X OS
##x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-v4:].tolist()
##
### Y OS
##a=np.array(y_drzavni_potvrdeni)
##b=np.array(y_drzavni_umrli)
##c=np.array(y_drzavni_oporavljeni)
###print(a,b,c)
##y_aktivni=a-b-c
##
##x_drzavni_aktivni_dates=[]
##for s in x_drzavni_oporavljeni: #'8/29/20'
##    x_drzavni_aktivni_dates.append(datetime.strptime(s, '%m/%d/%y'))
##
##source3=ColumnDataSource(data={
##    'x' : x_drzavni_oporavljeni_dates,
##    'broj' : y_aktivni})
##
##p_aktivni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
##                   title='Dnevne brojke aktivnih slučajeva')
##p_aktivni.background_fill_color="#fdffe3"
##p_aktivni.grid.grid_line_color="white"
##p_aktivni.xaxis.axis_label = 'Date'
##p_aktivni.yaxis.axis_label = 'Broj aktivnih slučajeva'
##p_aktivni.axis.axis_line_color = None
##
##p_aktivni.line(x='x', y='broj', line_color='orange',line_width=2, source=source3) # line_width=3
##p_aktivni.circle(x='x', y='broj', size=5,color='orange', fill_color='white', source=source3) # line_width=3
##
##p_aktivni.add_tools(HoverTool(
##    tooltips=[
##        ('datum', '@x{%m/%d/%y}'),
##        ('broj', '@broj')],
##    formatters={
##        '@x':'datetime',
##        'broj':'numeral'},
##    mode='vline'))
##
##
##first=Panel(child=row(p_potvrdeni), title='Potvrdeni')
##second=Panel(child=row(p_umrli), title='Umrli')
##third=Panel(child=row(p_oporavljeni), title='Oporavljeni')
##fourth=Panel(child=row(p_aktivni), title='Aktivni')
##
##tabs=Tabs(tabs=[first, second,third, fourth])
##output_file('tabbed_countries.html')
##
##show(tabs)
