class Room(object):
    def __init__(self, name, description, north=None, west=None, east=None, south=None, up=None, down=None,):
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        self.name = name
        self.description = description


class Player(object):
    def __init__(self, starting_locating):
        self.health = 100
        self.inventory = []
        self.current_location = starting_locating


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100


R19A = Room("Mr. William's Room", "INSERT DESCRIPTION HERE")

parking_Lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_Lot