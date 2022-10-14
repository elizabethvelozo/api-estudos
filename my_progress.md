# 🌐 Cliente PokeAPI

## 👩🏽‍💻 Objetivo 2:

Adicionar **Banco de Dados** ao projeto "Cliente PokeAPI" por meio da biblioteca **SQLite3**.

🔗 [Para testar clique aqui](https://replit.com/@elizabethvelozo/cliente-pokeapi-v2).
(PS.: Clique em `▶️ Run` no Replit)

### :jigsaw: Componentes adicionados:
- DAO Pokémon

### 🌌 Fluxo

- 1. Solicitar informação do usuário;
- 2. Criar banco e tabela caso não existam;
- 3. Consultar a existência da informação no banco;
- 4. Em caso afirmativo e, se o pokémon tiver sido cadastrado há mais de 10 minutos, deve-se fazer uma consulta à API e atualizar as informações no banco;
- 4. Em caso negativo, deve-se fazer uma consulta à API e cadastrar as informações no banco;
- 5. A não ser que o pokémon não exista no mundo dos Pokémons, exibir informações sobre ele ao usuário.

## 👩🏽‍💻 Objetivo 1: 

Fazer consumo da [PokeAPI](https://pokeapi.co/) em Python 
puro. 

🔗 [Para testar clique aqui](https://replit.com/@elizabethvelozo/cliente-pokeapi).
(PS.: Clique em `▶️ Run` no Replit)

### :jigsaw: Componentes:
- Modelo Pokémon
- Cliente HTTP da PokeAPI

### 🌌 Fluxo

- 1. Solicitar informação do usuário;
- 2. Criar as variáveis para armanezar essa informação;
- 3. Consultar a PokeAPI passando a variável;
- 4. Tratar o retorno da API para extrair a informação desejada;
- 5. Exibir ao usuário.