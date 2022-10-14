from pokeapi_client import PokeAPIClient
import os
clean = lambda: os.system('cls' if os.name == 'nt' else 'clear')
import sqlite3
from dao.pokemon_dao import PokemonDao
from utils import elapsed_minutes

while True:
    print('''
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
|    ____       _     __     _              |
|   |  _ \ ___ | | __/_/  __| | _____  __   |
|   | |_) / _ \| |/ / _ \/ _` |/ _ \ \/ /   |
|   |  __/ (_) |   <  __/ (_| |  __/>  <    |
|   |_|   \___/|_|\_\___|\__,_|\___/_/\_\   |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
    ''')
    pokemon_name = input(' Digite o nome do pokémon: ').lower()

    # cria banco e tabela caso não existam
    connection = sqlite3.connect('pokedex.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pokemons (id INT, \
                    name VARCHAR(20), types VARCHAR(30), timestamp DATETIME)')

    pokemon_dao = PokemonDao()

    if pokemon_dao.exists(pokemon_name) \
    and elapsed_minutes(pokemon_dao.get(pokemon_name).timestamp) <= 10:
        print(' ~ Pokémon encontrado no banco.')
        print(pokemon_dao.get(pokemon_name))
    else:
        # cria uma instância do cliente HTTP da Pokeapi
        pokeapi_client = PokeAPIClient()
        # busca pokémon no cliente da Pokeapi
        pokemon = pokeapi_client.get_pokemon(pokemon_name)

        if pokemon == None:
            print('\n \'~\' Pokémon não encontrado. \'~\' ')
        elif not pokemon_dao.exists(pokemon_name):
            pokemon_dao.create(pokemon)
            print(' ~ Cadastrando pokémon no banco...')
            print(pokemon_dao.get(pokemon_name))
        else:
            pokemon_dao.update(pokemon)
            print(' ~ Atualizando pokémon no banco...')
            print(pokemon_dao.get(pokemon_name))
    

    print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n')
    reset = input(' Deseja reiniciar? [S/N]: ').upper()
    if reset == 'S': 
      clean()
      continue
    break
