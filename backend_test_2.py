import json
from urllib.request import urlopen


pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1/'
pokemon_form_url = 'https://pokeapi.co/api/v2/pokemon-form/1/'


def get_json_response(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

pokemon_data = get_json_response(pokemon_url)

filter_stats = [stat for stat in pokemon_data['stats'] if stat['stat']['name'] in ('hp', 'attack')]

pokemon_form_data = get_json_response(pokemon_form_url)

name = pokemon_form_data['name']
sprites = pokemon_form_data['sprites']

new_json_object = {
    'stats': filter_stats,
    'name': name,
    'sprites': sprites
    
}


text = (json.dumps(new_json_object, indent=2))
 
f = open("result_test_2.json", "wt")
f.write(text)  