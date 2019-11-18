import pokemon
import random

def attack(pokemon, move):
    

def battle(player, trainer_2):
    opponent_party_index = 0
    player_pokemon = player.party[0]
    opponent_pokemon = trainer_2.party[opponent_party_index]
    while True:
        player_usable_pokemon = [p for p in player.party if p.current_hp > 0]
        opponent_usable_pokemon = [p for p in trainer_2.party if p.current_hp > 0]

        if len(player_usable_pokemon) <= 0:
            return "loss"
        if len(opponent_usable_pokemon) <= 0:
            return "win"

        if player_pokemon.current_hp <= 0:
            player_pokemon.fainted = True
            opponent_party_index += 1

        print("\nYOUR POKEMON")

        print("Lv. " + str(player_pokemon.level) + " "
              + player_pokemon.name + " (" + str(player_pokemon.current_hp)
              + "/" + str(player_pokemon.stats["hp"]) + " HP)")

        print("\nATTACKS")
        for i in range(len(player_pokemon.moves)):
            print(str(i + 1) + ". " + player_pokemon.moves[i].name)

        move = input("\nWhat will you do? ")
