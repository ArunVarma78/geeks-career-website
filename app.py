from flask import Flask, render_template, jsonify
from config.db import JOBS

app = Flask(__name__)


@app.route("/")
def hello():
  return render_template('index.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
