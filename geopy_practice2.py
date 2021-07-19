from geopy.geocoders import Nominatim
import json
import pprint

geolocator = Nominatim(user_agent="Your_Name")
location = geolocator.geocode("175 5th Avenue NYC")

# print(location.address)

# print((location.latitude, location.longitude))

pprint.pprint(location.raw)
