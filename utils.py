from math import sin, cos, sqrt, atan2,radians
from data import Vehicle
import data

# approximate radius of earth in km
R = 6373.0


def computeDistanceBetweenTwoPoints(lat1,lon1,lat2,lon2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def computeDistanceBetweenTwoRawPoints(lat1,lon1,lat2,lon2):
    return computeDistanceBetweenTwoPoints(radians(lat1),radians(lon1),radians(lat2),radians(lon2))

def computeDistanceBetweenPointAndCar(pointLat,pointLon,car):
    return computeDistanceBetweenTwoPoints(radians(pointLat),radians(pointLon),car.lat,car.long)

def printAllVehicles(vehiclesDict):
    print ("going to write all known vehicles")
    for v in vehiclesDict:
        print ("ID: %d, location:(lat,long)" % v)
        print vehiclesDict[v]

