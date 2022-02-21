import pandas as pd

lines = pd.read_csv('metro_lines.csv', sep=';')
stations = pd.read_csv('metro_stations.csv', sep=';')

pairs = []

last_index = -1
last_row = None
for index, row in lines.iterrows():
    if index == 0:
        last_index = index
        last_row = row
        continue
    if last_row['line name'] == row['line name']:
        old_station_id = stations.index[stations['station_name'] == last_row['station_name']].tolist()[0]
        station_id = stations.index[stations['station_name'] == row['station_name']].tolist()[0]
        item = [min(station_id, old_station_id), max(station_id, old_station_id)]
        if item not in pairs:
            pairs.append(item)

    last_index = index
    last_row = row

pairs_df = pd.DataFrame(pairs)
pairs_df.to_csv("metro_connections.csv", sep=';', index=False, header=False)
print(pairs)
