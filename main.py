from flask import *

app = Flask(__name__)

guests = [ {"name": "Bobby Fischer", "license": "123456789", "duration": "24", "phone": "416-614-4114", "email": "ruh-roh@goofball.com"}, {"name": "Ubuntu", "email": "duh-doh@boofgall.com"} ]

@app.route("/")
def hello():
    return render_template("resident.html", name = "Magnus 'Opus' Carlson", address = "3579 True Road", unit = 101, hasGuest = True, guests = guests)


@app.route("/test")
def test():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
