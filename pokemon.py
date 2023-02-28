import requests

def pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    pokemon = response.json()
    pokemon_data = {
    'Pokemon': pokemon['forms'][0]['name'].title(),
    'Base_experience': pokemon['base_experience'],
    'Sprite': pokemon['sprites']['back_default']
    }
    return pokemon_data

print(pokemon_info('pikachu'))
print(pokemon_info('bulbasaur'))
print(pokemon_info('charizard'))
print(pokemon_info('squirtle'))
print(pokemon_info('wartortle'))