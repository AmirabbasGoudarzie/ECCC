import asyncio 
import nest_asyncio 
from env_canada import ECHistorical, get_historical_stations
import pandas as pd
 

# snipet to fix bug in asyncio 

nest_asyncio.apply() 
stns = asyncio.run(get_historical_stations([54.000000, -122.000000])) 
print(stns)


# search for stations, response contains station_ids
coordinates = [53.916944, -122.749444] # [lat, long]
coordinates_ON = [44, -80]

# coordinates: [lat, long]
# radius: km
# limit: response limit, value one of [10, 25, 50, 100]
# The result contains station names and ID values.
stations = asyncio.run(get_historical_stations(coordinates, radius=200, limit=100))
Ontario_Stations = asyncio.run(get_historical_stations(coordinates_ON, radius=200, limit = 100))

#ec_en_xml = ECHistorical(station_id=31688, year=2020, language="english", format="xml")
#ec_fr_xml = ECHistorical(station_id=31688, year=2020, language="french", format="xml")
ec_en_csv = ECHistorical(station_id=31688, year=2020, language="english", format="csv")
#ec_fr_csv = ECHistorical(station_id=31688, year=2020, language="french", format="csv")

# timeframe argument can be passed to change the granularity
# timeframe=1 hourly (need to create of for every month in that case, use ECHistoricalRange to handle it automatically)
# timeframe=2 daily (default)
ec_en_xml = ECHistorical(station_id=31688, year=2020, month=1, language="english", format="xml", timeframe=1)
ec_en_csv = ECHistorical(station_id=4413, year=1975, month=1, language="english", format="csv", timeframe=1)

asyncio.run(ec_en_xml.update())
asyncio.run(ec_en_csv.update())

# metadata describing the station
ec_en_xml.metadata

# historical weather data, in dictionary form
ec_en_xml.station_data

# csv-generated responses return csv-like station data

df = pd.read_csv(ec_en_csv.station_data)
print(df)