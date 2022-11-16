#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research
   Features: Additional rooms, move counter, room description with directions, and sword to kill monster"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom  + '. ' + rooms[currentRoom]['desc'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'desc' : 'A long dark hall where the lights flicker alternately. you can go north, east, or south',
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'north' : 'Guest Bedroom',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'desc' : 'A beutiful kitchen, newly furnished with stainless steel appliances...What is that smell?! You can go north',
                  'north' : 'Hall',
                  'item' : 'monster',
                },

            'Dining Room' : {
                    'desc' : 'A beautiful dining room with a table to fit 8 lovely souls.. I mean people. You can go north, west, or south',
                    'west' : 'Hall',
                    'south' : 'Garden',
                    'north' : 'Master Bedroom',
                    'item' : 'potion'
                },
            
            'Garden' : {
                'desc' : 'The smell of fresh air hits. This may be the way out!',
                'north' : 'Dining Room',
            },

            'Guest Bedroom' : {
                'desc' : 'A quaint bedroom with wooden bedframe and one dresser. You can go east or south',
                'south' : 'Hall',
                'east' : 'Master Bedroom'
            },

            'Master Bedroom' : {
                'desc' : 'A room truly for a master. You can go west or south',
                'west' : 'Guest Bedroom',
                'south' : 'Dining Room',
                'item' : 'sword'
            }

         }

# start the player in the Hall
currentRoom = 'Hall'

# move counter
moves = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # increase move counter when player moves through the rooms
            moves += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        # if player picks up the coat rack, they have the ability to fight the monster.
        if 'sword' in inventory:
            print('You fought off the monster with the sword! Good job!\nNow go back the way you came!')
        else:
            print('A monster has got you... GAME OVER!')
            print(f"You made {moves} moves in the game!")
            break  

    #player wins is they get to the garden with the key and potion
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        print(f"You made {moves} moves in the game!")
        break
