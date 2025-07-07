import requests

base_url = "https://api.pokemonbattle.ru"
api_version = "v2"
headers = {
    "Content-Type": "application/json",
    "trainer_token": "a00bf87466a5d99f787d39c16233e5c2"
}

url_pokemons = f"{base_url}/{api_version}/pokemons"
url_add_pokeball = f"{base_url}/{api_version}/trainers/add_pokeball"

response_create = requests.post(url_pokemons, headers=headers, json={"name": "Python", "photo_id": 10})
pokemon_id = response_create.json().get('id')

response_update = requests.put(url_pokemons, headers=headers, json={"pokemon_id": str(pokemon_id), "name": "Жора", "photo_id": 10})

response_pokeball = requests.post(url_add_pokeball, headers=headers, json={"pokemon_id": str(pokemon_id)})

print("Создан покемон:", response_create.json())
print("Ответ при смене имени:", response_update.json())
print("Ответ при поймке в покебол:", response_pokeball.json())