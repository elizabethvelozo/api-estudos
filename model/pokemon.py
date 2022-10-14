class Pokemon:

    def __init__(self, id, name, types, timestamp = None):
        self.id = id
        self.name = name
        self.types = types
        self.timestamp = timestamp

    def __str__(self):
        return f''' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n
 Infos do Pokémon ⮯\n
 ID: {self.id}
 Nome: {self.name.capitalize()}
 Tipo(s): {', '.join(self.types)}'''
