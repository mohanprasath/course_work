#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def inches_to_centi_meters(inches):
    centi_meters = inches * 2.54
    return centi_meters

def pounds_to_kilo_grams(pounds):
    kilo_grams = pounds * 0.453592 
    return kilo_grams

def strip(data):
    # TODO: Needs documentation
    # TODO: Needs verification
    """
    This function gets some data and convert it into string and it removes
     all the white spaces, newlines, tab spaces,
    carriage returns etc.
    """
    return str(data).strip(" ").strip("\r\t\n").strip("\r").\
        strip("\t").strip("\n")

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    SOURCE : STACKOVERFLOW
    http://stackoverflow.src/questions/15736995/how-can-i-quickly-estimate-
    the-distance-between-two-latitude-longitude-points
    100000 iterations in a minute
    :param lon1:
    :param lat1:
    :param lon2:
    :param lat2:
    :return km:
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c * 1000
    return km  # actually in meters