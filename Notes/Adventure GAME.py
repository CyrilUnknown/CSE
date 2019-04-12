class Room(object):
    def __init__(self, name, description="insert description", north=None, west=None, east=None, south=None,
                 up=None, down=None, item=None):
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        self.name = name
        self.description = description
        self.item = item


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the
        room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Knife(Weapon):
    def __init__(self, name, damage):
        super(Knife, self).__init__(name, damage)
        self.sharp = True
        self.durability = 10

    def attack(self):
        if self.sharp:
            self.durability -= 1
            if self.durability <= 0:
                self.sharp = False


class Handgun(Weapon):
    def __init__(self, name, damage):
        super(Handgun, self).__init__(name, damage)
        self.shoot = True
        self.durability = 20

    def attack(self):
        if self.shoot:
            self.durability -= 1
            if self.durability <= 0:
                self.shoot = False


class Bat(Weapon):
    def __init__(self, name, damage):
        super(Bat, self).__init__(name, damage)
        self.swing = True
        self.durability = 10

    def attack(self):
        if self.swing:
            self.durability -= 1
            if self.durability <= 0:
                self.swing = False


class KatanaSword(Weapon):
    def __init__(self, name, damage):
        super(KatanaSword, self).__init__(name, damage)
        self.swing = True


class ShotGun(Weapon):
    def __init__(self, name, damage):
        super(ShotGun, self).__init__(name, damage)
        self.shoot = True


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)
        self.Heal = True
        self.durability = 5

    def heal(self):
        if self.Heal:
            self.durability -= 1
            if self.durability <= 0:
                self.Heal = False


class Apple(Consumable):
    def __init__(self, name):
        super(Apple, self).__init__(name)
        self.eat = True
        self.durability = 6

    def eat(self):
        if self.eat:
            self.durability -= 1
            if self.durability <= 0:
                self.eat = False


class Drink(Consumable):
    def __init__(self, name):
        super(Drink, self).__init__(name)


class Gatorade(Drink):
    def __init__(self, name):
        super(Gatorade, self).__init__(name)
        self.durability = 6


class Soda(Drink):
    def __init__(self, name):
        super(Soda, self).__init__(name)
        self.durability = 6


class AppleJuice(Drink):
    def __init__(self, name):
        super(AppleJuice, self).__init__(name)
        self.durability = 6


class Water(Drink):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.durability = 6


class Pizza(Consumable):
    def __init__(self, name):
        super(Pizza, self).__init__(name)
        self.durability = 4
        self.eat = True

    def eat(self):
        if self.eat:
            self.durability -= 1
            if self.durability <= 0:
                self.eat = False


class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You Turn The Key and The Engine Start's")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


class Lamborghini(Car):
    def __init__(self):
        super(Lamborghini, self).__init__("Lamborghini")


class Van(Car):
    def __init__(self):
        super(Van, self).__init__("Van")


class AudiR8(Car):
    def __init__(self):
        super(AudiR8, self).__init__("Audi R8")


R19A = Room("Mr.Wiebe's room", "This is the room that you are in", None, "parking_lot", None, None, None, None)
parking_lot = Room("The Parking Lot", "There are a few cars parked here", "JOHNS_INCREDIBLE", 'R19A', None, None, None,
                   None, AudiR8())
JOHNS_INCREDIBLE = Room("Johns incredible pizza for kids","There are lots of things to do here", None,
                        None, "DARKROOM", "R19A", None, None)
DARKROOM = Room("The Dark room", "A room full of darkness", "MAZE", "JOHNS_INCREDIBLE", None, None, None, None)
MAZE = Room("The Maze room", "Don't get lost in the Maze", None, None, "FAZE_ROOM", "DARK_ROOM", None, None)
FAZE_ROOM = Room("Faze room", "Room that you can go through things", "LIGHT_ROOM", "MAZE", None, None)
LIGHT_ROOM = Room("Light room", "Search for people", None, "AIRPORT", None, "FAZE_ROOM", None, None)
AIRPORT = Room("Airport", "Go visit somewhere else", "GYM", None, "LIGHT_ROOM", None, None, None)
GYM = Room("Gym", "Workout Here", None, "HALLWAY", None, "AIRPORT", None, None)
HALLWAY = Room("Hallway", "Walk places here", None, None, "GYM", "MY_ROOM", None, None)
MY_ROOM = Room("MY room", "Hangout Here", "HALLWAY", "COMPUTER_ROOM", None, None, None, None)
COMPUTER_ROOM = Room("Computer room", "Search thing up or play games here", "TROPHY_ROOM", None, "MY_ROOM", None, None,
                     None)
TROPHY_ROOM = Room("Trophy room", "Store metals and trophy's here", None, "GARAGE", None, "COMPUTER_ROOM", None, None)
GARAGE = Room("Garage", "Put your car's in here", None, None, "TROPHY_ROOM", "LIVING_ROOM", None, None)
LIVING_ROOM = Room("Living room", "You use a living room everyday", "GARAGE", None, None, None, None, None)


player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']

playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")