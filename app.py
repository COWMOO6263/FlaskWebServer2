from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Custum web server is a go!!!"
