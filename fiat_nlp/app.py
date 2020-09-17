from flask import Flask, jsonify, request

from .utils import Recommendation, parse_entities
from .watson_nlu import process_text
from .watson_stt import get_file_text

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = request.args.get("user")
    return f"Hello, World {user}!"


@app.route("/nlp", methods=["POST"])
def process_query():
    if request.files:
        file = request.files["audio"]
        text = get_file_text(file)
    else:
        text = request.form.get("text")
    try:
        nlu_response = process_text(text)
    except Exception as err:
        return jsonify({"error": str(err)})
    car = request.form.get("car")
    entities = parse_entities(nlu_response)
    recommendation = Recommendation(car, entities)
    response = {"entities": entities}
    response["recommendation"] = recommendation.get()
    return jsonify(response)
