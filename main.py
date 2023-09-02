from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm


db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'insert good password here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parkings.db'

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
    # phonenumber = db.Column(db.String(12), unique=True, nullable=True)
    # license_plate = db.Column(db.String(8), unique=True, nullable=True)
    # unit_number = db.Column(db.String(10), nullable=True)
    # building = db.Column(db.Integer, nullable=True)
    # manage_buildings = db.relationship('Building')
    # bookings = db.relationship('Bookings', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.password}', '{self.id}')"

    # def __init__(name: str, email: str, password: str, phonenumber: str,
    #              license_plate: str, unit_number: str):
    #     if id is not None:

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150), unique=True, nullable=False)
    # manager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text(1000), nullable=True)
    bookings = db.relationship('Bookings')

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=func.now())
    duration = db.Column(db.Integer, nullable=False)
    visitor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # resident_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

""" dummy data for buildings """
buildings = [
    {
        "id": 1,
        "name": "Building 1",
        "address": "Address 1",
        "manager": "Manager 1",
        "description": "Description 1",
        "image": "../static/images/apartment1.jpg",
        "Parking": 1,
    },
    {
        "id": 2,
        "name": "Building 2",
        "address": "Address 2",
        "manager": "Manager 2",
        "description": "Description 2",
        "image": "Image 2",
        "Parking": 2,
    },
    {
        "id": 3,
        "name": "Building 3",
        "address": "Address 3",
        "manager": "Manager 3",
        "description": "Description 3",
        "image": "Image 3",
        "Parking": 3,
    },
    {
        "id": 4,
        "name": "Building 4",
        "address": "Address 4",
        "manager": "Manager 4",
        "description": "Description 4",
        "image": "Image 4",
        "Parking": 4,
    },
    {
        "id": 5,
        "name": "Building 5",
        "address": "Address 5",
        "manager": "Manager 5",
        "description": "Description 5",
        "image": "Image 5",
        "Parking": 5,
    },
    {
        "id": 6,
        "name": "Building 6",
        "address": "Address 6",
        "manager": "Manager 6",
        "description": "Description 6",
        "image": "Image 6",
        "Parking": 6,
    }
    # ,{
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # },
    # {
    #     "id": 5,
    #     "name": "Building 5",
    #     "address": "Address 5",
    #     "manager": "Manager 5",
    #     "description": "Description 5",
    #     "image": "Image 5",
    #     "Parking": 5,
    # }
    ]

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html", buildings=buildings)

""" forms according to flask tutorials """
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #TODO:implement unique email
        # User added to database
        new_user = User(name=form.username.data, email=form.email.data, password=form.password.data)
        
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            print(User.query.all())
        
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        with app.app_context():
            
            # query database
            users = db.session.query(User).filter(User.email.like(form.email.data)).all()
        
        if users is not None and len(users) == 1 and users[0].password == form.password.data:
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", "error")
    return render_template('login.html', title='Login', form=form)

# @app.route("/sign-in", methods=["GET", "POST"])
# def signin():
#     print(request.method)
#     user = ""
#     if request.method == 'POST':
#         email = request.form.get("email")
#         user = email
#         if email == "":
#             flash("Failled to login, invalid email", category="error")
#         else:
#             flash(f"Login successful for {email}!", category="success")
#     return render_template("sign-in.html", username=user , signedIn=False)


# @app.route("/sign-up", methods=["GET", "POST"])
# def signup():
#     print(request.method)
#     user = ""
#     errors = False
#     if request.method == 'POST':
#         email = request.form.get("email")
#         name = request.form.get("name")
#         password1 = request.form.get("password1")
#         password2 = request.form.get("password2")
#         phonenumber = request.form.get("phonenumber")
#         unit_number = request.form.get("unit_number")
#         building = request.form.get("building")

#         if email is None or len(email) < 4:
#             errors = True
#             flash("Email must be greater than 3 characters.", category="error")
#         if name is None or len(name) < 2:
#             errors = True
#             flash("First name must be greater than 1 characters.", category="error")
#         if password1 is None or password2 is None or password1 != password2:
#             errors = True
#             flash("Passwords do not match.", category="error")
#         if password1 is None or len(password1) < 8:
#             errors = True
#             flash("Password must be atleast 8 charcaters.", category="error")
#         if phonenumber != "" and len(phonenumber) < 10:
#             errors = True
#             flash("Phonenumber must be atleast 10 numbers(no spaces or - inbetween numbers).", category="error")
#         if errors == False:
#             flash(f"Sign Pp and Login successful for {email}!", "success")
#             # new_user = User(name=name, password=generate_password_hash(password1, method='sha256'), phonenumber=phonenumber, email=email, unit_number=unit_number, building=building)
#             # login_user(new_user, remember=True)
#             # flash('Account created!', category='success')
#             # db.session.add(new_user)
#             # db.session.commit()

#     return render_template("sign-up.html", username=user , signedIn=False, buildings=["2120 Burnamthorpe street, Mississauga", "2675 Hurontario street, Mississauga", "345 Backside street, Mississauga", "609 Ambush cresent, Mississauga"])


# @app.route("/sign-up")
# def signup():
#     return render_template("sign-up.html")

""" dummy data for guests """
guests = [ {
                "name": "Bobby Fischer", 
                "license": "123456789", 
                "duration": "24", 
                "phone": "416-614-4114", 
                "email": "ruh-roh@goofball.com"
            }, 
            {  
                "name": "Ubuntu", 
                "email": "duh-doh@boofgall.com"
            } 
        ]

@app.route("/buildings-view-visitor")
def buildingsViewVisitor():
    return render_template("buildings-view-visitor.html", buildings=buildings)

@app.route("/buildings-view-manager")
def buildingsViewManager():
    return render_template("buildings-view-manager.html", buildings=buildings)

building = {}

# can't seem to pass in a building via the button in buildings-view-visitors.html or the manager version, need to find a workaround

@app.route(f"/visit-building")
def visitBuilding():
    return render_template("visit-building.html", building = building)

@app.route("/manage-building")
def manageBuilding():
    return render_template("manage-building.html", building=building)

name = "Bobby Fischer"
address = "1234 56th street, Mississauga"
unit = "123"
hasGuest = True

@app.route("/residentView")
def residentView():
    return render_template("resident.html", guests=guests, name=name, address=address, unit=unit, hasGuest=hasGuest)

if __name__ == "__main__":
    
    with app.app_context():
        
        if not path.exists('parkings.db'):
            db.create_all()
            print("making db")
        
    #     # dummy data for users
    #     user_1 = User(name='Bobby',email='th@th.com',password='password')
    #     user_2 = User(name='Jason',email='grind@mind.com',password='password')
    #     db.session.add(user_1)
    #     db.session.add(user_2)
    #     db.session.commit()
    #     User.query.all()
     
    app.run(debug=True)
