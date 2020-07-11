from pokemon_battle_mine.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self,pokemon:Pokemon):
        if pokemon.name in map(lambda x: x.name, self.pokemon):
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"
    def release_pokemon(self,pokemon_name:str):
        pok = [p for p in self.pokemon if pokemon_name == p.name]
        if pok:
            self.pokemon.remove(pok[0])
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"
    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- "
        for el in self.pokemon:
            result+=el.pokemon_details()+"\n"
        return result

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())


