import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '45c1366bf8e37f91d1f8638ba5374913'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Котик",
    "photo_id": 937
}

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

body_change = {
    "pokemon_id": "72851",
    "name": "Super",
    "photo_id": 936
}

response_change= requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_add = {
    "pokemon_id": "72851"
}

response_add= requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)
