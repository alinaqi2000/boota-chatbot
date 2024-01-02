import random
from .process_data import process_dataset


def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]


def preprocess_text(text):
    # text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # return text.lower()
    return text


def train_chatbot(dataset):
    responses = {}

    for conversation in dataset:
        for i in range(len(conversation) - 1):
            user_message = preprocess_text(conversation[i][1])
            bot_message = preprocess_text(conversation[i + 1][1])

            if user_message not in responses:
                responses[user_message] = [bot_message]
            else:
                responses[user_message].append(bot_message)

    return responses


def get_response(user_input, responses):
    user_input = preprocess_text(user_input)

    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that."


def prompt_input(input_prompt):
    dataset = process_dataset()

    chatbot_responses = train_chatbot(dataset)

    return get_response(input_prompt, chatbot_responses)
