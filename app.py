from flask import Flask, render_template

JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000"
}]

app = Flask(__name__)


@app.route("/")
def hello():
  return render_template('index.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
