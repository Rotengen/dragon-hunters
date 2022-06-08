import pickle
import random
# player class
class Player:
    def __init__(self):
        self.name = ""
        self.world = 0
        self.goals = "0000000000"
        self.stone_mined = 0
        self.iron_mined = 0
        self.dragon_mined = 0
        self.hunger = 10
        self.health = 10
        self.chunk = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.unlocked = 0
        self.achievements = []
        self.inventory = []
        for i in range(48):
            self.inventory.append(0)

    def move(self, x,y,z):
        # need to implement achievements in the use class
        if self.achievements[0] == "0":
            self.unlocked = 1
        if self.x != 27:
            if self.z == 0:
                self.x += x
            
        if self.y != 27:
            if self.z == 0:
                self.y += y
        # need to implement Z axis moving
        return 0
    
    def respawn(self):
        w = self.world
        self.__init__()
        self.world = w
        self.save()
        return 0

    def save(self):
         pickle.dump(self, open('player' + str(self.world), 'wb'))

    def load(self, world):
        self = pickle.load(open('player' + str(world), 'rb'))

# mob class
class Mob:
    def __init__(self, m, hp, ap, gold):
        self.marker = m
        self.x = random.randint(0,27)
        self.y = random.randint(0,27)
        self.health = hp
        self.attack = ap
        self.gold = gold

# dragon class
class Dragon:
    def __init__(self):
        import random
        self.x = random.randint(0, 27)
        self.y = random.randint(0, 27)
        self.health = 18
        self.alive = True

    def move(self):
        for i in random.randint(0, 1):
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)