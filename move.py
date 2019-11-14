import type

class Move():
    def __init__(self, name, type, category, power, accuracy, range, effect=None):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.range = range
        self.effect = effect

GROWL = Move("Growl", type.NORMAL, "status", "enemy", 0, 100)
TACKLE = Move("Tackle", type.NORMAL, "physical", "enemy", 40, 100)
VINE_WHIP = Move("Vine Whip", type.GRASS, "status", "enemy", 45, 100)
GROWTH = Move("Growth", type.NORMAL, "status", "self", 0, 100)
