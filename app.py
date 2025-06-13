from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from jard.jard import Jard

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
CORS(app)  # Allows requests from React


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/jard", methods=["POST"])
def jard():
    jard = Jard()

    data = request.json
    result = jard.slide_window(data)
    return jsonify({"result": result})


@app.route("/jard", methods=["POST"])
def jard():
    jard = Jard()

    result = jard.slide_window(
        [
            {"strbluprnt": "slide window", "w": 149.5, "h": 175.7},
        ]
    )
    return jsonify({"result": result})


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
