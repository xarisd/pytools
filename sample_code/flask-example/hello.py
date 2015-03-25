"""A simple Hello World web application using Flask"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """Hello route"""
    return "Hello World!"
if __name__ == "__main__":
    app.run()
