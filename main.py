import logging
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def root():
    return "Home"


@app.route("/user/<user_id>")
def get_user(user_id):
    user = {"id": user_id}
    query = request.args
    print(query)
    if query:
        user["query"] = query
    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run()
