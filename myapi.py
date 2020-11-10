from flask import Flask, jsonify  # import objects from the flask model
from os import environ
import subprocess

app = Flask(__name__)  # define app using flask

service_name = "myapplication"
version = "1.0.0"
process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
git_head_hash = process.communicate()[0].strip()
service_port = environ.get("SERVICE_PORT")
log_level = environ.get("LOG_LEVEL")

@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "it works!"})

@app.route("/info", methods=["GET"])
def returnAll():
output = {
    "service_name": service_name,
    "version": version,
    "git_commit_sha": git_head_hash,
    "environment": {
        "service_port": service_port,
        "log_level": log_level,
    },}
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=service_port)  # run app on service_port in debug model

