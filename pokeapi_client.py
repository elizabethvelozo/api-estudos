import requests
from model.pokemon import Pokemon

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

class PokeAPIClient:
    ''' Abstração do cliente HTTP para consumir a Pokeapi. '''

    def get_pokemon(self, name):
        ''' Busca um pokémon por meio de uma requisição HTTP,
            retornando um modelo limpo. '''
        try:
            response = requests.get(BASE_URL+name)

            response.raise_for_status()
        
            response = response.json()
            types = [type['type']['name'] for type in response['types']]
            pokemon = Pokemon(response['id'], response['name'], types)

            return pokemon
        except requests.exceptions.HTTPError as error:
            print (' Erro de HTTP:', error)
        except requests.exceptions.ConnectionError as error:
            print (' Erro de conexão:', error)
        except requests.exceptions.Timeout as error:
            print (' Tempo excedido:', error)
        except requests.exceptions.RequestException as error:
            print (' Algo deu errado:', error)
