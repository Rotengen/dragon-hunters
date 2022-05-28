input("                           PRESS ENTER TO BEGIN                            ")
import random
import time
import os
file1 = 'world1'
file2 = 'world2'
file3 = 'world3'
iron_spawn = [14,28,28,22,22]
coal_spawn = [60,48,28,18,14]
dragonite_spawn = [0,2,4,6,6]
magite_spawn = [6,8,10,14,22]
character = 0
ach_list = ["A new day", "The Miner", "Dedicated Miner","A Useful Metal","Serious Miner","The Shinest Jewel","Vast Riches","One Nice Upgrade"]
ach_des = []
ach_des.append("Move around in your new world")
ach_des.append("Mine stone with a pickaxe")
ach_des.append("Mine 200+ stone")
ach_des.append("Obtain Iron")
ach_des.append("Mine over 36 iron")
ach_des.append("Obtain Dragonite")
ach_des.append("Mine 6 Dragonite, then cry in pain")
ach_des.append("Upgrade a Iron Pickaxe to a Steel Pickaxe")
f1 = open('world1','a')
f2 = open('world2','a')
f3 = open('world3','a')
f4 = open('inv1','a')
f5 = open('inv2','a')
f6 = open('inv3','a')
f7 = open('pos1','a')
f8 = open('pos2','a')
f9 = open('pos3','a')
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
worlds = 0
# check if size of file is 0
w1 = True
w2 = True
w3 = True
if os.stat(file1).st_size == 0:
    worlds += 1
    w1 = False
if os.stat(file2).st_size == 0:
    worlds += 1
    w2 = False
if os.stat(file3).st_size == 0:
    worlds += 1
    w3 = False
def save(map):
    save = ""
    for chunk in map:
        for x in chunk:
            for y in x:
                for z in y:
                    save += str(z)
    return save
def loading(string):
    letter = 0
    world = []
    for i in range(1):
        chunk = []
        for i in range(28):
            x = []
            for i in range(28):
                y = []
                for i in range(6):
                    z = int(string[letter])
                    y.append(z)
                    letter += 1
                x.append(y)
            chunk.append(x)
        world.append(chunk)
    return world
load = ""
def saveinv(inv,file):
    for amount in inv:
        file.write(str(amount))
        file.write('\n')
def loadinv(file):
    inv = []
    for line in file:
        inv.append(int(line))
    return inv
def savepos(pos,file):
    for amount in pos:
        file.write(str(amount))
        file.write('\n')
def loadpos(file):
    inv = []
    for line in file:
        inv.append(int(line))
    return inv
def unwrap(string):
    theset = []
    for letter in string:
        theset.append(letter)
    return theset
def rewrap(s):
    string = ''
    for item in s:
        string += item
    return string
while load != "l" or load != "n":
    load = input("L to load or N to start new world")
    load = load.lower()
    print(load)
    if load == "l" or load == "n":
        break
    else:
        print("Please input L or N")
if load == "n" and worlds != 0:
    goals = "00000000"
    stone_mined = 0
    iron_mined = 0
    dragon_mined = 0
    tw = 4 - worlds
    inventory = []
    for i in range(36):
        inventory.append(0)
    player_z = 0
    player_chunk = 0
    player_y = 0
    player_x = 0
