import re

FILE_PATH = 'chat_data_min.txt'


def process_dataset():
    conversations = []

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_conversation = []

    for line in lines:
        line = line.strip()

        if line:
            user_match = re.match(r'^USER: (.+)', line)
            bot_match = re.match(r'^BOT: (.+)', line)

            if user_match:
                current_conversation.append(('user', user_match.group(1)))
            elif bot_match:
                current_conversation.append(('bot', bot_match.group(1)))

        elif current_conversation:
            conversations.append(current_conversation)
            current_conversation = []

    if current_conversation:
        conversations.append(current_conversation)

    return conversations
