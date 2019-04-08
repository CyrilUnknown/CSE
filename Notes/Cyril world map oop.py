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

    def move(self, new_location):
        """

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the
        room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)
        # getattr(R19A, "north")

# These are the instances of the rooms (Instantiation)


R19A = Room("Mr.Wiebe's room", "This is the room that you are in", None, "PARKING_LOT", None, None, None, None)
parking_lot = Room("The Parking Lot", "There are a few cars parked here", "john", R19A)
JOHNS_INCREDIBLE = Room("Johns incredible pizza for kids","There are lots of things to do here", None, "JOHNS_INCREDIBLE", None, None, None, None)
DARKROOM = Room("The Dark room", "A room full of darkness", None, "DARKROOM", None, None, None, None)
MAZE = Room("The Maze room", "Don't get lost in the Maze", None, "Maze", None, None, None, None)
FAZE_ROOM = Room("Faze room", "Room that you can go through things", None, "FAZE_ROOM", None, None, None, None)
LIGHT_ROOM = Room("Light room", "Search for people", None, "LIGHT_ROOM", None, None, None, None)
AIRPORT = Room("Airport", "Go visit somewhere else", None, "AIRPORT", None, None, None, None)
GYM = Room("Gym", "Workout Here", None, "GYM", None, None, None, None)
HALLWAY = Room("Hallway", "Walk places here", None, "HALLWAY", None, None, None, None)
MY_ROOM = Room("MY room", "Hangout Here", None, "MY_ROOM", None, None, None, None)
COMPUTER_ROOM = Room("Computer room", "Search thing up or play games here", None, "COMPUTER_ROOM", None, None, None, None)
TROPHY_ROOM = Room("Trophy room", "Store metals and trophy's here", None, "TROPHY_ROOM", None, None, None, None)
GARAGE = Room("Garage", "Put your car's in here", None, "Garage", None, None, None, None)
LIVING_ROOM = Room("Living room", "You use a living room everyday", None, "LIVING_ROOM", None, None, None, None)

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']

playing = True
#  Controller
while playing:
    print(player.current_location.name)# player is object of
    # the player class data
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognize")