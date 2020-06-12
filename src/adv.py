import sys
from typing import Dict, List
from controller import Controller
from room import Room
from player import Player
RoomDict = Dict[str, Room]

room: RoomDict = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

HELP_PROPMT = "Type 'help' for a list of commands"

def print_help():
    help_message = """To move in a cardinal direction type n, s, e or w
To pick up an item type 'get' or 'take' and then the name of the item"""
    print(help_message)

controller = Controller()

commands = {
    'n': controller.make_subject_mover('n'),
    's': controller.make_subject_mover('s'),
    'e': controller.make_subject_mover('e'),
    'w': controller.make_subject_mover('w'),
    'take': controller.take_item,
    'get': controller.take_item,
    'help': print_help,
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def run_repl():
    while True:
        raw_input: str = input('$> ')
        args: List[str] = raw_input.split(' ')
        try:
            if len(args) == 1:
                commands[args[0].lower()]()
            else:
                commands[args[0].lower()](args[1])
        except KeyError as error:
            print(f"{error} is not a valid command")
            print(HELP_PROPMT)
        except TypeError:
            print("I don't understand your command")
            print(HELP_PROPMT)

if __name__ == "__main__":
    staring_room = room['outside']
    player = Player('Patrick', room['outside'])
    controller.subject = player
    print(staring_room)
    try:
        run_repl()
    except KeyboardInterrupt:
        print()
        print('Thank you for playing')

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
