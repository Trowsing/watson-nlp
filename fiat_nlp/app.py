from flask import Flask, jsonify, request, redirect

from fiat_nlp.utils import Recommendation, parse_entities
from fiat_nlp.watson_nlu import process_text
from fiat_nlp.watson_stt import get_file_text


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/ping")


@app.route("/ping")
def ping():
    return "Pong"


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


if __name__ == "__main__":
    app.run(port=5000)
