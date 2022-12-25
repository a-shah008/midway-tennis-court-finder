from app.models import TennisCourt
import math
# import googlemaps

# key = "AIzaSyAocmmtxjBtVRKkSrtKE6EOBi-KrtzMQrg"

# map_client = googlemaps.Client(key)

# distance = map_client.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

# print(distance)

# # response = map_client.geocode(address)
# # return pprint(response)

def get_coords(str):
    lat_long_list = []
    final_coords = []
    lat_long_list = str.split(", ")
    for item in lat_long_list:
        item = float(item)
        final_coords.append(item)

    return final_coords

def get_middle_coords(lat1, long1, lat2, long2):
    new_lat = (lat1 + lat2) / 2
    new_long = (long1 + long2) / 2

    return (new_lat, new_long)

def haversine(lat1, lon1, lat2, lon2):
     
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    km_to_mi = 0.621371
    return (rad * c) * km_to_mi

def get_distance_between(midpoint_coords):
    all_courts_db = TennisCourt.query.all()
    courts_with_distance = {}

    for court in all_courts_db:
        court_coords = court.coordinates.split(", ")
        final_court_coords = (float(court_coords[0]), float(court_coords[1]))
        mp_coords = (float(midpoint_coords[0]), float(midpoint_coords[1]))
        distance_between = haversine(final_court_coords[0], final_court_coords[1], mp_coords[0], mp_coords[1])

        courts_with_distance[court.name] = float(distance_between)

    return courts_with_distance

