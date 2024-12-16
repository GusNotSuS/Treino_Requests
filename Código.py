import requests


url_base = "https://pokeapi.co/api/v2/"

def get_info_pokemon():
    nome = str(input('digite o nome do pokemon\n')).lower()
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
def menu():
    while True:
        opção = int(input('PokeAPI, selecione uma opção:\n1 para ver informação básica de um pokemon\n2 para localização de pokemons em jogos\n3 para egg moves \n0 para encerrar o codigo\n'))
        if opção == 1:
            get_info_pokemon()
        if opção == 0:
            break
        else:
            print('Opção invalida')

menu()