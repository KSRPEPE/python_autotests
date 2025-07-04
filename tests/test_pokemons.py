import requests

BASE_URL = "https://api.pokemonbattle.ru/v2/trainers"
TRAINER_ID = "35932"
EXPECTED_NAME = "Ash"
TOKEN = "a00bf87466a5d99f787d39c16233e5c2"

def test_trainer_name_is_correct():
    headers = {
        "Content-Type": "application/json",
        "trainer_token": TOKEN,
    }
    params = {
        "trainer_id": TRAINER_ID
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    assert response.status_code == 200, f"Статус-код не 200, а {response.status_code}"
    resp_json = response.json()

    assert "data" in resp_json, "Нет ключа 'data' в ответе"
    assert isinstance(resp_json["data"], list), "'data' не является списком"
    assert len(resp_json["data"]) > 0, "'data' — пустой список, тренер не найден"

    trainer = resp_json["data"][0]
    actual_name = trainer.get("trainer_name")
    assert actual_name == EXPECTED_NAME, f"Имя тренера ({actual_name}) не совпадает с ожидаемым ({EXPECTED_NAME})"
