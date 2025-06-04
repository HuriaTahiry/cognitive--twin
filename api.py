from flask import Flask, request, jsonify
from twin_store import TwinStore
from survey_processor import build_cognitive_twin, neurotransmitter_vector

app = Flask(__name__)
store = TwinStore()

@app.route("/create_twin", methods=["POST"])
def create_twin():
    data = request.json
    twin_id, vec = store.add_twin(data)
    return jsonify({"message": "Cognitive Twin Created", "id": twin_id})

@app.route("/search_similar", methods=["POST"])
def search_similar():
    data = request.json
    profile = build_cognitive_twin(data)
    vec = neurotransmitter_vector(profile)
    results = store.search_similar(vec, k=3)
    return jsonify({"results": results})

@app.route("/")
def home():
    return " Cognitive Twin API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)

