from sqlalchemy.sql import func
from main import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phonenumber = db.Column(db.String(12), unique=True, nullable=True)
    license_plate = db.Column(db.String(8), unique=True, nullable=True)
    unit_number = db.Column(db.String(10), nullable=True)
    building = db.relationship('Building')
    bookings = db.relationship('Bookings')


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150), unique=True, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bookings = db.relationship('Bookings')


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=func.now())
    duration = db.Column(db.Integer, nullable=False)
    visitor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resident_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
