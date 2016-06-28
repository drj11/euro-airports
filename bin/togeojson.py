#!/usr/bin/env python3

import csv
import json
import sys

def main():
    features = []
    geo = dict(type='FeatureCollection',
      features=features)
    with open('airports.ussv') as u:
        airports = [row for row in csv.reader(u, delimiter='\037')]

    with open('routes.dat') as r:
        routes = [row for row in csv.reader(r)]

    # All airports that appear in some route
    sources = set(route[2] for route in routes)
    destinations = set(route[4] for route in routes)
    routed = sources | destinations

    print(len(airports))
    airports = [airport for airport in airports
      if airport[4] in routed or airport[5] in routed]
    print(len(airports))

    for row in airports:
        lat, lon = map(float, row[6:8])
        features.append(dict(type='Feature',
          geometry=dict(type='Point',
            coordinates=[lon, lat])))
    with open('airports.geojson', 'wb') as j:
        json.dump(geo, j)
            

if __name__ == '__main__':
    sys.exit(main())
