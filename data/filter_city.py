import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# % matplotlib inline

# Make sure you read postal codes as strings, otherwise
# the postal code 01110 will be parsed as the number 1110.
plz_shape_df = gpd.read_file('./plz-gebiete.shp', dtype={'plz': str})

# print(plz_shape_df.head())

plz_einwohner_df = pd.read_csv(
    './plz_einwohner.csv',
    sep=',',
    dtype={'plz': str, 'einwohner': int}
)
plz_region_df = pd.read_csv(
    './zuordnung_plz_ort.csv',
    sep=',',
    dtype={'plz': str}
)

plz_region_df.drop('osm_id', axis=1, inplace=True)

germany_df = pd.merge(
    left=plz_shape_df,
    right=plz_region_df,
    on='plz',
    how='inner'
)

germany_df.drop(['note'], axis=1, inplace=True)

# Merge data.
germany_df = pd.merge(
    left=germany_df,
    right=plz_einwohner_df,
    on='plz',
    how='left'
)

pd.set_option('display.max_columns', None)
# print(germany_df.head())

# cities in germany
# print(set(germany_df['ort']))
city_name = 'München'
city_df = germany_df[germany_df['ort'] == city_name].reset_index()
# print(city_df.head())
print(city_df)

# todo update population data

city_df.to_csv('munich.csv', sep=';', index=False)
