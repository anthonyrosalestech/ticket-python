from routes import Aspazul
from flask import Flask, jsonify, request
from config import config

app = Flask(__name__)


@app.route("/")
def root():
    return "Home app "


@app.route("/user/<user_id>")
def get_user(user_id):
    user = {"id": user_id}
    query = request.args
    print(query)
    if query:
        user["query"] = query
    return jsonify(user), 200


def page_not_found():
    return '<h1>Not found</h1>'


if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_blueprint(Aspazul.main, url_prefix='/api/')
    # app.register_error_handler(404, page_not_found)
    app.run(debug=True)
else:
    app.run()
