# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# URL OF CSV
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# LOAD DATA
try:
    df_potvrdeni=pd.read_csv(url_potvrdeni) # NEW CASES
    df_umrli=pd.read_csv(url_umrli) # DEATHS
    df_oporavljeni=pd.read_csv(url_oporavljeni) # RECOVERED

except:
    print('Something went wrong... URL problems')

# EXTRACT "CROATIA" ROW
df_potvrdeni_Croatia=df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia']
df_potvrdeni_Croatia_dates=df_potvrdeni_Croatia.iloc[:,4:]

# EXTRACT "SERBIA" ROW
df_potvrdeni_Serbia=df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Serbia']
df_potvrdeni_Serbia_dates=df_potvrdeni_Serbia.iloc[:,4:]

# EXTRACT "SLOVENIA" ROW
df_potvrdeni_Slovenia=df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Slovenia']
df_potvrdeni_Slovenia_dates=df_potvrdeni_Slovenia.iloc[:,4:]

# GRAPH - TOTAL CASES
# DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
x_cro_potvrdeni=df_potvrdeni_Croatia_dates.columns[-82:].tolist()
x_ser_potvrdeni=df_potvrdeni_Serbia_dates.columns[-82:].tolist()
x_slo_potvrdeni=df_potvrdeni_Slovenia_dates.columns[-82:].tolist()

# DEFINING Y
y_cro_potvrdeni=[]
for i in df_potvrdeni_Croatia_dates.iloc[:,-82:].values:
    for j in i:
        y_cro_potvrdeni.append(j)

# DEFINING Y
y_ser_potvrdeni=[]
for i in df_potvrdeni_Serbia_dates.iloc[:,-82:].values:
    for j in i:
        y_ser_potvrdeni.append(j)

# DEFINING Y
y_slo_potvrdeni=[]
for i in df_potvrdeni_Slovenia_dates.iloc[:,-82:].values:
    for j in i:
        y_slo_potvrdeni.append(j)

plt.figure(figsize=(20,12))
plt.plot(x_cro_potvrdeni,y_cro_potvrdeni, label="Croatia")
plt.plot(x_ser_potvrdeni,y_ser_potvrdeni, label="Serbia")
plt.plot(x_slo_potvrdeni,y_slo_potvrdeni, label="Slovenia")
plt.xticks(rotation='vertical')
plt.title('TOTAL NUMBER OF CONFIRMED CASES')
plt.grid()
plt.legend()
plt.xticks(x_cro_potvrdeni[::2])
plt.show()


# GRAPH - DAILY CASES
# X IS THE SAME
# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
# COLUMNS FROM -31,-1
y_cro_potvrdeni2=[]
for i in df_potvrdeni_Croatia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_cro_potvrdeni2.append(j)

# REVERSED LISTS        
yr=list(reversed(y_cro_potvrdeni))

