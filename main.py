from flask import *

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html", arg1 = "Hello", arg2 = "World"


@app.route("/test")
def test():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
