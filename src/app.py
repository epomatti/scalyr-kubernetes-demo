from flask import Flask
import logging

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return "OK", 200


@app.route("/print", methods=["GET"])
def print_something():
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    print("#### DEVELOPMENT TEST ####")
    return "OK", 200


@app.route("/exception", methods=["GET"])
def exp():
    raise "This is an unexpected error."


@app.route("/logging", methods=["GET"])
def exp():
    logging.warning("Watch out!")  # will print a message to the console
    logging.info("I told you so")  # will not print anything
    return "OK", 200


def create_app():
    return app
