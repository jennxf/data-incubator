from twython import Twython
import time
import math
import json
import pymongo
import folium
from itertools import izip


# loading it back into the Python interpreter's memory
def load_json(filename):
    with open(filename) as infile:
        data = json.load(infile)
    return data



fname  = 'tutorial_test_friends_profile.json'
# load the file back into python workspace 
test_reload = load_json(fname)


# fname  = 'tutorial_test_followers_profiles.json'



geo_enabled = [p['geo_enabled'] for p in test_reload]
# print geo_enabled
print geo_enabled.count(1), 'geo_enabled.count'


location = [p['location'] for p in test_reload]
# print location
print location.count(''), 'location count'


# print(set(location))

# time_zone = [p['time_zone'] for p in test_reload]
# print time_zone.count(None), 'time_zone.count(None)'
# print(set(time_zone)), 'time zone'

# status_geo = [p['status']['geo'] for p in test_reload if ('status' in p and p['status']['geo'] is not None)]
# if status_geo: print status_geo[0]
# print len(status_geo), 'len(status_geo)'

status_geo = []
status_geo_screen_names = []
#Only want tweets that are geo-tagged and have a screen-name
for fp in test_reload:
    if ('status' in fp and fp['status']['geo'] is not None and 'screen_name' in fp):
        status_geo.append(fp['status']['geo'])
        status_geo_screen_names.append(fp['screen_name'])

print status_geo
print status_geo_screen_names

map = folium.Map(location=[48, -90],zoom_start=5, tiles='Mapbox Control Room')

for sg, sn in izip(status_geo, status_geo_screen_names):
    print sg['coordinates'], str(sn)
    map.simple_marker(location=sg['coordinates'],popup=str(sn))

map.create_map(path='us_states.html')
