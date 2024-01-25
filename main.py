import os
import random

# from PIL import Image

# map = Image.open("themazerunner.png")
# map.show()


# Clears screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Menu
def prompt():

    print("\t\t\tWelcome To The Maze Runner Game\n\n\
        Moves:\t'go {direction}'(travel North, South, East, or West)\n\
        \t'get {item}' (add current weapon to inventory)")

    input("Press Any Key To Continue...")


# Maze Map
Section = {
    # Starting Point-----------------------------------
    "The Glade": {  # 4 Ways
        "North": "The Glade Entrance",
        "East": "Runners' Junction",
        "South": "Twilight Tunnels",
        "West": "Whispering Woods",
    },
    # 2nd Phase of the Maze----------------------------
    "The Glade Entrance": {  # 4 Ways
        "North": "Echoing Corridor",
        "East": "Shadow Labyrinth",
        "South": "The Glade",
        "West": "Grievers' Alley",
        'Weapon': 'Spear'
    },
    "Shadow Labyrinth": {  # 3 Ways
        "North": "Wraith's Walk",
        "East": "Eclipsed Enclave",
        "West": "The Glade Entrance",
        'Weapon': 'Grenades'
    },
    "Runner' Junction": {  # 2 Ways
        "South": "Enigma Passage",
        "West": "The Glade",
        'Weapon': 'Sword'
    },
    "Enigma Passage": {  # 4 Ways
        "North": "Runners' Junction",
        "East": "Serpent's Spiral",
        "South": "Cryptic Crossroads",
        "West": "Twilight Tunnels",
        'Monster': 'Grievers'
    },
    "Twilight Tunnels": {  # 3 Ways
        "North": "The Glade",
        "East": "Enigma Passage",
        "West": "Solitude Path",
        'Weapon': 'Bow'
    },
    "Solitude Path": {  # 3 Ways
        "North": "Whispering Woods",
        "East": "Twilight Tunnels",
        "West": "Forgotten Nexus",
        'Weapon': 'Spear'
    },
    "Whispering Woods": {  # 4 Ways
        "North": "Grivers' Alley",
        "East": "The Glade",
        "South": "Solitude Path",
        "East": "Nebula Nexus",
        'Weapon': 'Grenades'
    },
    "Grivers' Alley": {  # 3 Ways
        "North": "Vortex Vestibule",
        "East": "The Glade Entrance",
        "South": "Whispering Woods",
        'Monster': 'Grievers'
    },
    # 3rd Phase of the Maze-----------------------------
    "Echoing Corridor": {  # 3 Ways
        "North": "SECTION 5",
        "East": "Wraith's Walk",
        "South": "The Glade Entrance",
        'Weapon': 'Bow'
    },
    "Wraith's Walk": {  # 3 Ways
        "East": "Abyssal Arches",
        "South": "Shadow Labyrinth",
        "West": "Echoing Corridor",
        'Monster': 'Grievers'
    },
    "Abyssal Arches": {  # 1 Way
        "West": "Wraith's Walk",
        'Weapon': 'Darts'
    },
    "Eclipsed Enclave": {  # 3 Ways
        "East": "SECTION 3",
        "South": "Veiled Vista",
        "East": "Shawdow Labyrinth",
        'Weapon': 'Spear'
    },
    
    ###
    "Veiled Vista": { # 1 Way 
        "North": "Eclipsed Enclave"
        'Weapon' 'Darts'
    },
    "Serpent's Spiral": {  # 2 Ways
        "South": "Moonlit Maze",
        "East": "Enigma Passage",
        'Weapon': 'Spear'
    },
    "Moonlit Maze": {  # 2 Ways
        "North": "Serpent's Spiral",
        "East": "SECTION 8",
        'Weapon': 'Darts'
    },
    "Cryptic Crossroads": {  # 4 Ways
        "North": "Enigma Passage",
        "South": "SECTION 2",
        'Weapon': 'Darts'
    },
    "Enchanted Corridor": {  # 1 Way
        "West": "Starlit Sentries",
        'Weapon':'Spear'
    },
    "Starlit Sentries": {  # 3 Ways
        "East": "Enchanted Corridor",
        "South": "SECTION 4",
        "West": "Celestial Circuit",
        'Weapon': 'Sword'
    },
    "Celestial Circuit": {  # 2 Ways
        "North": "Forgotten Nexus",
        "East": "Starlit Sentries",
        'Monster': 'Grievers'
    },
    "Forgetten Nexus": {  # 3 Ways
        "East": "Solutide Path",
        "South": "Celestial Circuit",
        "West": "SECTION 6",
        'Weapon': 'Bow'
    },
    "Nebula Nexus": {  # 1 Way
        "East": "Whispering Woods",
        'Monster': 'Grievers'
    },
    "Mazeheart Nexus": {  # 2 Ways
        "North": "Twilight Traverse",
        "West": "SECTION 7",
        'Weapon': 'Sword'
    },
    "Twilight Traverse": {  # 3 Ways
        "North": "SECTION 1",
        "East": "Vortex Vestibule",
        "South": "Mazeheart Nexus",
        'Weapon': 'Darts'
    },
    "Vortex Vestibule": {  # 2 Ways
        "South": "Grievers' Alley",
        "West": "Twilight Traverse",
        'Weapon': 'Sword'
    },
}

# User's Inventory max 10
inventory = []

# Track User's Section Location
current_section = "The Glade"

# User's Last Move
msg = ""

clear()
prompt()

#Game loop # stop==win lose or exit
while True:

    clear()

    print(f"You are in the {current_section}\n Inventory: {inventory}\n{'-'*27}")

    #Display msg
    print(msg)

    #Weapon
    if "Weapon" in Section[current_section].keys():

        current_weapon = Section[current_section]["Weapon"]

        if current_weapon not in inventory:

            if current_weapon[-1] == 's':
                print(f"You see {current_weapon}")
            
            elif current_weapon[0] == 'a'or 'e'or'i'or 'o' or'u':
                print(f"You see an {current_weapon}")
            
            else:
                print(f"You see a {current_weapon}")


    # Monster
        
    # For movement
    player_input = input("Enter your move:\n")

    # Split move into words
    next_move = player_input.split(' ')

    # Action first word
    action = next_move[0].title()

    if len(next_move) > 1:
        weapon = next_move[1].title()
        direction = next_move[1].title()
        
    #Moving
    if action == "Go":
        try:
            current_section = Section[current_section][direction]
            msg = f"You travel {direction}."

        except:
            msg = f"You can't go that way."

    # Picking
    elif action == "Get":
            
        try:    
            if weapon == Section[current_section]["Weapon"]:

                if weapon not in inventory:
                    inventory.append(Section[current_section]["Weapon"])
                    msg = f"You got {weapon}!"

                ###
                else:
                    msg = f"You already have the {weapon}."
                
            else:
                msg = "You meet Monster!"

        except:
            msg = "You meet Monster!"

    #Exit game
    elif action == "Exit":
        break

    else:
        msg = "Invalid command"

            