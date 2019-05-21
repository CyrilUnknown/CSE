class Room(object):
    def __init__(self, name, description="insert description", north=None, west=None, east=None, south=None,
                 up=None, down=None):
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        self.name = name
        self.description = description
        self.item = []
        self.enemies = []


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location
        self.weapon = None

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

    def attack(self, target):
        print("You attack the %s for %i damage" % (target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Item(object):
    def __init__(self, name):
        self.name = name
        self.picked_up = False


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.name = name

    def grab(self):
        player.inventory.append(self)
        print("You grabbed the %s" % self.name)


class Enemy(object):
    def __init__(self, name, starting_location=None):
        self.health = 150
        self.inventory = []
        self.name = name

    def take_damage(self, damage):
        self.health -= damage
        print("The %s has %i health left" % (self.name, self.health))


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


class Katanasword(Weapon):
    def __init__(self, name, damage):
        super(Katanasword, self).__init__(name, damage)
        self.swing = True


none = Katanasword("", 100)


class Flashlight(Weapon):
    def __init__(self, name, damage):
        super(Flashlight, self).__init__(name, damage)
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


R19A = Room("You are in the mansion", "", None, "parking_lot", None, None, None, None,
            )
parking_lot = Room("This is the parking lot of the mansion", "There are a few cars parked here", "JOHNS_INCREDIBLE",
                   'R19A', None, None, None,
                   None, )
JOHNS_INCREDIBLE = Room("You are at John's Incredible Pizza", "The Bear outfit is on the floor and there is old pizza",
                        None, None, "DARKROOM", "R19A", None, None)
DARKROOM = Room("You are at the Dark room", "I can barely see anything here ", "MAZE", "JOHNS_INCREDIBLE", None, None,
                None, None)
MAZE = Room("You are at the Maze room", "Don't get lost in the Maze", None, None, "FAZE_ROOM", "DARK_ROOM", None, None)
FAZE_ROOM = Room("Faze room", "Room that you can go through things", "LIGHT_ROOM", "MAZE", None, None)
LIGHT_ROOM = Room("Light room", "Search for people", None, "AIRPORT", None, "FAZE_ROOM", None, None)
AIRPORT = Room("Airport", "Go visit somewhere else", "GYM", None, "LIGHT_ROOM", None, None, None)
GYM = Room("Gym", "Workout Here", None, "HALLWAY", None, "AIRPORT", None, None)
HALLWAY = Room("Hallway", "Walk places here", None, None, "GYM", "MY_ROOM", None, None)
MY_ROOM = Room("MY room", "Hangout Here", "HALLWAY", "COMPUTER_ROOM", None, None, None, None)
COMPUTER_ROOM = Room("Computer room", "Search thing up or play games here", "TROPHY_ROOM", None, "MY_ROOM", None, None,
                     None)
TROPHY_ROOM = Room("Trophy room", "Store metals and trophy's here", None, "GARAGE", None, "COMPUTER_ROOM", None, None,
                   )
GARAGE = Room("Garage", "Put your car's in here", None, None, "TROPHY_ROOM", "LIVING_ROOM", None, None)
LIVING_ROOM = Room("Living room", "You use a living room everyday", "GARAGE", None, None, None, None, None)

Car = AudiR8()

parking_lot.item.append(Car)

Gun = Handgun("Handgun", 25)

LIVING_ROOM.item.append(Gun)

Car = [Lamborghini, Viper, Van]

GARAGE.item.append(Car)

Gun = ShotGun("Remington 870", 60)

TROPHY_ROOM.item.append(Gun)

Weapon2 = Katanasword("Katana Sword", 100)

MY_ROOM.item.append(Weapon)

Melee_Weapon = Bat("Baseball Bat", 50)

Consumable2 = AppleJuice("AppleJuice")

AIRPORT.item.append(Consumable2)

Consumable3 = Pizza("Pepperoni Pizza")

JOHNS_INCREDIBLE.item.append(Consumable3)

Weapon3 = Flashlight("FlashLight", 10)

JOHNS_INCREDIBLE.item.append(Weapon3)

player = Player(R19A)

player.weapon = Melee_Weapon

Consumable4 = Soda("Mountain Dew Soda")

GYM.item.append(Consumable4)

zombie = Enemy("Bomb Zombie", R19A)

zombie2 = Enemy("Running Zombie", JOHNS_INCREDIBLE)

zombie3 = Enemy("Legless Zombie", DARKROOM)

zombie4 = Enemy("Acid Bomb Zombie", AIRPORT)

zombie5 = Enemy("Smart Zombie", COMPUTER_ROOM)

zombie6 = Enemy("Faceless Zombie", HALLWAY)

zombie7 = Enemy("Boss Zombie", LIVING_ROOM)

none2 = Enemy("")

R19A.enemies.append(zombie)

JOHNS_INCREDIBLE.enemies.append(zombie2)

DARKROOM.enemies.append(zombie3)

AIRPORT.enemies.append(zombie4)

COMPUTER_ROOM.enemies.append(zombie5)

HALLWAY.enemies.append(zombie6)

LIVING_ROOM.enemies.append(zombie7)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
shorter_directions = ['n', 's', 'e', 'w', 'u', 'd']

playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if len(player.current_location.item) > 0:
        print("The following items are in this room:")
        for item in player.current_location.item:
            print(item.name)

    if len(player.current_location.enemies) > 0:
        print("The following enemies are here:")
        for enemy in player.current_location.enemies:
            print(enemy.name)
            print()
    command = input(">>")
    if command in shorter_directions:
        pos = shorter_directions.index(command)
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    if 'attack ' in command.lower():
        targets_name = command[7:]

        target = None
        for enemies in player.current_location.enemies:
            print(enemies.name)
            if enemies.name.lower() == targets_name.lower():
                target = enemies
                player.attack(target)
        if target is not None and target.health <= 0:
            player.current_location.enemies.remove(target)
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")

    elif "grab " in command.lower():
        if player.current_location.item is not None:
            item_name = command[5:]
            item_found = None
            for items in player.current_location.item:
                if items.name.lower() == item_name.lower():
                    item_found = items
                    if item_found is not None:
                        try:
                            item_found.grab()
                            player.current_location.item.remove(item_found)
                            print()
                        except AttributeError:
                            print("I can't grab this")

    else:
        print("Command not recognized.")