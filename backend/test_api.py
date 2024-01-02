import requests
import pytest
from .process_data import process_dataset

api_url = "http://localhost:5000/prompt"

dataset = process_dataset()


@pytest.mark.parametrize("prompt_data", dataset)
def test_prompt_responses(prompt_data):
    user_input = next(
        (message[1] for message in prompt_data if message[0] == 'user'), None)
    bot_response = next(
        (message[1] for message in prompt_data if message[0] == 'bot'), None)

    response = requests.post(api_url, json={"prompt": user_input})
    assert response.status_code == 201
    assert response.json().get("response") == bot_response
