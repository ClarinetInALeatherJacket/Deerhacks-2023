from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy 
from os import path
from forms import RegistrationForm, LoginForm
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'insert good password here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parkings.db'
db = SQLAlchemy()
db.init_app(app)
# db.init_app(app)
building_id = -1

#
# Models for db
#

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phonenumber = db.Column(db.String(12), unique=True, nullable=True)
    license_plate = db.Column(db.String(8), unique=True, nullable=True)
    unit_number = db.Column(db.String(10), nullable=True)
    building = db.Column(db.Integer, nullable=True)
    manage_buildings = db.relationship('Building')
    bookings = db.relationship('Bookings')

    # def __init__(name: str, email: str, password: str, phonenumber: str,
    #              license_plate: str, unit_number: str):
    #     if id is not None:

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150), unique=True, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text(1000), nullable=True)
    bookings = db.relationship('Bookings')

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=func.now())
    duration = db.Column(db.Integer, nullable=False)
    visitor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resident_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login successful for {form.email.data}!", "success")
        return redirect(url_for("home"))
    return render_template("base.html", username="User", signedIn=False)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    print(request.method)
    user = ""
    if request.method == 'POST':
        email = request.form.get("email")
        user = email
        if email == "":
            flash("Failled to login, invalid email", category="error")
        else:
            flash(f"Login successful for {email}!", category="success")
    return render_template("sign-in.html", username=user , signedIn=False)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    print(request.method)
    user = ""
    errors = False
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        phonenumber = request.form.get("phonenumber")
        unit_number = request.form.get("unit_number")
        building = request.form.get("building")

        if email is None or len(email) < 4:
            errors = True
            flash("Email must be greater than 3 characters.", category="error")
        if name is None or len(name) < 2:
            errors = True
            flash("First name must be greater than 1 characters.", category="error")
        if password1 is None or password2 is None or password1 != password2:
            errors = True
            flash("Passwords do not match.", category="error")
        if password1 is None or len(password1) < 8:
            errors = True
            flash("Password must be atleast 8 charcaters.", category="error")
        if phonenumber != "" and len(phonenumber) < 10:
            errors = True
            flash("Phonenumber must be atleast 10 numbers(no spaces or - inbetween numbers).", category="error")
        if errors == False:
            flash(f"Sign Pp and Login successful for {email}!", "success")
            # new_user = User(name=name, password=generate_password_hash(password1, method='sha256'), phonenumber=phonenumber, email=email, unit_number=unit_number, building=building)
            # login_user(new_user, remember=True)
            # flash('Account created!', category='success')
            # db.session.add(new_user)
            # db.session.commit()

    return render_template("sign-up.html", username=user , signedIn=False, buildings=["2120 Burnamthorpe street, Mississauga", "2675 Hurontario street, Mississauga", "345 Backside street, Mississauga", "609 Ambush cresent, Mississauga"])


# @app.route("/sign-up")
# def signup():
#     return render_template("sign-up.html")


@app.route("/buildings-view")
def building():
    return render_template("buildings-view.html")


@app.route(f"/buildings-view/{building_id}")
def building_id(building_id):
    return render_template("building.html", building_id=building_id)


if __name__ == "__main__":
    if not path.exists('parkings.db'):
        with app.app_context():
            db.create_all()
        print("making db")
    app.run(debug=True)
