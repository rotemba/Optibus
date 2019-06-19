
import utils
import data

vehiclesDict = {}
def initData():
    print("getting all locations")
    vehiclesLocation = data.getVehiclesLocation()
    for v in vehiclesLocation:
        vehiclesDict[v.id] = (v.rawLat, v.rawLong)


def reportVehicle(latitude, longitude ,vehicleId):
    vehiclesDict[vehicleId] = (latitude, longitude)


def vehiclesInRadius(lat,long,radius):

    print("creating list of all vehicle in Radius of %d kms from [%f,%f]" %(radius,lat,long))
    for v in vehiclesDict:
        distance = utils.computeDistanceBetweenTwoRawPoints(lat, long,vehiclesDict[v][0],vehiclesDict[v][1])
        if (distance<radius):
            print ("distance between [%f,%f] and Vehicle %d is: %0.2f KM" % (lat, long,v, distance))


def testBasic():
    print "running a basic test"
    pointLat = 31.705791
    pointLong = 35.200657
    vehiclesInRadius(pointLat, pointLong, 60)


def basics():
    initData()
    utils.printAllVehicles(vehiclesDict)
    testBasic()


# -------------- With Optimization --------------#

GridMin = 0
GridMax = 360

gridDict = {}
for lan in range(GridMin,GridMax):
    for long in range(GridMin,GridMax):
        gridDict[(lan,long)] = []




def initDataWithGridDict():
    print("initDataWithGridDict")
    vehiclesLocation = data.getVehiclesLocation()
    for v in vehiclesLocation:
        lat = (int)(v.rawLat)
        long = (int)(v.rawLong)
        if v.id in vehiclesDict:

            oldLat = (int)(vehiclesDict[v.id][0])
            oldLong = (int)(vehiclesDict[v.id][1])
            for car in gridDict[(oldLat,oldLong)]:
                if v.id == car.id:
                    gridDict[(oldLat, oldLong)].remove(car)
        gridDict[(lat,long)].append(v)
        vehiclesDict[v.id] = (v.rawLat, v.rawLong)


def printGridDict():
    print ("printing grid dictionary")
    for grid in gridDict:
        if (len(gridDict[grid])>0):
            print grid
        for v in gridDict[grid]:
            data.show(v)

# Computation of size of each grid according to the size of Earth..
GridHeight = 111
GridWidth = 93

def getAllPotentialGrids(lat,long,radius):
    relevantGrids = []
    upperLeftLat = (int)(lat)
    upperLeftLong = (int)(long)
    totalWidth = radius/GridWidth
    totalHeight = radius/GridHeight
    for lat1 in range (upperLeftLat-totalHeight-1,upperLeftLat+totalHeight+2):
        for long1 in range(upperLeftLong-totalWidth-1,upperLeftLong+totalWidth+2):
            gridLat = lat1
            gridLong = long1
            if (gridLat<GridMin):
                gridLat = gridLat + GridMax
            if (gridLat>=GridMax):
                gridLat = gridLat % GridMax
            if (gridLong<GridMin):
                gridLong = gridLong + GridMax
            if (gridLong>=GridMax):
                gridLong = gridLong % GridMax
            relevantGrids.append((gridLat,gridLong))
    return relevantGrids







def vehiclesInRadiusWithOptimization(lat,long,radius):

    print("creating list of all vehicle in Radius of %d kms from [%f,%f]" %(radius,lat,long))
    allPotentialGrids = getAllPotentialGrids(lat,long,radius)
    for grid in allPotentialGrids:
        for v in gridDict[grid]:
            # print ("will check now Vehicle %d " %v.id)
            distance = utils.computeDistanceBetweenTwoRawPoints(lat, long,v.rawLat,v.rawLong)

            # print ("distance between [%f,%f] and Vehicle %d in [%f,%f] is: %0.2f KM" % (lat, long, v.id, v.rawLat,v.rawLong, distance))
            if (distance < radius):
                print ("distance between [%f,%f] and Vehicle %d is: %0.2f KM" % (lat, long,v.id, distance))



def testOptimization():
    pointLat = 31.705791
    pointLong = 35.200657
    vehiclesInRadiusWithOptimization(pointLat, pointLong, 60)




def optimization():
    initDataWithGridDict()
    printGridDict()
    testOptimization()


# basics()
optimization()