# Block Ids: 0 - stone, 1 - wood, 2 - iron, 3 - coal, 4 - dragonite, 5 - magite
    print("World generating...please wait")
    percent = 0
    the_map =[]
    for i in range(1):
        chunk_1 =[]
        for i in range(28):
            blank = []
            for i in range(28):
                blank_2 = []
                for i in range(6):
                    blank_2.append(0)
                blank.append(blank_2)
            bb = []
            for i in range(6):
                bb.append(0)
            blank.append(bb)
            chunk_1.append(blank)
        for i in range(18):
            x_pos = random.randint(1,28)
            y_pos = random.randint(1,28)
            chunk_1[x_pos-1][y_pos-1][0] = 1
        z_pos = 1
        for i in range(5):
            for i in range(iron_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 2
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(coal_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 3
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(dragonite_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 4
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(magite_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 5
            z_pos = z_pos + 1
        big_blank = []
        for i in range(29):
            bb = []
            for i in range(6):
                bb.append(0)
            big_blank.append(bb)    
        chunk_1.append(big_blank)
        the_map.append(chunk_1)
        percent += (100/36)
        #print("Percent done: " ,str(round(percent))," %")
    if tw == 1:
            file1 = open('world1', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world1","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    elif tw == 2:
            file1 = open('world2', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world2","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    elif tw == 3:
            file1 = open('world3', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world3","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    time.sleep(1)
    print("Generation finished.")
elif load == "l" and worlds == 3:
    print("No worlds found.")
    print("Generating a new world instead.")
    stone_mined = 0
    iron_mined = 0
    dragon_mined = 0
# Block Ids: 0 - stone, 1 - wood, 2 - iron, 3 - coal, 4 - dragonite, 5 - magite
    tw = 4 - worlds
    inventory = []
    goals = "00000000"
    for i in range(36):
        inventory.append(0)
    player_z = 0
    player_chunk = 0
    player_y = 0
    player_x = 0
# Block Ids: 0 - stone, 1 - wood, 2 - iron, 3 - coal, 4 - dragonite, 5 - magite
    print("World generating...please wait")
    percent = 0
    the_map =[]
    for i in range(1):
        chunk_1 =[]
        for i in range(28):
            blank = []
            for i in range(28):
                blank_2 = []
                for i in range(6):
                    blank_2.append(0)
                blank.append(blank_2)
            bb = []
            for i in range(6):
                bb.append(0)
            blank.append(bb)
            chunk_1.append(blank)
        for i in range(18):
            x_pos = random.randint(1,28)
            y_pos = random.randint(1,28)
            chunk_1[x_pos-1][y_pos-1][0] = 1
        z_pos = 1
        for i in range(5):
            for i in range(iron_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 2
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(coal_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 3
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(dragonite_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 4
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(magite_spawn[z_pos-1]):
                x_pos = random.randint(1,28)
                y_pos = random.randint(1,28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 5
            z_pos = z_pos + 1
        big_blank = []
        for i in range(29):
            bb = []
            for i in range(6):
                bb.append(0)
            big_blank.append(bb)    
        chunk_1.append(big_blank)
        the_map.append(chunk_1)
        percent += (100/36)
        #print("Percent done: " ,str(round(percent))," %")
    if tw == 1:
            file1 = open('world1', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world1","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    elif tw == 2:
            file1 = open('world2', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world2","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    elif tw == 3:
            file1 = open('world3', 'w')
            file1.write(save(the_map))
            file1.close()
            file = open("world3","r")
            thing = file.read()
            the_map = loading(thing)
            file.close()
    time.sleep(1)
    print("Generation finished.")
elif load == "n" and worlds == 0:
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
        ans = input("Type in the number of the world you want to load.")
        if ans not in valid:
            print("Type a valid number which are",valid)
    if ans == "1":
        file = open("world1","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 1
        file2 = open("inv1","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos1","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
    elif ans == "2":
        file = open("world2","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 2
        file2 = open("inv2","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos2","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
    elif ans == "3":
        file = open("world3","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 3
        file2 = open("inv3","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos3","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
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
        ans = input("Type in the number of the world you want to load.")
        if ans not in valid:
            print("Type a valid number which are",valid)
    if ans == "1":
        file = open("world1","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 1
        file2 = open("inv1","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos1","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
    elif ans == "2":
        file = open("world2","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 2
        file2 = open("inv2","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos2","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
    elif ans == "3":
        file = open("world3","r")
        thing = file.read()
        the_map = loading(thing)
        file.close()
        tw = 3
        file2 = open("inv3","r")
        inventory = loadinv(file2)
        file.close()
        file3 = open("pos3","r")
        lmaonoobimaginenames = loadpos(file3)
        player_x = lmaonoobimaginenames[0]
        player_y = lmaonoobimaginenames[1]
        player_z = lmaonoobimaginenames[2]
        player_chunk = lmaonoobimaginenames[3]
        stone_mined = lmaonoobimaginenames[4]
        iron_mined = lmaonoobimaginenames[5]
        dragon_mined =lmaonoobimaginenames[6]
        goals = str(lmaonoobimaginenames[7])
def identify(block_id):
    block = ""
    if block_id == 0:
        block = "O"
    elif block_id == 1:
        block = "T"
    elif block_id == 2:
        block = "I"
    elif block_id == 3:
        block = "C"
    elif block_id == 4:
        block = "D"
    elif block_id == 5:
        block = "M"
    elif block_id == 6:
        block = " "
    return block
def draw_map(chunk, pl_x,pl_y,pl_z):
    print("x = ",pl_x + chunk * 28,"  y = ",pl_y + chunk * 28,"  z = ",pl_z)
    y = 0
    if pl_z == 0:
        for i in range(28):
            line = ""
            x = 0
            for i in range(28):
                if x == pl_x:
                    if y == pl_y:
                        line = line + "P"
                    else:
                        if the_map[int(chunk)][int(x)][int(y)][0] == 1:
                            line = line + "T"
                        elif the_map[int(chunk)][int(x)][int(y)][0] == 6:
                            line = line + " "
                        else:
                            line = line + "O"
                else:
                    if the_map[int(chunk)][int(x)][int(y)][0] == 1:
                        line = line + "T"
                    elif the_map[int(chunk)][int(x)][int(y)][0] == 6:
                        line = line + " "
                    else:
                        line = line + "O"
                line = line + " "
                x = x + 1
            print(line)
            y = y + 1
    else:
        print("# # # # #")
        row =  ""
        row += "# # "
        row += identify(the_map[int(chunk)][pl_x][pl_y - 1][pl_z-1])
        row += " # #"
        print(row)
        row  = "# "
        try:
            row += identify(the_map[int(chunk)][pl_x - 1][pl_y][pl_z-1])
        except:
            row += "O"
        row += " P "
        try:
            row += identify(the_map[int(chunk)][pl_x + 1][pl_y][pl_z-1])
        except:
            row += "O"
        row += " #"
        print(row)
        row =  ""
        row += "# # "
        try:
            row += identify(the_map[int(chunk)][pl_x][pl_y + 1][pl_z-1])
        except:
            row += "O"
        row += " # #"
        print(row)
        print("# # # # #")
def see_block(block_type):
    if block_type == 0:
        block = "stone"
    elif block_type == 1:
        block = "wood"
    elif block_type == 2:
        block = "iron ore"
    elif block_type == 3:
        block = "coal ore"
    elif block_type == 4:
        block = "dragonite ore"
    elif block_type == 5:
        block = "magite ore"
    elif block_type == 6:
        block = "none"
    return block
pos_save = [player_x,player_y,player_z,player_chunk,stone_mined,iron_mined,dragon_mined,goals]
if tw == 1:
    file2 = open('inv1', 'w')
    saveinv(inventory,file2)
    file2.close()
    file3 = open('pos1', 'w')
    savepos(pos_save,file3)
    file3.close()
elif tw == 2:
    file2 = open('inv2', 'w')
    saveinv(inventory,file2)
    file2.close()
    file3 = open('pos2', 'w')
    savepos(pos_save,file3)
    file3.close()
elif tw == 3:
    file2 = open('inv3', 'w')
    saveinv(inventory,file2)
    file2.close()
    file3 = open('pos3', 'w')
    savepos(pos_save,file3)
    file3.close()
time.sleep(1)
while True:
    pos_save = [player_x,player_y,player_z,player_chunk,stone_mined,iron_mined,dragon_mined,goals]
    achievements = unwrap(goals)
    unlocked = 0
    print("P is the player, O is stone, and T is a tree,")
    print("C is coal, I is iron, D is dragonite, and M is magite")
    print("and # is a dark space that you cannnot see.")
    print("type WASD keys to move, E to dig, and C to craft，U to use an item")
    print("I to open inventory, P to look at achievements, and V to save.")
    draw_map(player_chunk,player_x,player_y,player_z)
    block = ""
    try:
        block_type = the_map[player_chunk][player_x][player_y][player_z]
        block = see_block(block_type)
    except:
        block_type = 7
        block = "bedrock"
    if block != "none":
        print("Below you is",block)
    if block == "none":
        print("There is nothing below you. Type G to go down.")
    block_type_up = the_map[player_chunk][player_x][player_y][player_z - 2]
    block_up = see_block(block_type_up)
    if block_up != "none":
        if player_z > 1 :
            print("Above you is",block_up)
    if block_up == "none" and player_z > 1:
        print("There is nothing above you. Type H to go up.")
    elif player_z == 1:   
        print("Type H to go back up.")
    key = input()
    if key == "G" or key == "g":
        if block == "none":
            player_z += 1
            if achievements[0] == "0":
                unlocked = 1
        else:
            print("You cannot go down here!")
    elif key == "H" or key == "h":
        if block_up == "none" and player_z != 0:
            player_z -= 1
            if achievements[0] == "0":
                unlocked = 1
        elif player_z == 1:
            player_z -= 1
            if achievements[0] == "0":
                unlocked = 1
        else:
            print("You cannot go up here!")
    elif key == "e" or key  == "E":
        if player_z != 0:
            while True:
                direction = input("Where do you want to mine? WASD, H for up and G for down")
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
                    if player_y + y_change > 27 or player_y + y_change < 0 or player_x + x_change > 27 or player_x + x_change < 0:
                        print("You cannot mine blocks outside the border!")
                    else:
                        break
                elif direction == "h":
                    if player_z == 1:
                        print("You cannot mine up")
                    else:
                        break
                else:
                    print("Please input a valid direction")
        else:
            direction = "g"
        pick = 0
        if inventory[10] == 1:
            pick = 1
        if inventory[11] == 1:
            pick = 2
        if inventory[12] == 1:
            pick = 3
        if inventory[13] == 1:
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
            block_mine = the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change]
        except:
            block_mine = 7
        if block_mine == 1:
            print("Mining...")
            time.sleep(4 - pick)
            print("Block broken")
            inventory[0] += 1
            print("Wood obtained!")
            the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
        elif block_mine == 0:
            if pick != 0:
                print("Mining...")
                time.sleep(7 - pick*1.5)
                print("Block broken")
                inventory[1] += 1
                print("Stone obtained!")
                the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
                stone_mined += 1
                if achievements[1] == "0":
                    unlocked = 2
                if achievements[2] == "0" and stone_mined == 216:
                    unlocked = 3
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 3:
            if pick != 0:
                print("Mining...")
                time.sleep(10 - pick*2)
                print("Block broken")
                inventory[3] += 1
                print("Coal obtained!")
                the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 2:
            if pick > 1:
                print("Mining...")
                time.sleep(13 - pick*2.5)
                print("Block broken")
                inventory[2] += 1
                print("Iron obtained!")
                the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
                iron_mined += 1
                if achievements[3] == "0":
                    unlocked = 4
                if achievements[4] == "0" and iron_mined == 36:
                    unlocked = 5
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 4:
            if pick == 4:
                print("Mining...")
                time.sleep(19 - pick*3.5)
                print("Block broken")
                inventory[4] += 1
                print("Dragonite obtained!")
                the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
                dragon_mined += 1
                if achievements[5] == "0":
                    unlocked = 6
                if achievements[6] == "0" and dragon_mined == 6:
                    unlocked = 7
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 5:
            if pick == 3 or pick == 4:
                print("Mining...")
                time.sleep(16 - pick*3)
                print("Block broken")
                inventory[5] += 1
                print("Magite obtained!")
                the_map[player_chunk][player_x + x_change][player_y + y_change][player_z + z_change] = 6
            else:
                print("This cannot be broken currently! Get a better pickaxe")
        elif block_mine == 6:
            print("You cannot break air!")
        elif block_mine == 7:
            print("You cannot break bedrock.")
        

    elif key == "w" or key == "W":
        if player_y != 0:
            if player_z == 0:
                player_y += -1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player_chunk][player_x][player_y - 1][player_z - 1] == 6:
                player_y += -1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "s" or key == "S":
        if player_y != 27:
            if player_z == 0:
                player_y += 1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player_chunk][player_x][player_y + 1][player_z - 1] == 6:
                player_y += 1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "a" or key == "A":
        if player_x != 0:
            if player_z == 0:
                player_x += -1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player_chunk][player_x - 1][player_y][player_z - 1] == 6:
                player_x += -1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")

    elif key == "d" or key == "D":
        if player_x != 27:
            if player_z == 0:
                player_x += 1
                if achievements[0] == "0":
                    unlocked = 1
            elif the_map[player_chunk][player_x + 1][player_y][player_z - 1] == 6:
                player_x += 1
                if achievements[0] == "0":
                    unlocked = 1
            else:
                print("There is a wall in the way. You cannot go in this direction")
        else:
            print("On world border. Cannot travel in this direction")
    elif key == "v" or  key == "V":
        print("Saving...")
        if tw == 1:
            file1 = open('world1', 'w')
            file1.write(save(the_map))
            file1.close()
            file2 = open('inv1', 'w')
            saveinv(inventory,file2)
            file2.close()
            file3 = open('pos1', 'w')
            savepos(pos_save,file3)
            file3.close()
        elif tw == 2:
            file1 = open('world2', 'w')
            file1.write(save(the_map))
            file1.close()
            file2 = open('inv2', 'w')
            saveinv(inventory,file2)
            file2.close()
            file3 = open('pos2', 'w')
            savepos(pos_save,file3)
            file3.close()
        elif tw == 3:
            file1 = open('world3', 'w')
            file1.write(save(the_map))
            file1.close()
            file2 = open('inv3', 'w')
            saveinv(inventory,file2)
            file2.close()
            file3 = open('pos3', 'w')
            savepos(pos_save,file3)
            file3.close()
        time.sleep(1)
        print("Saved.")
    elif key == "c" or  key == "C":
        if inventory[22] == 0:
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
                ID = input("Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        inventory[34] += 4
                        inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        inventory[35] += 2
                        inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if inventory[34] <= 3:
                        print("Not enough materials")
                    else:
                        inventory[22] += 1
                        inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "Q" or ID == "q":
                    break
                else:
                    print("Please type a valid ID")
        elif inventory[24] == 1:
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
            print("--------------------UPGRADES--------------------")
            print("ID 9:Steel pickaxe")
            print("Upgraded from Iron pickaxe")
            print("Upgraded using 5 iron, 5 steel and 2 sticks")
            print("Helps you to mine all ores")
            
            ID = 0
            while True:
                ID = input("Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        inventory[34] += 4
                        inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        inventory[35] += 2
                        inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if inventory[34] < 4:
                        print("Not enough materials")
                    else:
                        inventory[22] += 1
                        inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "4":
                    if inventory[34] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[10] += 1
                        inventory[34] -= 5
                        inventory[35] -= 4
                        print("Obtained Wooden Pickaxe")
                elif ID == "5":
                    if inventory[1] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[11] += 1
                        inventory[1] -= 5
                        inventory[35] -= 4
                        print("Obtained Stone Pickaxe")
                elif ID == "6":
                    if inventory[2] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[12] += 1
                        inventory[2] -= 5
                        inventory[35] -= 4
                        
                        print("Obtained Iron Pickaxe")
                elif ID == "7":
                    if inventory[1] < 16 or inventory[2] < 3 or inventory[3] < 3 or inventory[34] < 6:
                        print("Not enough materials")
                    else:
                        inventory[1] -= 16
                        inventory[2] -= 3
                        inventory[3] -= 3
                        inventory[34] -= 6
                        inventory[23] += 1
                        
                        print("Obtained Blaster. Type U to use.")
                elif ID == "8":
                    if inventory[1] < 16 or inventory[2] < 4 or inventory[7] < 5:
                        print("Not enough materials")
                    else:
                        inventory[1] -= 16
                        inventory[2] -= 4
                        inventory[7] -= 5
                        inventory[24] += 1
                        
                        print("Obtained Upgrader Bench.")
                elif ID == "9":
                    if inventory[2] < 5 or inventory[7] < 5 or inventory[35] < 2 or inventory[12] < 1:
                        print("Not enough materials")
                    else:
                        inventory[7] -= 5
                        inventory[2] -= 5
                        inventory[35] -= 2
                        inventory[12] -= 1
                        inventory[13] += 1
                        print("Obtained Steel pickaxe")
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
            ID = 0
            while True:
                ID = input("Type the ID of the crafting recipe you want to do. Type Q to quit.")
                if ID == "1":
                    if inventory[0] == 0:
                        print("Not enough materials")
                    else:
                        inventory[34] += 4
                        inventory[0] -= 1
                        print("Obtained Wooden planks X4")
                elif ID == "2":
                    if inventory[34] == 0:
                        print("Not enough materials")
                    else:
                        inventory[35] += 2
                        inventory[34] -= 1
                        print("Obtained Sticks X2")
                elif ID == "3":
                    if inventory[34] < 4:
                        print("Not enough materials")
                    else:
                        inventory[22] += 1
                        inventory[34] -= 4
                        print("Obtained Workbench")
                elif ID == "4":
                    if inventory[34] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[10] += 1
                        inventory[34] -= 5
                        inventory[35] -= 4
                        print("Obtained Wooden Pickaxe")
                elif ID == "5":
                    if inventory[1] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[11] += 1
                        inventory[1] -= 5
                        inventory[35] -= 4
                        print("Obtained Stone Pickaxe")
                elif ID == "6":
                    if inventory[2] < 5 or inventory[35] < 4:
                        print("Not enough materials")
                    else:
                        inventory[12] += 1
                        inventory[2] -= 5
                        inventory[35] -= 4
                        print("Obtained Iron Pickaxe")
                elif ID == "7":
                    if inventory[1] < 16 or inventory[2] < 3 or inventory[3] < 3 or inventory[34] < 6:
                        print("Not enough materials")
                    else:
                        inventory[1] -= 16
                        inventory[2] -= 3
                        inventory[3] -= 3
                        inventory[34] -= 6
                        inventory[23] += 1
                        print("Obtained Blaster. Type U to use.")
                elif ID == "8":
                    if inventory[1] < 16 or inventory[2] < 4 or inventory[7] < 5:
                        print("Not enough materials")
                    else:
                        inventory[1] -= 16
                        inventory[2] -= 4
                        inventory[7] -= 5
                        inventory[24] += 1
                        print("Obtained Upgrader Bench.")
                elif ID == "Q" or ID == "q":
                    break
                else:
                    print("Please type a valid ID")
    elif key == "u" or  key == "U":
        if inventory[23] != 0:
            print("Use 1 coal and 3 iron to make 2 steel.")
            e = input("Type Y to do this")
            if e.lower() == "y":
                if inventory[3] < 1 or inventory[2] < 3:
                    print("Not enough materials")
                else:
                    print("Smelting...")
                    time.sleep(12)
                    print("Obtained 2 steel")
                    inventory[7] += 2
                    inventory[2] -= 3
                    inventory[3] -= 1
        else:
            print("You need a blaster for this.")
    elif key == "i" or  key == "I":
        print("Inventory:")
        ready = [0,1,2,3,4,5,7,10,11,12,13,22,23,24,34,35]
        names = ["Wood","Stone","Iron","Coal","Dragonite","Magite","Steel","Wood Pickaxe","Stone Pickaxe","Iron Pickaxe","Steel Pickaxe","Workbench","Blaster","Upgrader Bench","Wooden Plank","Sticks"]
        for i in range(16):
            t = inventory[ready[i]]
            if t != 0:
                print(t,names[i])
        input("Press enter to continue.")
    elif key == "P" or key == "p":
        print("Achievements:")
        print("Unlocked:")
        for i in range(8):
            if achievements[i] == "1":
                print(ach_list[i])
                print(ach_des[i])
        print("Locked:")
        for i in range(8):
            if achievements[i] == "0":
                print(ach_list[i])
                print(ach_des[i])
        input("Press Enter to continue.")
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
    goals = rewrap(achievements)


    
        
    


          

    

    
        
