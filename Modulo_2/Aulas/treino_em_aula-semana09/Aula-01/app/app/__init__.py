from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_w():
    return "<p>Hello, World!</p>"
