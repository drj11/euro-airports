#!/usr/bin/env python3

import csv
import json
import sys

def main():
    features = []
    geo = dict(type='FeatureCollection',
      features=features)
    with open('airports.ussv') as u:
        for row in csv.reader(u, delimiter='\037'):
            print(row)
            lat, lon = map(float, row[6:8])
            features.append(dict(type='Feature',
              geometry=dict(type='Point',
                coordinates=[lon, lat])))
    with open('airports.geojson', 'wb') as j:
        json.dump(geo, j)
            

if __name__ == '__main__':
    sys.exit(main())
