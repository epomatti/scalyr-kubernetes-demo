from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def get():
    return "OK", 200

@app.route("/print", methods=['GET'])
def print_test():
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    return "OK", 200

@app.route("/exception", methods=['DELETE'])
def exp():
    raise "This is an unexpected error."
    return "OK", 200

def create_app():
    return app