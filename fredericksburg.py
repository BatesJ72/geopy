from geopy.geocoders import Nominatim
import pandas as pd
 
geolocator = Nominatim(user_agent="Your_Name")

# location = geolocator.geocode("175 5th Avenue NYC")
# print((location.latitude, location.longitude))

# list = ['6120 US HWY 290 East, Fredericksburg, Texas 78624', '140 Augusta Vin Lane, Fredericksburg, Texas','5865 E, US-290, Fredericksburg, TX 78624']
# for i in list:
#     print(i)

df = pd.read_csv('fredericksburg_original.csv')
# print(df)

# df['long'] = ''
# df['lat'] = ''

# for x in range(len(df)):
#     geocode_result = geolocator.geocode(df['Addresss'][x])
#     df['lat'][x] -  geocode_result[0][location][latitude]
#     df['long'][x] -  geocode_result[0][location][longitude]

df["loc"] = df["Address"].apply(geolocator.geocode)
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)

try:
    df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)
except ValueError:
    pass

data = df['point'].str.split(",", n = 1, expand = True)
# df['lat'] = data[0]
# df['long'] = data[1]
# df['altitude'] = data[2]


print(data)


# df.to_csv('fredericksburg_with_lat_long.csv')