import os
import time
import random
from functions import *
from classes import Player, Dragon

player = Player()  # initialize player
clear() # Clear the screen
input("                           PRESS ENTER TO BEGIN                            ")

# 🖤 🖤 🖤 🖤 🖤 🖤 🖤 🖤     💛  🥖 🥖 🥖 🥖 🥖 🥖 🥖 🥖 🥖 🥖4 5 7 9 10
ach_list = ["A new day", "The Miner", "Dedicated Miner", "A Useful Metal", "Serious Miner", "The Shinest Jewel", "Vast Riches", "One Nice Upgrade", "Power in My hands", "Dragon Hunters"]
ach_des = ["Move around in your new world", "Mine stone with a pickaxe", "Mine 200+ stone", "Obtain Iron", "Mine over 36 iron", "Obtain Dragonite", "Mine 6 Dragonite, then cry in pain", "Upgrade a Iron tool to a Steel tool", "Craft a sword", "Kill a mingel"]

# initialize all data files if they don't already exist
initialize_files()

# check if size of initialized world file is 0
w1 = True
w2 = True
w3 = True
if os.stat('world1').st_size == 0:
    player.world += 1
    w1 = False
if os.stat('world2').st_size == 0:
    player.world += 1
    w2 = False
if os.stat('world3').st_size == 0:
    player.world += 1
    w3 = False

interface = 0
while interface != "1" or interface != "2":
    print("Note that this game uses Unicode characters.")
    print("IDLE supports Unicode, but the regular Python runner cannot.")
    print("If this symbol \"🖤\" is not a heart, your softwdare does not support Unicode.")
    interface = input(
        "Type 1 if your system can support Unicode, or 2 if your system can't: ")
    if interface == "1" or interface == "2":
        break

load = ""
while load != "l" or load != "n":
    load = input("L to load or N to start new world, and C to see changelog: ")
    load = load.lower()
    print(load)
    if load == "l" or load == "n":
        break
    elif load == "c":
        print("This feature is postponed til the next snapshot.")
        # 1
        # Save
        # ore dist.
        # advancements
        # 2
        # swords/
        # change of pick/
        # meat/
        # dragon/
        # autosave/
        # player.health/
        #adv. change
        #adv. add
    else:
        print("Please input L or N: ")
if load == "n" and player.world != 0:
    player.world = 4 - player.world
    the_map = generate_map()
    savemap(the_map, player.world)
    the_map = loadmap(player.world)
    time.sleep(1)
    print("Generation finished.")
elif load == "l" and player.world == 3:
    print("No worlds found.")
    print("Generating a new world instead.")
    player.world = 4 - player.world
    # Generating and saving new map and player
    the_map = generate_map()
    savemap(the_map, player.world)
    the_map = loadmap(player.world)
    time.sleep(1)
    print("Generation finished.")
elif load == "n" and player.world == 0:
    print("There is no more memory for worlds!")
    print("Load a world instead.")
    print("Worlds avaliable:")
    valid = []
    if w1 == True:
        print("World 1")
        valid.append("1")
    if w2 == True:
        print("World 2")
        valid.append("2")
    if w3 == True:
        print("World 3")
        valid.append("3")

    ans = " "
    while ans not in valid:
        ans = input("Type in the number of the world you want to load: ")
        if ans not in valid:
            print("Type a valid number which are", valid)
    player.world = ans
    # load existing map and player
    the_map = loadmap(player.world)
    player.load(player.world)
else:
    print("Worlds avaliable:")
    valid = []
    if w1 == True:
        print("World 1")
        valid.append("1")
    if w2 == True:
        print("World 2")
        valid.append("2")
    if w3 == True:
        print("World 3")
        valid.append("3")

    ans = " "
    while ans not in valid:
        ans = input("Type in the number of the world you want to load: ")
        if ans not in valid:
            print("Type a valid number which are", valid)

        # Load Existing Map and Player
        player.world = ans
        the_map = loadmap(player.world)
        player.load(player.world)
        time.sleep(1)

autosave = 0

