import pandas as pd 
import geopandas as gpd 
import os 
import numpy as np 

df_shapefile = gpd.read_file("GeoJSON_Files/Shape Files/2011/2011_Dist.shp")
df_shapefile = gpd.read_file("GeoJSON_Files/backup.geojson")

# Create GeoJSON files for the 2011 Census asset ownership labels!!

df_data = pd.read_csv("data/asset-ownership.csv")
del df_data["Name"]
df_data.columns = ["censuscode", "asset"]

df_shapefile = df_shapefile.merge(df_data, on="censuscode")

print(df_shapefile)

# Create GeoJSON files for the 2011 labels, 2001 labels, and the change labels!!

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

# Create GeoJSON files for the spatial labels!!

df_data = pd.read_csv("data/clustering-labels.csv")
df_data.columns = [x.lower() for x in df_data.columns]
del df_data["unnamed: 0"]
df_data.columns = ["censuscode" if x == "district" else x for x in df_data.columns]
df_data.columns = [x+"_spatial" if x != "censuscode" else x for x in df_data.columns]
df_shapefile = df_shapefile.merge(df_data, on="censuscode", how="outer")

cols = list(df_shapefile)
cols.insert(len(cols)-1, cols.pop(cols.index('geometry')))
df_shapefile = df_shapefile.ix[:, cols]

print(df_shapefile)

df_shapefile.to_file(driver='GeoJSON', filename='GeoJSON_Files/main-2.geojson')