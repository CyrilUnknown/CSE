world_map = {
    'R19A': {
        'NAME': "Mr.Wiebe's room",
        'DESCRIPTION': "This is the room that you are in",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    },
    'JOHNS_INCREDIBLE': {
        'NAME': "Johns incredible pizza for kids",
        'DESCRIPTION': "There are lots of things to do here",
        'PATHS': {
            'WEST': 'DARKROOM'
        }
    },
    'DARKROOM': {
        'NAME': "The Darkroom",
        'DESCRIPTION': "A room full of darkness",
        'PATHS': {
            'EAST': 'JOHNS_INCREDIBLE'
        }
    },
    'MAZE': {
        'NAME': "MAZE",
        'DESCRIPTION': "Don't get lost in the Maze",
        'Paths': {
            'SOUTHEAST': 'MAZE'
        }
    },
    'FazeRoom': {
        'NAME': "FazeRoom",
        'DESCRIPTION': "Room that you can go through things",
        'PATHS': {
            'EAST': 'MAZE'
        }
    },
    'LIGHT ROOM': {
        'NAME': "LIGHT ROOM",
        'DESCRIPTION': "Search for people",
        'PATHS': {
            'NORTHEAST': 'LIGHT ROOM'
        }
    },
    'AIRPORT': {
        'NAME': "AIRPORT",
        'DESCRIPTION': "Go visit somewhere else ",
        'PATHS': {
            'SOUTHWEST': 'AIRPORT'
        }
    },
    'GYM': {
        'NAME': "GYM",
        'DESCRIPTION': "Workout Here",
        'Paths': {
            'East': 'GYM'
        }
    },
    'HALLWAY': {
        'NAME': "Hallway",
        'DESCRIPTION': "Walk places here",
        'Paths': {
            'North'
        }
    },
    'My room': {
        'NAME': "My room",
        'DESCRIPTION': "Hangout Here",
        'Paths': {
            'Southwest'
        }
    },
    'Computer room': {
        'NAME': "Computer room",
        'DESCRIPTION': "Search thing up or play games here",
        'Paths': {
            'Southeast'
        }
    },
    'Trophy room': {
        'NAME': "Trophy room",
        'DESCRIPTION': "Store metals and trophy's here",
        'Paths': {

        }
    },
    ''
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