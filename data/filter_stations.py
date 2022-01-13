import pandas as pd

metro_lines = pd.read_csv('metro_lines.csv', sep=';')
stations = pd.read_csv('mvv_stations.csv', sep=';').rename(columns={'Name ohne Ort': 'station_name'})
stations = stations[stations['Ort'].isin(['München', 'Garching (b München)'])]
# stations['station_name'] = stations['station_name'].astype(str)

print(metro_lines)
print(stations)

metro_stations = set(metro_lines['station_name'])

index = stations['station_name'].isin(metro_stations)
stations = stations[index]

stations['WGS84 X'] = stations['WGS84 X'].str.replace(',', '.')
stations['WGS84 Y'] = stations['WGS84 Y'].str.replace(',', '.')

# remaining = set(metro_stations) - set(stations['station_name'])
# print(remaining)
print(stations)

stations[['station_name', 'WGS84 X', 'WGS84 Y']].to_csv('metro_stations.csv', sep=';', index=False)
