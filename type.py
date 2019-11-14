class Type():
    def __init__(self, name, vulnerable_to, resistant_to, immune_to):
        self.name = name
        self.vulnerable_to = vulnerable_to
        self.resistant_to = resistant_to
        self.immune_to = immune_to

NORMAL = Type("Normal", ["Fighting"], [], ["Ghost"])
FIRE = Type("Fire", ["Water", "Ground", "Rock"], ["Fire", "Grass", "Ice",
            "Bug", "Steel", "Fairy"], [])
WATER = Type("Water", ["Electric", "Grass"], ["Fire", "Water", "Ice", "Steel"],
             [])
ELECTRIC = Type("Electric", ["Ground"], ["Electric", "Flying", "Steel"], [])
GRASS = Type("Grass", ["Fire", "Ice", "Poison", "Flying", "Bug"],
             ["Water", "Electric", "Grass", "Ground"], [])
ICE = Type("Ice", ["Fire", "Fighting", "Rock", "Steel"], ["Ice"], [])
FIGHTING = Type("Fighting", ["Flying", "Psychic", "Fairy"],
                ["Bug", "Rock", "Dark"], [])
POISON = Type("Poison", ["Ground", "Psychic"], ["Grass", "Fighting", "Poison",
              "Bug", "Fairy"], [])
GROUND = Type("Ground", ["Water", "Grass", "Ice"], ["Poison", "Rock"],
              ["Electric"])
FLYING = Type("Flying", ["Electric", "Ice", "Rock"], ["Grass", "Fighting",
              "Bug"], ["Ground"])
PSYCHIC = Type("Psychic", ["Bug", "Ghost", "Dark"], ["Fighting", "Psychic"], [])
BUG = Type("Bug", ["Fire", "Flying", "Rock"], ["Grass", "Fighting", "Ground"],
           [])
ROCK = Type("Rock", ["Water", "Grass", "Fighting", "Ground", "Steel"],
            ["Normal", "Fire", "Poison", "Flying"], [])
GHOST = Type("Ghost", ["Ghost", "Dark"], ["Poison", "Bug"], ["Normal",
             "Fighting"])
DRAGON = Type("Dragon", ["Ice", "Dragon", "Fairy"], ["Fire", "Water",
              "Electric", "Grass"], [])
DARK = Type("Dark", ["Fighting", "Bug", "Fairy"], ["Ghost", "Dark"],
            ["Psychic"])
STEEL = Type("Steel", ["Fire", "Fighting", "Ground"], ["Normal", "Grass",
             "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon",
             "Steel", "Fairy"], ["Poison"])
FAIRY = Type("Fairy", ["Poison", "Steel"], ["Fighting", "Bug", "Dark"],
             ["Dragon"])
