import requests


url_base = "https://pokeapi.co/api/v2/"

def get_info_pokemon():
    nome = str(input('digite o nome do pokemon ou número na pokedex\n')).lower()
    url = f"{url_base}/pokemon/{nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        Data_pokemon = resposta.json()
        pass
    else:
        print(f"falha ao obter dados, código de erro:{resposta.status_code}")
    if resposta:
        # Obter os tipos
        tipos = [tipo['type']['name'] for tipo in Data_pokemon['types']]
        # Montar a string do tipo
        if len(tipos) == 1:
            tipos_str = f"Tipo 1: {tipos[0].capitalize()}"
        elif len(tipos) == 2:
            tipos_str = f"Tipo 1: {tipos[0].capitalize()}, Tipo 2: {tipos[1].capitalize()}"
        print(f"nome: {Data_pokemon['name'].capitalize()}\nnumero na pokedex: {Data_pokemon['id']}\n{tipos_str}")


def location():
    # 1. Receber o nome do Pokémon e buscar dados
    pokemon = str(input("Digite o nome do pokemon ou número da pokedex: ")).lower()
    url_base = "https://pokeapi.co/api/v2/"
    url = f"{url_base}pokemon/{pokemon}/encounters"

    resposta = requests.get(url)
    if resposta.status_code == 200:
        Data_Pokemon = resposta.json()
        
        # 2. Organizar os dados por versão
        versions_data = {}
        for location in Data_Pokemon:
            for version in location["version_details"]:
                version_name = version["version"]["name"]
                if version_name not in versions_data:
                    versions_data[version_name] = []
                
                encounter_details = {
                    "local": location["location_area"]["name"],
                    "method": version["encounter_details"][0]["method"]["name"],
                    "chance": version["encounter_details"][0]["chance"]
                }
                versions_data[version_name].append(encounter_details)
        
        # 3. Mostrar as versões disponíveis
        print("\nVersões Disponíveis:")
        for idx, version in enumerate(versions_data.keys(), 1):
            print(f"{idx}. {version}")
        
        # 4. Perguntar ao usuário qual versão deseja ver
        version_choice = int(input("\nDigite o número da versão desejada: ")) - 1
        version_names = list(versions_data.keys())
        selected_version = version_names[version_choice]

        # 5. Exibir os detalhes da versão escolhida
        print(f"\nDetalhes de encontros para a versão '{selected_version}':\n")
        for encounter in versions_data[selected_version]:
            print(f"Local: {encounter['local']}, Método: {encounter['method']}, Chance: {encounter['chance']}%")
    else:
        print(f"Falha ao obter dados\nCódigo de erro: {resposta.status_code}")







def menu():
    # Menu Inicial
    while True:
        opção = int(input('PokeAPI, selecione uma opção:\n1 para ver informação básica de um pokemon\n2 para localização de pokemons em jogos\n0 para encerrar o codigo\n'))
        if opção == 1:
            get_info_pokemon()
        if opção == 2:
            location()
        if opção == 0:
            break

menu()