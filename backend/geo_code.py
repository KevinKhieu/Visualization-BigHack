import urllib
import json
import sys

"""
Input: Single address query command line argument
Output: JSON with fields: lat, lng, location_type, formatted_address
"""

def url(address, return_call = "json", sensor = "false"):
    root = "http://maps.google.com/maps/api/geocode/"
    query = "?" + urllib.urlencode({"address": address, "sensor": sensor})
    return root + return_call +  query

def geo_code(address, verbose = False):
    if verbose: print address
    u = url(address)
    doc = urllib.urlopen(u).read()
    x = json.loads(doc)
    if x['status'] == "OK":
        lat = x['results'][0]['geometry']['location']['lat']
        lng = x['results'][0]['geometry']['location']['lng']
        location_type = x['results'][0]['geometry']['location_type']
        formatted_address = x['results'][0]['formatted_address']
        return {'lat': lat, 'lng': lng, 'location_type': location_type,
            'formatted_address': formatted_address}
    else:
        return {'lat': None, 'lng': None, 'location_type': None,
            'formatted_address': None}

def main(argv):
    if len(argv) > 0:
        address = argv[0]
    else:
        address = "unknown"
    print json.dumps(geo_code(address))

if __name__ == "__main__":
    main(sys.argv[1:])
    
