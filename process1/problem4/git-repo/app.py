import flask

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, GitHub!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
