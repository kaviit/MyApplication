<<<<<<< HEAD
from flask import Flask, jsonify  # import objects from the flask model
import os, subprocess

app = Flask(__name__)  # define app using flask

service_name = "myapplication"
version = "1.0.0"
git_head_hash = subprocess.check_output(["git", "rev-parse", "HEAD"])
git_head_hash = git_head_hash.decode("utf-8").rstrip("\n")
service_port = os.getenv("service_port")
log_level = os.getenv("log_level")


@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "it works!"})


@app.route("/info", methods=["GET"])
def info():
    info = {
        "service_name": service_name,
        "version": version,
        "git_commit_sha": git_head_hash,
        "environment": {"service_port": service_port, "log_level": log_level},
    }
    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=service_port)  # run app on service_port

=======
from flask import Flask, jsonify  # import objects from the flask model
from os import environ
import subprocess

app = Flask(__name__)  # define app using flask

service_name = "myapplication"
version = "1.0.0"
process = subprocess.Popen(
    ["git", "rev-parse", "HEAD"], shell=False, stdout=subprocess.PIPE
)
git_head_hash = process.communicate()[0].strip()
service_port = environ.get("SERVICE_PORT")
log_level = environ.get("LOG_LEVEL")
output = {
    "service_name": service_name,
    "version": version,
    "git_commit_sha": git_head_hash,
    "environment": {"service_port": service_port, "log_level": log_level},
}


@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "it works!"})


@app.route("/info", methods=["GET"])
def returnAll():
    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(
        debug=True, host="0.0.0.0", port=service_port
    )  # run app on service_port in debug model

>>>>>>> 70c0f643f2d82a4ebf3e2770c8f81bddeda1836e
