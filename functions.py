import random
import pickle


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

def getChar():
    # figure out which function to use once, and store it in _func
    if "_func" not in getChar.__dict__:
        try:
            # for Windows-based systems
            import msvcrt  # If successful, we are on Windows
            getChar._func = msvcrt.getch

        except ImportError:
            # for POSIX-based systems (with termios & tty support)
            import tty
            import sys
            import termios  # raises ImportError if unsupported

            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)

                try:
                    tty.setcbreak(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

                return answer

            getChar._func = _ttyRead

    return getChar._func()

def save(map):
    save = ""
    for chunk in map:
        for x in chunk:
            for y in x:
                for z in y:
                    save += str(z)
    return save

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def savemap(map, world):
    pickle.dump(map, open('world' + str(world), 'wb'))

def loadmap(world):
    map = pickle.load(open('world' + str(world), 'rb'))
    return map


def draw_map(the_map, player, interface):
    print("x = ", player.x + player.chunk * 28, "  y = ",
          player.y + player.chunk * 28, "  z = ", player.z)
    y = 0
    if player.z == 0:
        for i in range(28):
            line = ""
            x = 0
            for i in range(28):
                if x == player.x:
                    if y == player.y:
                        line = line + "█"
                    else:
                        if the_map[int(player.chunk)][int(x)][int(y)][0] == 1:
                            line = line + "T"
                        elif the_map[int(player.chunk)][int(x)][int(y)][0] == 6:
                            line = line + " "
                        else:
                            line = line + "O"
                else:
                    if the_map[int(player.chunk)][int(x)][int(y)][0] == 1:
                        line = line + "T"
                    elif the_map[int(player.chunk)][int(x)][int(y)][0] == 6:
                        line = line + " "
                    else:
                        line = line + "O"
                line = line + " "
                x = x + 1
            print(line)
            y = y + 1
    else:
        print("# # # # #")
        row = ""
        row += "# # "
        row += identify(the_map[int(player.chunk)][player.x][player.y - 1][player.z-1])
        row += " # #"
        print(row)
        row = "# "
        try:
            row += identify(the_map[int(player.chunk)][player.x - 1][player.y][player.z-1])
        except:
            row += "O"
        row += " P "
        try:
            row += identify(the_map[int(player.chunk)][player.x + 1][player.y][player.z-1])
        except:
            row += "O"
        row += " #"
        print(row)
        row = ""
        row += "# # "
        try:
            row += identify(the_map[int(player.chunk)][player.x][player.y + 1][player.z-1])
        except:
            row += "O"
        row += " # #"
        print(row)
        print("# # # # #")
    if interface == 1:
        gui = ""
        for i in range(player.health):
            gui += "🖤 "
        for i in range(10-player.health):
            gui += "💛 "
        for i in range(2):
            gui += " "
        for i in range(player.hunger):
            gui += "🥖 "
    else:
        gui = ""
        for i in range(player.health):
            gui += "H "
        for i in range(10-player.health):
            gui += "  "
        for i in range(2):
            gui += " "
        for i in range(player.hunger):
            gui += "F "
    print(gui)

def initialize_files():
    for i in range(1, 4):
        f = open('world' + str(i), 'ab')
        f.close()
        f = open('player' + str(i), 'ab')
        f.close()

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

def coord_check(player, dragon):
    ret = False
    ind = None
    i = 0
    if dragon.x == player.x and dragon.y == player.y:
      ret = True
      ind = i
      i += 1
    return ret, ind

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

def system_check(health, hunger):
    hungers = [0, 6, 8, 9, 10, 11, 11, 12, 13, 14, 14]
    if random.randint(1, hungers[hunger]) == 1 and hunger != 0:
        hu = hunger - 1
    else:
        hu = hunger
    if hunger > 5:
        he = health
    elif hunger > 3:
        if random.randint(1, 3) == 1:
            he = health - 1
        else:
            he = health
    elif hunger > 1:
        if random.randint(1, 2) == 1:
            he = health - 1
        else:
            he = health
    else:
        he = health - 1
    return he, hu

def clear():
    from os import system, name
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def generate_map():
    iron_spawn = [14, 28, 28, 22, 22]
    coal_spawn = [60, 48, 28, 18, 14]
    dragonite_spawn = [0, 2, 4, 6, 6]
    magite_spawn = [6, 8, 10, 14, 22]
    # Block Ids: 0 - stone, 1 - wood, 2 - iron, 3 - coal, 4 - dragonite, 5 - magite
    print("World generating...please wait")
    percent = 0
    the_map = []
    for i in range(1):
        chunk_1 = []
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
            x_pos = random.randint(1, 28)
            y_pos = random.randint(1, 28)
            chunk_1[x_pos-1][y_pos-1][0] = 1
        z_pos = 1
        for i in range(5):
            for i in range(iron_spawn[z_pos-1]):
                x_pos = random.randint(1, 28)
                y_pos = random.randint(1, 28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 2
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(coal_spawn[z_pos-1]):
                x_pos = random.randint(1, 28)
                y_pos = random.randint(1, 28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 3
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(dragonite_spawn[z_pos-1]):
                x_pos = random.randint(1, 28)
                y_pos = random.randint(1, 28)
                chunk_1[x_pos-1][y_pos-1][z_pos] = 4
            z_pos = z_pos + 1
        z_pos = 1
        for i in range(5):
            for i in range(magite_spawn[z_pos-1]):
                x_pos = random.randint(1, 28)
                y_pos = random.randint(1, 28)
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
    return the_map
