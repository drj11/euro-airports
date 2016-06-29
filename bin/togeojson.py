#!/usr/bin/env python3

import csv
import json
import sys

from collections import namedtuple

Airport = namedtuple("Airport",
  "index name city country code icao latitude longitude altitude timezone dst tz")

def main():
    features = []
    geo = dict(type='FeatureCollection',
      features=features)
    with open('airports.ussv') as u:
        airports = [row for row in csv.reader(u, delimiter='\037')]

    with open('routes.dat') as r:
        routes = [row for row in csv.reader(r)]

    # All airport codes that appear in some route
    sources = set(route[2] for route in routes)
    destinations = set(route[4] for route in routes)
    routed = sources | destinations

    # Filter airports to only those that have routes
    print(len(airports))
    airports = [airport for airport in airports
      if airport[4] in routed]
    print(len(airports))

    # Convert lat/lon to numeric.
    for row in airports:
        row[6] = float(row[6])
        row[7] = float(row[7])

    # Convert to namedtuple
    airports = [Airport(*row) for row in airports]

    airport_dict = {airport.code: airport for airport in airports}


    for row in airports:
        features.append(dict(type='Feature',
          geometry=dict(type='Point',
            coordinates=[row.longitude, row.latitude])))
    with open('airports.geojson', 'wb') as j:
        json.dump(geo, j)
            

if __name__ == '__main__':
    sys.exit(main())
