#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a
SET of the types that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

type([]) is list
type({}) is dict
type('') is str
type(0) is int

All the data initially is a string, so you have to do some checks on the values
first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    for field in fields:
        fieldtypes[field] = set()
    # YOUR CODE HERE
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):  # skip 4 rows
            reader.next()
        for row in reader:
            for field in fields:
                v = row[field]
                if v == "NULL" or v == "":
                    fieldtypes[field].add(type(None))
                elif v.startswith('{'):
                    fieldtypes[field].add(list)
                else:
                    try:
                        v = int(v)
                        fieldtypes[field].add(int)
                    except ValueError:
                        try:
                            v = float(v)
                            fieldtypes[field].add(float)
                        except ValueError:
                            fieldtypes[field].add(str)

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
