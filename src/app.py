from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def get():
    return "OK", 200

@app.route("/print", methods=['GET'])
def print_something():
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    return "OK", 200

@app.route("/exception", methods=['GET'])
def exp():
    raise "This is an unexpected error."
    return "OK", 200

def create_app():
    return app