from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", message="Hello Flask!  I am on the Home page");


@app.route("/learning")
def learning():
    return render_template("learn.html", title="Learn", message="Hello Flask!  I am on the learning page");


@app.route("/resources")
def resources():
    return render_template("resources.html", title="Resources", message="Hello Flask!  I am on the resources page");

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)