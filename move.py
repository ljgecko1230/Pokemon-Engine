import type

class Move():
    def __init__(self, name, type, category, range, power, accuracy, pp, effect=None):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.range = range
        self.pp = pp
        self.effect = effect

GROWL = Move("Growl", type.NORMAL, "status", "enemy", 0, 100, 40)
TAIL_WHIP = Move("Tail Whip", type.NORMAL, "status", "enemy", 0, 100, 30)
TACKLE = Move("Tackle", type.NORMAL, "physical", "enemy", 40, 100, 35)
QUICK_ATTACK = Move("Quick Attack", type.NORMAL, "physical", "enemy", 40, 100, 30)
VINE_WHIP = Move("Vine Whip", type.GRASS, "status", "enemy", 45, 100, 25)
GROWTH = Move("Growth", type.NORMAL, "status", "self", 0, 100, 20)
FOCUS_ENERGY = Move("Focus Energy", type.NORMAL, "status", "self", 0, 100, 30)
LEECH_SEED = Move("Leech Seed", type.GRASS, "status", "enemy", 0, 90, 10)
RAZOR_LEAF = Move("Razor Leaf", type.GRASS, "physical", "enemy", 55, 95, 25)
BITE = Move("Bite", type.DARK, "physical", "enemy", 60, 100, 25)
SUPER_FANG = Move("Super Fang", type.NORMAL, "physical", "enemy", 0, 90, 10)
CRUNCH = Move("Crunch", type.DARK, "physical", "enemy", 80, 100, 15)
HYPER_FANG = Move("Hyper Fang", type.NORMAL, "physical", "enemy", 80, 90, 15)
POISON_POWDER = Move("Poison Powder", type.POISON, "status", "enemy", 0, 75, 35)
SLEEP_POWDER = Move("Sleep Powder", type.GRASS, "status", "enemy", 0, 75, 15)
SEED_BOMB = Move("Seed Bomb", type.GRASS, "physical", "enemy", 80, 100, 15)
TAKE_DOWN = Move("Take Down", type.NORMAL, "physical", "enemy", 90, 85, 20)
SWEET_SCENT = Move("Sweet Scent", type.NORMAL, "status", "self", 0, 100, 20)
SYNTHESIS = Move("Synthesis", type.GRASS, "status", "self", 0, 100, 5)
WORRY_SEED = Move("Worry Seed", type.GRASS, "status", "self", 0, 100, 10)
DOUBLE_EDGE = Move("Double Edge", type.NORMAL, "physical", "enemy", 120, 100, 15)
SUCKER_PUNCH = Move("Sucker Punch", type.DARK, "physical", "enemy", 70, 100, 5)
