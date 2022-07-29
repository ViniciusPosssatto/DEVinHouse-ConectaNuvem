from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_w():
    return "<div style='backgroud-color:blue;'><h1>Hello, World!</h1></div>"
