import random
import type
import nature
import move

class PokemonTemplate():
    def __init__(self, name, type, exp, hpev, atkev, defev, spatkev, spdefev,
                 speedev, hpbase, atkbase, defbase, spatkbase, spdefbase,
                 speedbase, learnable_attacks, front_sprite, back_sprite):
        self.name = name
        self.type = type
        self.granted_experience = exp
        self.granted_evs = {"hp": hpev, "atk": atkev, "def": defev,
                            "spatk": spatkev, "spdef": spdefev,
                            "speed": speedev}
        self.base_stats = {"hp": hpbase, "atk": atkbase, "def": defbase,
                           "spatk": spatkbase, "spdef": spdefbase,
                           "speed": speedbase}
        self.learnable_attacks = learnable_attacks
        self.front_sprite = front_sprite
        self.back_sprite = back_sprite

class Pokemon():
    def __init__(self, template, level):
        self.name = template.name
        self.template = template
        self.level = level
        self.nature = random.choice(nature.NATURES)

        self.ivs = {"hp": 0, "atk": 0, "def": 0, "spatk": 0, "spdef": 0,
                    "speed": 0}

        for iv in self.ivs:
            self.ivs[iv] = random.randint(0, 15)

        self.evs = {"hp": 0, "atk": 0, "def": 0, "spatk": 0, "spdef": 0,
                    "speed": 0}

        self.stats = {"hp": 0, "atk": 0, "def": 0, "spatk": 0, "spdef": 0,
                      "speed": 0}

        self.attacks = []

        self.generate_stats()

    def generate_stats(self):
        self.stats["hp"] = round(((((2 * self.template.base_stats["hp"])
                         + self.ivs["hp"] + ((self.evs["hp"] / 4) * self.level))
                         / 100)) + self.level + 10)

        for stat in self.stats:
            if stat != "hp":
                self.stats[stat] = round(((((2 * self.template.base_stats[stat]
                                 + self.ivs[stat] + (self.evs["hp"] / 4))
                                 * self.level) / 100) + 5)
                                 * self.nature.stat_modifications[stat])

BULBASAUR = PokemonTemplate("Bulbasaur", type.GRASS, 64, 0, 0, 0, 1, 0, 0, 45,
                            49, 49, 65, 65, 45,
                            {1: [move.GROWL, move.TACKLE],
                             3: [move.VINE_WHIP],
                             6: [move.GROWTH],
                             9: [move.LEECH_SEED],
                             12: [move.RAZER_LEAF],
                             15: [move.POISON_POWDER, move.SLEEP_POWDER],
                             18: [move.SEED_BOMB],
                             21: [move.TAKE_DOWN],
                             24: [move.SWEET_SCENT],
                             27: [move.SYNTHESIS],
                             30: [move.WORRY_SEED],
                             33: [move.DOUBLE_EDGE],
                             36: [move.SOLAR_BEAM]},
                            "bulbasaur_front.png", "bulbasaur_back.png")

test_pokemon = Pokemon(BULBASAUR, 5)

# print("Lv. " + str(test_pokemon.level) + " " + test_pokemon.name)
# print("TYPE: " + test_pokemon.template.type.name)
# print("NATURE: " + test_pokemon.nature.name)

# for stat in test_pokemon.stats:
#     print(stat.upper() + ": " + str(test_pokemon.stats[stat]))
