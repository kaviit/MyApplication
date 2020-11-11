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
    app.run(
        debug=True, host="0.0.0.0", port=service_port
    )  # run app on service_port in debug mode

