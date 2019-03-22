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


R19A = Room("Mr. William's Room", "INSERT DESCRIPTION HERE")
parking_Lot = Room("The Parking Lot", None, R19A)
R19A.north = parking_Lot

# Option 2 - Use strings, but more difficult controller

# R19A = Room("Mr. Wiebe's Room")
# parking_Lot = Room("The Parking Lot", None, "R19A")
# JOHNS_INCREDIBLE = Room("Johns Incredible", "There are lots of things to do here", None,)

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