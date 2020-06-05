from room import Room
from player import Player
from item import Item

# Declare all the rooms

#items here?

items = {
    'kitten': Item("Kitten", "This friend makes the perfect companion!"),
    'puppy': Item("Puppy", "This friend makes the perfect companion!")
    }



#if else for movement? 

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['puppy']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['kitten']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# room['treasure'].items.append(items['kitten']) #second way to add items
# room['outside'].items.remove(items['kitten'])
# room['narrow'].list_items(items['puppy'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

newuser = Player('Kenzie', room['outside']) #cant use camelcase!

# Write a loop that:
# running = True
# while running:
while True: #has to be capital T for True
    print("\n")
#
# * Prints the current room name
    # print("\n")
    print("Player is in the room!\n", newuser.current_room.name)

# * Prints the current description (the textwrap module might be useful here).
    # print("\n")
    print(f'\nI think you are in', newuser.current_room.description)

# * Waits for user input and decides what to do.
    print("\n")
    command = input('Since you dont know what you are doing here are the directions, n is North, e is East, w is West, and s is South, and q is for Quitters')
    usercommand = command.lower().split(" ")
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if command == "q":
        print("\n")
        print("Quitter!")
        break #It terminates the current loop and resumes execution at the next statement

    elif command == "n" or command == "s" or command == "e" or command == "w":
        print("\n")
        # print("f {command} entered")
        newuser.move(command)
        print(f"\n {newuser.name} is in {newuser.current_room.name}\n {newuser.current_room.description} {newuser.current_room.list_items()}\n")
    else:
        # print("\n")
        print("Invalid command, please read the directions!")

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.