from pokeapi_client import PokeAPIClient
import os
clean = lambda: os.system('cls' if os.name == 'nt' else 'clear')

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
    pokemon_name = input(' Digite o nome do pokémon: ')

    # cria uma instância do cliente HTTP da Pokeapi
    pokeapi_client = PokeAPIClient()
    # busca pokémon no cliente da Pokeapi
    pokemon = pokeapi_client.get_pokemon(pokemon_name)

    if pokemon == None:
        print('\n \'~\' ERRO. Pokémon não encontrado. \'~\' ')
    else:
        print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n')
        print(' Infos do Pokémon ⮯ \n')
        print(f' ID: {pokemon.id}')
        print(f' Nome: {pokemon.name.capitalize()}')
        print(' Tipo(s): ', ', '.join(pokemon.types))

    print(' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n')
    reset = input(' Deseja reiniciar? [S/N]: ').upper()
    if reset == 'S': 
      clean()
      continue
    break
