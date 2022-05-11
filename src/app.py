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
def logging_function():
    logging.critical("CRITICAL")
    logging.error("ERROR")
    logging.warning("WARNING")
    logging.info("INFO")
    logging.debug("DEBUG")
    return "OK", 200


def create_app():
    return app
