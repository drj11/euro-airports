#!/usr/bin/env python

import csv
import sys

def usage():
    sys.stderr.write(
      "rectangle-crop-airports.py --rectangle W,E,S,N\n")
    return 4

def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv

    rectangle = None
    opts,args = getopt.getopt(argv[1:], '', ['rectangle='])
    for o, v in opts:
        if o == '--rectangle':
            rectangle = v

    if rectangle is None:
        return usage()
    w,e,s,n = map(float, rectangle.split(','))

    with open('airports.dat', 'r') as f, \
      open('airports.ussv', 'w') as out:
        ussv = csv.writer(out, delimiter='\037')
        for row in csv.reader(f):
            lat, lon = map(float, row[6:8])
            if w <= lon < e and s <= lat < n:
                ussv.writerow(row)

if __name__ == '__main__':
    sys.exit(main())
