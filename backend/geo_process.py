from geo_code import *
import os

"""
Input: None
Output: JSON of people and their locations
"""

def geo_location(profile):
    country = profile['country']
    location = profile['location']
    return location + ', ' + country

def name(profile):
    return profile['name']

def load_json(file_name):
    try:
        json_object = json.loads(open(file_name, 'r').read())
    except ValueError, e:
        return False
    return json_object

def main():
    res = {}
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    raw_dir = cur_dir + '/../data/raw/'
    for f in os.listdir(raw_dir):
        profile = load_json(raw_dir + f)
        if profile:
            location = geo_code(geo_location(profile))
            res.update({name(profile): location})
    print json.dumps(res)

if __name__ == "__main__":
    main()
