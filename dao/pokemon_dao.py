import sqlite3
from model.pokemon import Pokemon
from datetime import datetime


connection = sqlite3.connect('pokedex.db')
cursor = connection.cursor()


class PokemonDao:
    table_name = 'pokemons'

    def create(self, pokemon):
        cursor.execute(f'INSERT INTO {self.table_name} VALUES (?, ?, ?, ?)', 
                      (pokemon.id, pokemon.name, ','.join(pokemon.types), datetime.now()))
        # confirma a transação com o banco
        connection.commit()

    def exists(self, name):
        return self.get(name) != None

    def get(self, name):
        cursor.execute(f'SELECT id, name, types, timestamp FROM {self.table_name} \
                        WHERE name = :name', {'name': name})

        response = cursor.fetchone()

        if response == None:
            return

        id, name, types, timestamp = response
        types = types.split(',')
        pokemon = Pokemon(id, name, types, timestamp)

        return pokemon

    def update(self, pokemon):
        cursor.execute(f'UPDATE {self.table_name} SET name = ?, types = ?, \
                       timestamp = ? WHERE id = ?', (pokemon.name, ','.join(pokemon.types), 
                       datetime.now(), pokemon.id))
        connection.commit()
