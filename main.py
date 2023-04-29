from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__)
building_id = -1


@app.route("/")
@app.route("/home") 
def home():
    return render_template("home.html")


@app.route("/sign-up")
def signup():
    return render_template("sign-up.html")


@app.route("/buildings-view")
def building():
    return render_template("buildings-view.html")


@app.route(f"/buildings-view/{building_id}")
def building_id(building_id):
    return render_template("building.html", building_id=building_id)


if __name__ == "__main__":
    app.run(debug=True)
