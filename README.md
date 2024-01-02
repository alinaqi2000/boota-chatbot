# Boota Chatbot

Boota is a simple yet powerful chatbot that uses Flask for the backend and React for the frontend. The chatbot is designed to receive prompts and search for possible responses within conversations stored in text files. Whether you're looking to add a conversational interface to your application or just want to explore the world of chatbots, Boota is a great starting point.

## Features

- **Flask Backend**: The backend of Boota is powered by Flask, a lightweight web framework for Python. It efficiently handles incoming prompts and searches for responses within the stored conversations.

- **React Frontend**: Boota's frontend is built with React, providing a responsive and interactive user interface. Users can easily interact with the chatbot and view the responses in real-time.

- **Conversation Storage**: Conversations are stored in text files, allowing for easy customization and expansion of the chatbot's knowledge base. You can modify or extend the conversations to tailor Boota to your specific use case.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) installed on your machine
- [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/) installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/alinaqi2000/boota-chatbot.git
    cd boota-chatbot
    ```

2. Install dependencies for the frontend:

    ```bash
    cd frontend
    npm install
    ```

3. Install dependencies for the backend:

    ```bash
    cd ../backend
    pip install -r requirements.txt
    ```

### Usage

1. Start the Flask backend:

    ```bash
    cd backend
    python app.py
    ```

   The backend will be running at `http://localhost:5000`.

2. Start the React frontend:

    ```bash
    cd ../frontend
    npm start
    ```

   The frontend will be accessible at `http://localhost:3000`.

3. Open your browser and navigate to `http://localhost:3000` to interact with Boota.

## Customize Conversations

You can customize the conversations by editing the text file `backend/chat_data.txt`. It represents a conversation, and you can add, modify, or remove entries to suit your needs.

## Contributing

If you have ideas for improvements or new features, feel free to contribute! Fork the repository, create a branch, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Flask and React communities for creating powerful frameworks that make projects like Boota possible.

Enjoy chatting with Boota! 🤖💬