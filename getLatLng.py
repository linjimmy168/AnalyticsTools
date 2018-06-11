import googlemaps
import json
from datetime import datetime

class GetLat:
    def getLat(self,address):
        gmaps = googlemaps.Client(key='AIzaSyBKumMFEjcnysGwtImlFJ-xxXWeAYHQKs8')
        add = address

        geocode_result = gmaps.geocode(add)
        try:
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            return lat,lng
        except:
            pass

 



