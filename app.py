

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Custum web server is a go!!!"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=80)
