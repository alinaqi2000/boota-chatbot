from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from .bot import prompt_input

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def home():
    return jsonify({"app_name": "Boota - ChatBot API", "version": "0.0.1", "author": "Ali Naqi Al-Musawi"})


@app.route("/prompt", methods=["POST"])
@cross_origin()
def user_prompt():
    request_body = request.get_json() 
    if (request_body.get('prompt') == None):
        return jsonify({"error": "Please write a valid input!"})

    return ({"response": prompt_input(request_body.get('prompt'))}), 201