import requests
from tabulate import tabulate
from plyer import notification 

# Função para exibir alerta usando plyer
def alerta():
    notification.notify(
        title='Erro na API!',
        message='Ocorreu um erro ao acessar a API.',
        timeout=5  
    )

# URL base da API
base_url = 'https://pokeapi.co/api/v2/pokemon'

# Função para buscar dados da API
def buscar_dados():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            alerta()
            return None
    except requests.exceptions.RequestException as e:
        alerta()
        return None

# Função para extrair e mostrar tabelas
def extrair_e_mostrar_tabelas():
    data = buscar_dados()
    if data:
        # Extração e exibição de tabelas simples
        pokemons = data['results'][:10]  # 10 primeiros pokémons

        # Tabela 1: Listagem simples de pokémons
        headers = ["ID", "Nome"]
        table1 = [[i + 1, pokemon['name'].capitalize()] for i, pokemon in enumerate(pokemons)]
        print("\nTabela 1: Listagem de Pokémons")
        print(tabulate(table1, headers=headers))

        # Tabela 2: Detalhes de um pokémon específico (primeiro da lista)
        first_pokemon_url = pokemons[0]['url']
        response = requests.get(first_pokemon_url)
        if response.status_code == 200:
            pokemon_data = response.json()
            abilities = [ability['ability']['name'].capitalize() for ability in pokemon_data['abilities']]
            stats = {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokemon_data['stats']}
            table2 = [["Nome", pokemon_data['name'].capitalize()],
                      ["Altura", pokemon_data['height']],
                      ["Peso", pokemon_data['weight']],
                      ["Habilidades", ", ".join(abilities)]]
            print("\nTabela 2: Detalhes do Pokémon {}".format(pokemon_data['name'].capitalize()))
            print(tabulate(table2))

        # Tabela 3: Tipos de todos os pokémons na lista
        table3 = [["ID", "Nome", "Tipos"]]
        for pokemon in pokemons:
            response = requests.get(pokemon['url'])
            if response.status_code == 200:
                pokemon_data = response.json()
                types = ", ".join([t['type']['name'].capitalize() for t in pokemon_data['types']])
                table3.append([pokemon_data['id'], pokemon_data['name'].capitalize(), types])
        
        print("\nTabela 3: Tipos dos Pokémons")
        print(tabulate(table3))

# Chamada da função principal para execução
extrair_e_mostrar_tabelas()