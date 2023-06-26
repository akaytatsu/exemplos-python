import json
import urllib.request

# Define o cabeçalho de usuário
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Faz a requisição à API e obtém os dados dos 10 primeiros pokemons
url = 'https://pokeapi.co/api/v2/pokemon?limit=10'
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
data = json.loads(response.read())['results']

# Escreve os dados em um arquivo de texto
with open('pokemons.txt', 'w') as file:
    for pokemon in data:
        file.write(pokemon['name'] + '\n')