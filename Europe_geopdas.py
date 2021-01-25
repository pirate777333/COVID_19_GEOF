import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

df=df.groupby("Country/Region").sum()

df=df.drop(columns=["Lat","Long"])

df_t=df.T

world_map=gpd.read_file("C:/Users/Josko/Desktop/GeoViz/esej/Europe_Map.shp")

world_map.replace("Viet Nam","Vietnam",inplace=True)
world_map.replace("Brunei Darussalam","Brunei",inplace=True)
world_map.replace("Cape Verde","Cabo Verde",inplace=True)
world_map.replace("Democratic Republic of the Congo","Congo (Kinshasa)",inplace=True)
world_map.replace("Congo","Congo (Brazzaville)",inplace=True)
world_map.replace("Czech Republic","Czechia",inplace=True)
world_map.replace("Swaziland","Eswatini",inplace=True)
world_map.replace("Iran (Islamic Republic of)","Iran",inplace=True)
world_map.replace("Korea, Republic of","Korea, South",inplace=True)
world_map.replace("Lao People's Democratic Republic","Laos",inplace=True)
world_map.replace("Libyan Arab Jamahiriya","Libya",inplace=True)
world_map.replace("Republic of Moldova","Moldova",inplace=True)
world_map.replace("The former Yugoslav Republic of Macedonia","North Macedonia",inplace=True)
world_map.replace("Syrian Arab Republic","Syria",inplace=True)
world_map.replace("Taiwan","Taiwan*",inplace=True)
world_map.replace("United Republic of Tanzania","Tanzania",inplace=True)
world_map.replace("United States","US",inplace=True)
world_map.replace("Palestine","West Bank and Gaza",inplace=True)

merge=world_map.join(df,on="NAME", how="right")
    
ax=merge.plot(column="12/10/20",
              cmap="OrRd",
              figsize=(15,15),
              legend=True,
              scheme="user_defined",
              classification_kwds={"bins":[500,1000,10000,50000,100000,500000,1000000,5000000]},
              edgecolor="black",
              linewidth=0.5)
ax.set_title("Total Confirmed COVID-19 Cases", fontdict={'fontsize':20})

ax.set_axis_off()

ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

plt.show()
