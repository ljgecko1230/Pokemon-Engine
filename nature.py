class Nature():
    def __init__(self, name, atkmod, defmod, spatkmod, spdefmod, speedmod):
        self.name = name
        self.stat_modifications = {"atk": atkmod, "def": defmod,
                                   "spatk": spatkmod, "spdef": spdefmod,
                                   "speed": speedmod}

HARDY = Nature("Hardy", 1, 1, 1, 1, 1)
LONELY = Nature("Lonely", 1.1, 0.9, 1, 1, 1)
ADAMANT = Nature("Adamant", 1.1, 1, 0.9, 1, 1)
NAUGHTY = Nature("Naughty", 1.1, 1, 1, 0.9, 1)
BRAVE = Nature("Brave", 1.1, 1, 1, 1, 0.9)
BOLD = Nature("Bold", 0.9, 1.1, 1, 1, 1)
DOCILE = Nature("Docile", 1, 1, 1, 1, 1)
IMPISH = Nature("Impish", 1, 1.1, 0.9, 1, 1)
LAX = Nature("Lax", 1, 1.1, 1, 0.9, 1)
RELAXED = Nature("Relaxed", 1, 1.1, 1, 1, 0.9)
MODEST = Nature("Modest", 0.9, 1, 1.1, 1, 1)
MILD = Nature("Mild", 1, 0.9, 1.1, 1, 1)
BASHFUL = Nature("Bashful", 1, 1, 1, 1, 1)
RASH = Nature("Rash", 1, 1, 1.1, 0.9, 1)
QUIET = Nature("Quiet", 1, 1, 1.1, 1, 0.9)
CALM = Nature("Calm", 0.9, 1, 1, 1.1, 1)
GENTLE = Nature("Gentle", 1, 0.9, 1, 1.1, 1)
CAREFUL = Nature("Careful", 1, 1, 0.9, 1.1, 1)
QUIRKY = Nature("Quirky", 1, 1, 1, 1, 1)
SASSY = Nature("Sassy", 1, 1, 1, 1.1, 0.9)
TIMID = Nature("Timid", 0.9, 1, 1, 1, 1.1)
HASTY = Nature("Hasty", 1, 0.9, 1, 1, 1.1)
JOLLY = Nature("Jolly", 1, 1, 0.9, 1, 1.1)
NAIVE = Nature("Naive", 1, 1, 1, 0.9, 1.1)
SERIOUS = Nature("Serious", 1, 1, 1, 1, 1)
NATURES = [HARDY, LONELY, ADAMANT, NAUGHTY, BRAVE, BOLD, DOCILE, IMPISH,
           LAX, RELAXED, MODEST, MILD, BASHFUL, RASH, QUIET, CALM, GENTLE,
           CAREFUL, QUIRKY, SASSY, TIMID, HASTY, JOLLY, NAIVE, SERIOUS]