yrc=list(reversed(y_cro_potvrdeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAA
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

###
y_ser_potvrdeni2=[]
for i in df_potvrdeni_Serbia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_ser_potvrdeni2.append(j)

# REVERSED LISTS        
yr2=list(reversed(y_ser_potvrdeni))

yrc2=list(reversed(y_ser_potvrdeni2))

# TO ARRAY
yra2=np.array(yr2)
yrca2=np.array(yrc2)

# DIFFERENCE 2 ARRAYAA
ny2=yra2-yrca2

# TO LIST, REVERSED
ny2=list(reversed(ny2))
###

###
y_slo_potvrdeni2=[]
for i in df_potvrdeni_Slovenia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_slo_potvrdeni2.append(j)

# REVERSED LISTS        
yr3=list(reversed(y_slo_potvrdeni))

yrc3=list(reversed(y_slo_potvrdeni2))

# TO ARRAY
yra3=np.array(yr3)
yrca3=np.array(yrc3)

# DIFFERENCE 2 ARRAYAA
ny3=yra3-yrca3

# TO LIST, REVERSED
ny3=list(reversed(ny3))
###

plt.figure(figsize=(20,12))
plt.plot(x_cro_potvrdeni,ny, label="Croatia")
plt.plot(x_ser_potvrdeni,ny2, label="Serbia")
plt.plot(x_slo_potvrdeni,ny3, label="Slovenia")
plt.xticks(x_cro_potvrdeni[::2],rotation='vertical')
plt.title('CONFIRMED CASES - DAILY NUMBERS')
plt.grid()
plt.legend()
plt.show()


##############################################################################################################################################################

df_umrli_Croatia=df_umrli.loc[df_umrli['Country/Region']=='Croatia']
df_umrli_Croatia_dates=df_umrli_Croatia.iloc[:,4:]

df_umrli_Serbia=df_umrli.loc[df_umrli['Country/Region']=='Serbia']
df_umrli_Serbia_dates=df_umrli_Serbia.iloc[:,4:]

df_umrli_Slovenia=df_umrli.loc[df_umrli['Country/Region']=='Slovenia']
df_umrli_Slovenia_dates=df_umrli_Slovenia.iloc[:,4:]

# GRAF - TOTAL DEATHS
# DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
x_cro_umrli=df_umrli_Croatia_dates.columns[-82:].tolist()
x_ser_umrli=df_umrli_Serbia_dates.columns[-82:].tolist()
x_slo_umrli=df_umrli_Slovenia_dates.columns[-82:].tolist()

# DEFINING Y
y_cro_umrli=[]
for i in df_umrli_Croatia_dates.iloc[:,-82:].values:
    for j in i:
        y_cro_umrli.append(j)

# DEFINING Y
y_ser_umrli=[]
for i in df_umrli_Serbia_dates.iloc[:,-82:].values:
    for j in i:
        y_ser_umrli.append(j)

# DEFINING Y
y_slo_umrli=[]
for i in df_umrli_Slovenia_dates.iloc[:,-82:].values:
    for j in i:
        y_slo_umrli.append(j)


plt.figure(figsize=(20,12))
plt.plot(x_cro_umrli,y_cro_umrli, label="Croatia")
plt.plot(x_ser_umrli,y_ser_umrli, label="Serbia")
plt.plot(x_slo_umrli,y_slo_umrli, label="Slovenia")
plt.xticks(rotation='vertical')
plt.title('TOTAL NUMBER OF DEATHS')
plt.grid()
plt.legend()
plt.xticks(x_cro_umrli[::2])
plt.show()


# GRAPH - DAILY CASES
# X REMAINS THE SAME
# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
y_cro_umrli2=[]
for i in df_umrli_Croatia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_cro_umrli2.append(j)

# REVERSED 2 LISTS        
yr=list(reversed(y_cro_umrli))
yrc=list(reversed(y_cro_umrli2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
y_ser_umrli2=[]
for i in df_umrli_Serbia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_ser_umrli2.append(j)

# REVERSED 2 LISTS        
yr2=list(reversed(y_ser_umrli))
yrc2=list(reversed(y_ser_umrli2))

# TO ARRAY
yra2=np.array(yr2)
yrca2=np.array(yrc2)

# DIFFERENCE 2 ARRAYAS
ny2=yra2-yrca2

# TO LIST, REVERSED
ny2=list(reversed(ny2))

# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
y_slo_umrli2=[]
for i in df_umrli_Slovenia_dates.iloc[:,-83:-1].values:
    for j in i:
        y_slo_umrli2.append(j)

# REVERSED 2 LISTS        
yr3=list(reversed(y_slo_umrli))
yrc3=list(reversed(y_slo_umrli2))

# TO ARRAY
yra3=np.array(yr3)
yrca3=np.array(yrc3)

# DIFFERENCE 2 ARRAYAS
ny3=yra3-yrca3

# TO LIST, REVERSED
ny3=list(reversed(ny3))

plt.figure(figsize=(20,12))
plt.plot(x_cro_umrli,ny, label="Croatia")
plt.plot(x_ser_umrli,ny2, label="Serbia")
plt.plot(x_slo_umrli,ny3, label="Slovenia")
plt.xticks(x_cro_umrli[::2],rotation='vertical')
plt.title('DAILY NUMBER OF DEATHS')
plt.grid()
plt.legend()
plt.show()

###################################################

xl=["Croatia","Serbia","Slovenia"]

ycro=df_potvrdeni_Croatia_dates.iloc[:,-1].values-df_potvrdeni_Croatia_dates.iloc[:,-82].values
print(ycro[0])
yser=df_potvrdeni_Serbia_dates.iloc[:,-1].values-df_potvrdeni_Serbia_dates.iloc[:,-82].values
print(yser[0])
yslo=df_potvrdeni_Slovenia_dates.iloc[:,-1].values-df_potvrdeni_Slovenia_dates.iloc[:,-82].values
print(yslo[0])

yl=[ycro[0], yser[0], yslo[0]]

plt.bar(xl,yl, edgecolor="black", color=["#0006ff","#0091ff","#00fff7"])
plt.title("TOTAL NUMBER OF NEW CASES (LAST 82 DAYS)")
plt.show()

xl=["Croatia","Serbia","Slovenia"]

ycro=df_umrli_Croatia_dates.iloc[:,-1].values-df_umrli_Croatia_dates.iloc[:,-82].values
print(ycro[0])
yser=df_umrli_Serbia_dates.iloc[:,-1].values-df_umrli_Serbia_dates.iloc[:,-82].values
print(yser[0])
yslo=df_umrli_Slovenia_dates.iloc[:,-1].values-df_umrli_Slovenia_dates.iloc[:,-82].values
print(yslo[0])

yl=[ycro[0], yser[0], yslo[0]]

plt.bar(xl,yl, edgecolor="black", color=["#540000","#ff0000","#ff7878"])
plt.title("TOTAL NUMBER OF DEATHS (LAST 82 DAYS)")
plt.show()
##############################################################################################################################################################

##df_oporavljeni_Croatia=df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia']
##df_oporavljeni_Croatia_dates=df_oporavljeni_Croatia.iloc[:,4:]
##
### GRAPH - TOTAL RECOVERED
### DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
##x_cro_oporavljeni=df_oporavljeni_Croatia_dates.columns[-82:].tolist()
##
### DEFINING Y
##y_cro_oporavljeni=[]
##for i in df_oporavljeni_Croatia_dates.iloc[:,-82:].values:
##    for j in i:
##        y_cro_oporavljeni.append(j)
##
##plt.figure(figsize=(20,12))
##plt.plot(x_cro_oporavljeni,y_cro_oporavljeni, marker='.', color='green')
##plt.xticks(rotation='vertical')
##plt.title('NUMBER OF RECOVERED - TOTAL')
##plt.grid()
##plt.xticks(x_cro_oporavljeni[::2])
##plt.show()
##
##
### GRAPH - DAILY CASES
### X REMAINS THE SAME
### DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
##y_cro_oporavljeni2=[]
##for i in df_oporavljeni_Croatia_dates.iloc[:,-83:-1].values:
##    for j in i:
##        y_cro_oporavljeni2.append(j)
##
### REVERSED 2 LISTS        
##yr=list(reversed(y_cro_oporavljeni))
##yrc=list(reversed(y_cro_oporavljeni2))
##
### TO ARRAY
##yra=np.array(yr)
##yrca=np.array(yrc)
##
### DIFFERENCE 2 ARRAYAS
##ny=yra-yrca
##
### TO LIST, REVERSED
##ny=list(reversed(ny))
##
##plt.figure(figsize=(20,12))
##plt.plot(x_cro_oporavljeni,ny, marker='.', color='green')
##plt.xticks(x_cro_oporavljeni[::2],rotation='vertical')
##plt.title('DAILY NUMBER OF RECOVERED')
##plt.grid()
##plt.show()


##############################################################################################################################################################

### GRAPH - ACTIVE CASES LAST 30 DAYS
### DEFINING X (SAME)
##x_cro_oporavljeni=df_oporavljeni_Croatia_dates.columns[-82:].tolist()
##
### DEFINING Y : NEW CASES - DEATHS - RECOVERED
##y_cro_potvrdeni=[] # NEW CASES
##for i in df_potvrdeni_Croatia_dates.iloc[:,-82:].values:
##    for j in i:
##        y_cro_potvrdeni.append(j)
##        
##y_cro_oporavljeni=[] # DEATHS
##for i in df_oporavljeni_Croatia_dates.iloc[:,-82:].values:
##    for j in i:
##        y_cro_oporavljeni.append(j)
##
##y_cro_umrli=[] # RECOVERED
##for i in df_umrli_Croatia_dates.iloc[:,-82:].values:
##    for j in i:
##        y_cro_umrli.append(j)
##
##
##a=np.array(y_cro_potvrdeni)
##b=np.array(y_cro_oporavljeni)
##c=np.array(y_cro_umrli)
##y=a-b-c
##
##plt.figure(figsize=(20,12))
##plt.plot(x_cro_oporavljeni,y, marker='.', color='orange')
##plt.xticks(rotation='vertical')
##plt.title('ACTIVE CASES')
##plt.grid()
##plt.xticks(x_cro_oporavljeni[::2])
##plt.show()
