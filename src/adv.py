import sys
from typing import Dict, List
from room import Room

# Declare all the rooms
room: Dict[str, Room] = {
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

def foo():
    pass

def print_help():
    help_message = f"""To move in a cardinal direction type n, s, e or w
To pick up an item type 'get' or 'take' and then the name of the item"""
    print(help_message)

commands = {
    'n': foo,
    's': foo,
    'e': foo,
    'w': foo,
    'take': foo,
    'get': foo,
    'help': print_help,
}

help_prompt = "Type 'help' for a list of commands"

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


if __name__ == "__main__":
    raw_input: str
    args: List[str]
    try:
        while True:
            raw_input = input('$> ')
            args = raw_input.split(' ')
            try:
                if len(args) == 1:
                    commands[args[0].lower()]()
                else:
                    commands[args[0].lower()](args[1])
            except KeyError as error:
                print(f"{error} is not a valid command")
                print(help_prompt)
            except TypeError:
                print("I don't understand your command")
                print(help_prompt)
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
