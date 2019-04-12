world_map = {
    'R19A': {
        'NAME': "Mr.Wiebe's room",
        'DESCRIPTION': "This is the room that you are in",
        'PATHS': {
            'WEST': 'PARKING_LOT'
        }
    },
    'PARKING_LOT': {
        "NAME": "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here",
        'PATHS': {
            'NORTH': 'JOHNS_INCREDIBLE',
            'EAST': 'R19A'
        }
    },
    'JOHNS_INCREDIBLE': {
        'NAME': "Johns incredible pizza for kids",
        'DESCRIPTION': "There are lots of things to do here",
        'PATHS': {
            'EAST': 'DARKROOM',
            'SOUTH': 'R19A'
        }
    },
    'DARKROOM': {
        'NAME': "The Darkroom",
        'DESCRIPTION': "A room full of darkness",
        'PATHS': {
            'NORTH': 'MAZE',
            'WEST': "JOHNS_INCREDIBLE"
        }
    },
    'MAZE': {
        'NAME': "MAZE",
        'DESCRIPTION': "Don't get lost in the Maze",
        'Paths': {
            'EAST': "FAZE_ROOM",
            'SOUTH': "DARKROOM"
        }
    },
    'FAZE_ROOM': {
        'NAME': "FAZE_ROOM",
        'DESCRIPTION': "Room that you can go through things",
        'PATHS': {
            'NORTH': "LIGHT_ROOM",
            'WEST': "MAZE"
        }
    },
    'LIGHT_ROOM': {
        'NAME': "LIGHT ROOM",
        'DESCRIPTION': "Search for people",
        'PATHS': {
            'WEST': "AIRPORT",
            'SOUTH': "FAZE_ROOM"
        }
    },
    '': {
        'NAME': "AIRPORT",
        'DESCRIPTION': "Go visit somewhere else",
        'PATHS': {
            'NORTH': "GYM",
            'EAST': "LIGHT_ROOM"
        }
    },
    'GYM': {
        'NAME': "GYM",
        'DESCRIPTION': "Workout Here",
        'PATHS': {
            'WEST': "HALLWAY",
            'SOUTH': "AIRPORT"
        }
    },
    'HALLWAY': {
        'NAME': "Hallway",
        'DESCRIPTION': "Walk places here",
        'PATHS': {
            'SOUTH': "MY_ROOM",
            'EAST': "GYM"
        }
    },
    'MY_ROOM': {
        'NAME': "My room",
        'DESCRIPTION': "Hangout Here",
        'PATHS': {
            'WEST': "COMPUTER_ROOM",
            'NORTH': "HALLWAY"
        }
    },
    'COMPUTER_ROOM': {
        'NAME': "Computer room",
        'DESCRIPTION': "Search thing up or play games here",
        'PATHS': {
            'NORTH': "TROPHY_ROOM",
            'EAST': "MY_ROOM"
        }
    },
    'TROPHY_ROOM': {
        'NAME': "Trophy room",
        'DESCRIPTION': "Store metals and trophy's here",
        'PATHS': {
            'WEST': "GARAGE",
            'SOUTH': "COMPUTER_ROOM"
        }
    },
    'GARAGE': {
        'NAME': "Garage",
        'DESCRIPTION': "Put your car's in here",
        'PATHS': {
            'SOUTH': "LIVING_ROOM",
            'EAST': "TROPHY_ROOM"
        }
    },
    'LIVING_ROOM': {
        'NAME': "Living room",
        'DESCRIPTION': "You use a living room everyday",
        'PATHS': {
            'NORTH': "GARAGE"
        }
    }
}
# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]  # This is your current location
playing = True
#  Controller
while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command.lower() in['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognize")