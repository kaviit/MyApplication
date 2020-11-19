from flask import Flask, jsonify  # import objects from the flask model
import os, subprocess

app = Flask(__name__)  # define app using flask
app.config["JSON_SORT_KEYS"] = False  # Prevent Flask jsonify from sorting the data

service_name = "myapplication"
version = "1.0.0"
git_hash = subprocess.check_output(["git", "rev-parse", "head"]).decode("utf-8")
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
        "git_commit_sha": git_hash,
        "environment": {"service_port": service_port, "log_level": log_level},
    }
    return jsonify(info)


if __name__ == "__main__":
    app.run(
        debug=True, host="0.0.0.0", port=service_port
    )  # run app on service_port in debug mode

