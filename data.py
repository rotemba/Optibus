from math import radians

class Vehicle:
  def __init__(self, id, lat, long):
    self.id = id
    self.lat = radians(lat)
    self.long = radians(long)
    self.rawLat =lat
    self.rawLong = long


def show(vehicle):
        print("Vehicle %d - location [%f,%f]" %(vehicle.id,vehicle.rawLat,vehicle.rawLong))


# Ra'anana, Israel (32.184448, 34.870766)
# Bethlehem, Israel (31.705791, 35.200657)
# Ashdod, Israel (31.801447, 34.643497)
# Nazareth, Israel (32.699635, 35.303547)
# Bat Yam, Tel-Aviv, Israel (32.017136, 34.745441)
# Tel Aviv-Yafo, Israel (32.109333, 34.855499)
# Haifa, Israel (32.794044, 34.989571)
# Karmiel, Israel (32.919945, 35.290146)
# Herzliya, Tel-Aviv, Israel (32.166313, 34.843311)
# Rehovot, Israel (31.894756, 34.809322)



v1 = Vehicle(1,32.184448, 34.870766)
v2 = Vehicle(2,31.705791, 35.200657)
v3 = Vehicle(3,31.801447, 34.643497)
v4 = Vehicle(4,32.109333, 34.855499)
v5 = Vehicle(5,32.919945, 35.290146)
v6 = Vehicle(6,32.699635, 35.303547)
v7 = Vehicle(1,31.894756, 34.809322)
v8 = Vehicle(5,32.184448, 34.870766)
v9 = Vehicle(7,33.000000, 33.000000)
v10 =Vehicle(8,34.000000, 34.000000)

vehiclesLocation = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]

def getVehiclesLocation():
    return vehiclesLocation
