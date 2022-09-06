import requests
from model.pokemon import Pokemon

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

class PokeAPIClient:
    ''' Abstração do cliente HTTP para consumir a Pokeapi. '''

    def get_pokemon(self, name):
        ''' Busca um pokémon por meio de uma requisição HTTP,
            retornando um modelo limpo. '''
        response = requests.get(BASE_URL+name)

        if response.status_code != 200:
            return

        response = response.json()
        types = [type['type']['name'] for type in response['types']]
        pokemon = Pokemon(response['id'], response['name'], types)

        return pokemon