while True:
    autosave += 1
    if autosave == 10:
        autosave = 0
        player.save()
        savemap(the_map, player.world)

    achievements = unwrap(player.goals)
    unlocked = 0
    fight = False
    # Load a dragon object
    dragon = Dragon()
    print("Dragon radar detecting...")
    print(dragon.alive)
    print("Each dragon on the radar is shown by (x position, y position, player.health left)")
    print("P is the player, O is stone, and T is a tree,")
    print("C is coal, I is iron, D is dragonite, and M is magite")
    print("and # is a dark space that you cannnot see.")
    print("type WASD keys to move, E to dig, and C to craft，U to use an item,")
    print("F to eat food, and Q to quit.")
    print("I to open player.inventory, P to look at achievements, and V to save.")
    if interface == 1:
        print("For the bottom of the map, is the player.health andplayer.hunger GUIs where")
        print("🖤 represents 1 health, 💛 represents a lack of health,")
        print("and 🥖 represents hunger.")
    else:
        print("For the bottom of the map, is the player.health andplayer.hunger GUIs where")
        print("H represents 1 health,")
        print("and F represents hunger.")
    # draw the map    
    draw_map(the_map, player, interface)
    # check player status
    player.health, player.hunger = system_check(player.health, player.hunger)
    block = ""
    try:
        block_type = the_map[player.chunk][player.x][player.y][player.z]
        block = see_block(block_type)
    except:
        block_type = 7
        block = "bedrock"
    if block != "none":
        print("Below you is", block)
    if block == "none":
        print("There is nothing below you. Type G to go down.")
    block_type_up = the_map[player.chunk][player.x][player.y][player.z - 2]
    block_up = see_block(block_type_up)
    if block_up != "none":
        if player.z > 1:
            print("Above you is", block_up)
    if block_up == "none" and player.z > 1:
        print("There is nothing above you. Type H to go up.")
    elif player.z == 1:
        print("Type H to go back up.")
    r1, r2 = coord_check(player, dragon)
    if r1 == True and player.z == 0:
        print("There is a mingel near you!")
        print("Type B to fight.")
        fight = True
    key = getChar()
    if player.health == 0:
        print("You have died!")
        input("Press Enter to respawn.")
        print("Respawning...")
        time.sleep(1)
        player.respawn()
        player.world = 4 - player.world

    elif key == "B" or key == "b":
        if fight == True:
            if player.inventory[14] == 1:
                damage = 4
            if player.inventory[15] == 1:
                damage = 5
            if player.inventory[16] == 1:
                damage = 7
            if player.inventory[17] == 1:
                damage = 9
            if player.inventory[18] == 1:
                damage = 10
            dragon.health -= damage
            if dragon.health < 0:
                print("You killed a mingel!")
                food_drops = random.randint(1, 3)
                print("You got", food_drops, "dragon meat from the mingel")
                player.inventory[36] += food_drops
                if achievements[9] == "0":
                    unlocked = 10
                dragon = Dragon()
            else:
                print("You dealt", damage, "damage.")
                print("The mingel has ", dragon.health, " health left.")
        else:
            print("Please type a valid command")
    elif key == "G" or key == "g":
        if block == "none":
            player.z += 1
            if achievements[0] == "0":
                unlocked = 1
        else:
            print("You cannot go down here!")
    elif key == "H" or key == "h":
        if block_up == "none" and player.z != 0:
            player.z -= 1
            if achievements[0] == "0":
                unlocked = 1
        elif player.z == 1:
            player.z -= 1
            if achievements[0] == "0":
                unlocked = 1
        else:
            print("You cannot go up here!")
    elif key == "e" or key == "E":
        if player.z != 0:
            while True:
                direction = input(
                    "Where do you want to mine? WASD, H for up and G for down")
                direction = direction.lower()
                if direction == "w" or direction == "a" or direction == "s" or direction == "h" or direction == "g" or direction == "d":
                    if direction == "w":
                        x_change = 0
                        y_change = -1
                        z_change = -1
                    elif direction == "s":
                        x_change = 0
                        y_change = 1
                        z_change = -1
                    elif direction == "a":
                        x_change = -1
                        y_change = 0
                        z_change = -1
                    elif direction == "d":
                        x_change = 1
                        y_change = 0
                        z_change = -1
                    else:
                        x_change = 0
                        y_change = 0
                    if player.y + y_change > 27 or player.y + y_change < 0 or player.x + x_change > 27 or player.x + x_change < 0:
                        print("You cannot mine blocks outside the border!")
                    else:
                        break
                elif direction == "h":
                    if player.z == 1:
                        print("You cannot mine up")
                    else:
                        break
                else:
                    print("Please input a valid direction")
        else:
            direction = "g"
        pick = 0
        if player.inventory[10] == 1:
            pick = 1
        if player.inventory[11] == 1:
            pick = 2
        if player.inventory[12] == 1:
            pick = 3
        if player.inventory[13] == 1:
            pick = 4
        if direction == "w":
            x_change = 0
            y_change = -1
            z_change = -1
        elif direction == "s":
            x_change = 0
            y_change = 1
            z_change = -1
        elif direction == "a":
            x_change = -1
            y_change = 0
            z_change = -1
        elif direction == "d":
            x_change = 1
            y_change = 0
            z_change = -1
        elif direction == "g":
            x_change = 0
            y_change = 0
            z_change = 0
        elif direction == "h":
            x_change = 0
            y_change = 0
            z_change = -2
        try:
            block_mine = the_map[player.chunk][player.x +
                                               x_change][player.y + y_change][player.z + z_change]
        except:
            block_mine = 7
        if block_mine == 1:
            print("Mining...")
            time.sleep(4 - pick)
            print("Block broken")
            player.inventory[0] += 1
            print("Wood obtained!")
            the_map[player.chunk][player.x + x_change][player.y +
                                                       y_change][player.z + z_change] = 6
        elif block_mine == 0:
            if pick != 0:
                print("Mining...")
                time.sleep(7 - pick*1.5)
                print("Block broken")
                player.inventory[1] += 1
                print("Stone obtained!")
                the_map[player.chunk][player.x + x_change][player.y +
                                                           y_change][player.z + z_change] = 6
                player.stone_mined += 1
                if achievements[1] == "0":
                    unlocked = 2
                if achievements[2] == "0" and player.stone_mined == 216:
                    unlocked = 3
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 3:
            if pick != 0:
                print("Mining...")
                time.sleep(10 - pick*2)
                print("Block broken")
                player.inventory[3] += 1
                print("Coal obtained!")
                the_map[player.chunk][player.x + x_change][player.y + y_change][player.z + z_change] = 6
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 2:
            if pick > 1:
                print("Mining...")
                time.sleep(13 - pick*2.5)
                print("Block broken")
                player.inventory[2] += 1
                print("Iron obtained!")
                the_map[player.chunk][player.x + x_change][player.y +
                                                           y_change][player.z + z_change] = 6
                player.iron_mined += 1
                if achievements[3] == "0":
                    unlocked = 4
                if achievements[4] == "0" and player.iron_mined == 36:
                    unlocked = 5
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 4:
            if pick == 4:
                print("Mining...")
                time.sleep(19 - pick*3.5)
                print("Block broken")
                player.inventory[4] += 1
                print("Dragonite obtained!")
                the_map[player.chunk][player.x + x_change][player.y + y_change][player.z + z_change] = 6
                player.dragon_mined += 1
                if achievements[5] == "0":
                    unlocked = 6
                if achievements[6] == "0" and player.dragon_mined == 6:
                    unlocked = 7
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 5:
            if pick == 3 or pick == 4:
                print("Mining...")
                time.sleep(16 - pick*3)
                print("Block broken")
                player.inventory[5] += 1
                print("Magite obtained!")
                the_map[player.chunk][player.x + x_change][player.y + y_change][player.z + z_change] = 6
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 6:
            print("You cannot break air!")
        elif block_mine == 7:
            print("You cannot break bedrock.")

    elif key == "w" or key == "W":
        if player.y != 0:
            if player.z == 0:
                player.y += -1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player.chunk][player.x][player.y - 1][player.z - 1] == 6:
                player.y += -1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "s" or key == "S":
        if player.y != 27:
            if player.z == 0:
                player.y += 1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player.chunk][player.x][player.y + 1][player.z - 1] == 6:
                player.y += 1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "a" or key == "A":
        if player.x != 0:
            if player.z == 0:
                player.x += -1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player.chunk][player.x - 1][player.y][player.z - 1] == 6:
                player.x += -1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "d" or key == "D":
        if player.x != 27:
            if player.z == 0:
                player.x += 1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player.chunk][player.x + 1][player.y][player.z - 1] == 6:
                player.x += 1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")
    elif key == "v" or key == "V":
        player.save()
    elif key == "c" or key == "C":
        if player.inventory[22] == 0:
            print("These are what you can craft.")
            print("ID 1:Wooden planks X4")
            print("-crafted from one wood")
            print("ID 2:Sticks X2")
            print("Crafted from one wooden plank")
            print("ID 3:Workbench")
            print("crafted from 4 wooden planks")
            print("helps you to craft more items")
            ID = 0
            while True:
                ID = input(
                    "Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if player.inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[34] += 4
                        player.inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if player.inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[35] += 2
                        player.inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if player.inventory[34] <= 3:
                        print("Not enough materials")
                    else:
                        player.inventory[22] += 1
                        player.inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "Q" or ID == "q":
                    break
                else:
                    print("Please type a valid ID")
        elif player.inventory[24] == 1:
            print("These are what you can craft.")
            print("ID 1:Wooden planks X4")
            print("Crafted from one wood")
            print("ID 2:Sticks X2")
            print("Crafted from one wooden plank")
            print("ID 3:Workbench")
            print("Crafted from 4 wooden planks")
            print("helps you to craft more items")
            print("ID 4:Wooden pickaxe")
            print("Crafted from 5 wooden planks and 4 sticks")
            print("Helps you to mine stone and coal")
            print("ID 5:Stone pickaxe")
            print("Crafted from 5 stone and 4 sticks")
            print("Helps you to mine stone, coal and iron")
            print("ID 6:Iron pickaxe")
            print("Crafted from 5 iron and 4 sticks")
            print("Helps you to mine stone, coal, iron and magite")
            print("ID 7:Blaster")
            print("Crafted from 3 iron, 16 stone, 3 coal, and 6 wooden planks.")
            print("Helps you to make coal and iron to steel")
            print("ID 8:Upgrading table")
            print("Crafted from 4 iron, 16 stone and 5 steel")
            print("Helps you to upgrade iron to steel tools")
            print("ID 9:Wooden sword")
            print("Crafted from 4 wooden planks and 3 sticks")
            print("Deals 4 damage to dragons")
            print("ID 10:Stone sword")
            print("Crafted from 4 stone and 3 sticks")
            print("Deals 5 damage to dragons")
            print("ID 11:Iron sword")
            print("Crafted from 4 iron and 3 sticks")
            print("Deals 7 damage to dragons")
            print("ID 12:Dragonite sword")
            print("Crafted from 4 dragonite and 3 sticks")
            print("Deals 10 damage to dragons")
            print("--------------------UPGRADES--------------------")
            print("ID 13:Steel pickaxe")
            print("Upgraded from Iron pickaxe")
            print("Upgraded using 1 iron, 5 steel and 2 sticks")
            print("Helps you to mine all ores")
            print("ID 14:Steel Sword")
            print("Upgraded from Iron Sword")
            print("Upgraded using 2 iron, 3 steel and 3 sticks")
            print("Helps you to mine all ores")

            ID = 0
            while True:
                ID = input(
                    "Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if player.inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[34] += 4
                        player.inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if player.inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[35] += 2
                        player.inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if player.inventory[34] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[22] += 1
                        player.inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "4":
                    if player.inventory[34] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[10] += 1
                        player.inventory[34] -= 5
                        player.inventory[35] -= 4
                        print("Obtained Wooden Pickaxe")
                elif ID == "5":
                    if player.inventory[1] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[11] += 1
                        player.inventory[1] -= 5
                        player.inventory[35] -= 4
                        print("Obtained Stone Pickaxe")
                elif ID == "6":
                    if player.inventory[2] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[12] += 1
                        player.inventory[2] -= 5
                        player.inventory[35] -= 4

                        print("Obtained Iron Pickaxe")
                elif ID == "7":
                    if player.inventory[1] < 16 or player.inventory[2] < 3 or player.inventory[3] < 3 or player.inventory[34] < 6:
                        print("Not enough materials")
                    else:
                        player.inventory[1] -= 16
                        player.inventory[2] -= 3
                        player.inventory[3] -= 3
                        player.inventory[34] -= 6
                        player.inventory[23] += 1

                        print("Obtained Blaster. Type U to use.")
                elif ID == "8":
                    if player.inventory[1] < 16 or player.inventory[2] < 4 or player.inventory[7] < 5:
                        print("Not enough materials")
                    else:
                        player.inventory[1] -= 16
                        player.inventory[2] -= 4
                        player.inventory[7] -= 5
                        player.inventory[24] += 1

                        print("Obtained Upgrader Bench.")
                elif ID == "9":
                    if player.inventory[34] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[14] += 1
                        player.inventory[34] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Wooden Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "10":
                    if player.inventory[1] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                        if achievements[8] == "0":
                            unlocked = 9
                    else:
                        player.inventory[15] += 1
                        player.inventory[1] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Stone Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "11":
                    if player.inventory[2] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[16] += 1
                        player.inventory[2] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Iron Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "12":
                    if player.inventory[4] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[18] += 1
                        player.inventory[4] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Dragonite Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "13":
                    if player.inventory[2] < 1 or player.inventory[7] < 5 or player.inventory[35] < 2 or player.inventory[12] < 1:
                        print("Not enough materials")
                    else:
                        player.inventory[7] -= 5
                        player.inventory[2] -= 1
                        player.inventory[35] -= 2
                        player.inventory[12] -= 1
                        player.inventory[13] += 1
                        print("Obtained Steel pickaxe")
                        if achievements[7] == "0":
                            unlocked = 8
                elif ID == "14":
                    if player.inventory[2] < 1 or player.inventory[7] < 5 or player.inventory[35] < 2 or player.inventory[12] < 1:
                        print("Not enough materials")
                    else:
                        player.inventory[7] -= 3
                        player.inventory[2] -= 2
                        player.inventory[35] -= 3
                        player.inventory[16] -= 1
                        player.inventory[17] += 1
                        print("Obtained Steel Sword")
                        if achievements[7] == "0":
                            unlocked = 8
                elif ID == "Q" or ID == "q":
                    break
                else:
                    print("Please type a valid ID")
        else:
            print("These are what you can craft.")
            print("ID 1:Wooden planks X4")
            print("Crafted from one wood")
            print("ID 2:Sticks X2")
            print("Crafted from one wooden plank")
            print("ID 3:Workbench")
            print("Crafted from 4 wooden planks")
            print("helps you to craft more items")
            print("ID 4:Wooden pickaxe")
            print("Crafted from 5 wooden planks and 4 sticks")
            print("Helps you to mine stone and coal")
            print("ID 5:Stone pickaxe")
            print("Crafted from 5 stone and 4 sticks")
            print("Helps you to mine stone, coal and iron")
            print("ID 6:Iron pickaxe")
            print("Crafted from 5 iron and 4 sticks")
            print("Helps you to mine stone, coal, iron and magite")
            print("ID 7:Blaster")
            print("Crafted from 3 iron, 16 stone, 3 coal, and 6 wooden planks.")
            print("Helps you to make coal and iron to steel")
            print("ID 8:Upgrading table")
            print("Crafted from 4 iron, 16 stone and 5 steel")
            print("Helps you to upgrade iron to steel tools")
            print("ID 9:Wooden sword")
            print("Crafted from 4 wooden planks and 3 sticks")
            print("Deals 4 damage to dragons")
            print("ID 10:Stone sword")
            print("Crafted from 4 stone and 3 sticks")
            print("Deals 5 damage to dragons")
            print("ID 11:Iron sword")
            print("Crafted from 4 iron and 3 sticks")
            print("Deals 7 damage to dragons")
            print("ID 12:Dragonite sword")
            print("Crafted from 4 dragonite and 3 sticks")
            print("Deals 10 damage to dragons")
            ID = 0
            while True:
                ID = input(
                    "Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if player.inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[34] += 4
                        player.inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if player.inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        player.inventory[35] += 2
                        player.inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if player.inventory[34] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[22] += 1
                        player.inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "4":
                    if player.inventory[34] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[10] += 1
                        player.inventory[34] -= 5
                        player.inventory[35] -= 4
                        print("Obtained Wooden Pickaxe")
                elif ID == "5":
                    if player.inventory[1] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[11] += 1
                        player.inventory[1] -= 5
                        player.inventory[35] -= 4
                        print("Obtained Stone Pickaxe")
                elif ID == "6":
                    if player.inventory[2] < 5 or player.inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        player.inventory[12] += 1
                        player.inventory[2] -= 5
                        player.inventory[35] -= 4
                        print("Obtained Iron Pickaxe")
                elif ID == "7":
                    if player.inventory[1] < 16 or player.inventory[2] < 3 or player.inventory[3] < 3 or player.inventory[34] < 6:
                        print("Not enough materials")
                    else:
                        player.inventory[1] -= 16
                        player.inventory[2] -= 3
                        player.inventory[3] -= 3
                        player.inventory[34] -= 6
                        player.inventory[23] += 1
                        print("Obtained Blaster. Type U to use.")
                elif ID == "8":
                    if player.inventory[1] < 16 or player.inventory[2] < 4 or player.inventory[7] < 5:
                        print("Not enough materials")
                    else:
                        player.inventory[1] -= 16
                        player.inventory[2] -= 4
                        player.inventory[7] -= 5
                        player.inventory[24] += 1
                        print("Obtained Upgrader Bench.")
                elif ID == "9":
                    if player.inventory[34] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[14] += 1
                        player.inventory[34] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Wooden Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "10":
                    if player.inventory[1] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[15] += 1
                        player.inventory[1] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Stone Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "11":
                    if player.inventory[2] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[16] += 1
                        player.inventory[2] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Iron Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "12":
                    if player.inventory[4] < 4 or player.inventory[35] < 3:
                        print("Not enough materials")
                    else:
                        player.inventory[18] += 1
                        player.inventory[4] -= 4
                        player.inventory[35] -= 3
                        print("Obtained Dragonite Sword")
                        if achievements[8] == "0":
                            unlocked = 9
                elif ID == "Q" or ID == "q":
                    break
                else:
                    print("Please type a valid ID")
    elif key == "u" or key == "U":
        if player.inventory[23] != 0:
            print("Use 1 coal and 3 iron to make 2 steel.")
            e = input("Type Y to do this")
            if e.lower() == "y":
                if player.inventory[3] < 1 or player.inventory[2] < 3:
                    print("Not enough materials")
                else:
                    print("Smelting...")
                    time.sleep(12)
                    print("Obtained 2 steel")
                    player.inventory[7] += 2
                    player.inventory[2] -= 3
                    player.inventory[3] -= 1
        else:
            print("You need a blaster for this.")
    elif key == "i" or key == "I":
        print("player.inventory:")
        ready = [0, 1, 2, 3, 4, 5, 7, 10, 11, 12, 13,
                 14, 15, 16, 17, 18, 22, 23, 24, 34, 35, 36]
        names = ["Wood", "Stone", "Iron", "Coal", "Dragonite", "Magite", "Steel", "Wood Pickaxe", "Stone Pickaxe", "Iron Pickaxe", "Steel Pickaxe", "Wood Sword",
                 "Stone Sword", "Iron Sword", "Steel Sword", "Dragonite Sword", "Workbench", "Blaster", "Upgrader Bench", "Wooden Plank", "Sticks", "Dragon Meat"]
        for i in range(len(ready)):
            t = player.inventory[ready[i]]
            if t != 0:
                print(t, names[i])
        input("Press enter to continue.")
    elif key == "P" or key == "p":
        print("Achievements:")
        print("Unlocked:")
        for i in range(10):
            if achievements[i] == "1":
                print(ach_list[i])
                print(ach_des[i])
        print("Locked:")
        for i in range(10):
            if achievements[i] == "0":
                print(ach_list[i])
                print(ach_des[i])
        input("Press Enter to continue.")
    elif key == "F" or key == "f":
        print("You have, ", player.inventory[36], " Dragon Meat.")
        key = input("Eat Dragon Meat? Y to eat")
        if key == "y" or key == "Y":
            if player.hunger > 8:
                print("You are not hungry enough!")
            else:
                if player.inventory[36] == 0:
                    print("You don't have any dragon meat!")
                else:
                    player.hunger += random.randint(1, 2)
                    player.inventory[36] -= 1
    elif key == "Q" or key == "q":
        savemap(the_map, player.world)
        player.save()
        quit()
    else:
        print("Please type a valid command")
    if unlocked == 1:
        print("A new day")
        print("Achievement Unlocked!")
        achievements[0] = "1"
    elif unlocked == 2:
        print("The Miner")
        print("Achievement Unlocked!")
        achievements[1] = "1"
    elif unlocked == 3:
        print("Dedicated Miner")
        print("Achievement Unlocked!")
        achievements[2] = "1"
    elif unlocked == 4:
        print("A Useful Metal")
        print("Achievement Unlocked!")
        achievements[3] = "1"
    elif unlocked == 5:
        print("Serious Miner")
        print("Achievement Unlocked!")
        achievements[4] = "1"
    elif unlocked == 6:
        print("The Shinest Jewel")
        print("Achievement Unlocked!")
        achievements[5] = "1"
    elif unlocked == 7:
        print("Vast riches")
        print("Achievement Unlocked!")
        achievements[6] = "1"
    elif unlocked == 8:
        print("One nice upgrade")
        print("Achievement Unlocked!")
        achievements[7] = "1"
    elif unlocked == 9:
        print("Power in My hands")
        print("Achievement Unlocked!")
        achievements[8] = "1"
    elif unlocked == 10:
        print("Dragon Hunters")
        print("Achievement Unlocked!")
        achievements[9] = "1"
    player.goals = rewrap(achievements)
