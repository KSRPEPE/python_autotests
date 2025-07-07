import requests

BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = 35932

def test_get_trainers_status_code():
    url = f"{BASE_URL}/trainers?trainer_id={TRAINER_ID}"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_trainers_contains_name():
    url = f"{BASE_URL}/trainers?trainer_id={TRAINER_ID}"
    response = requests.get(url)
    assert "Ash" in response.text