import pandas as pd 
import geopandas as gpd 
import os 
import numpy as np 

df_data = pd.read_csv("data/asset-ownership.csv")
df_shapefile = gpd.read_file("GeoJSON_Files/backup.geojson")
# df_shapefile = df_shapefile[df_shapefile["censuscode"] != 0]

del df_data["Name"]
df_data.columns = ["censuscode", "asset"]

df_shapefile = df_shapefile.merge(df_data, on="censuscode")

print(df_shapefile)

df_data = pd.read_csv("data/2001-change.csv")
df_data.columns = [x.lower() for x in df_data.columns]
del df_data["state"]
del df_data["name"]
df_data.columns = ["censuscode" if x == "district" else x for x in df_data.columns]
df_shapefile = df_shapefile.merge(df_data, on="censuscode", how="outer")

cols = list(df_shapefile)
cols.insert(len(cols)-1, cols.pop(cols.index('geometry')))
df_shapefile = df_shapefile.ix[:, cols]

print(df_shapefile)

df_shapefile.to_file(driver='GeoJSON', filename='GeoJSON_Files/main.geojson')