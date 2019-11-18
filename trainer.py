import pokemon

class Trainer():
    def __init__(self, name, party):
        self.name = name
        self.party = party

PLAYER = Trainer("Player", [pokemon.Pokemon(pokemon.BULBASAUR, 5)])
JOEY = Trainer("Joey", [pokemon.Pokemon(pokemon.RATTATA, 4)])
