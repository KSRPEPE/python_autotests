import requests

url = "https://api.pokemonbattle.ru/v2/pokemons"
token = "a00bf87466a5d99f787d39c16233e5c2"
headers = {
    "Content-Type": "application/json",
    "trainer_token": token
}

body_update = {
    "pokemon_id": "333776", 
    "name": "Nika",
    "photo_id": 89  
}

response = requests.put(
    url=url,
    headers=headers,
    json=body_update
)

print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)