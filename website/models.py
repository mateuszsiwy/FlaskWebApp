from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

# User inherits from db.model and UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note') # when referencing relationship, use Upper case, when initializing the foreign key, use lower

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func.now gets the current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # in Python its User, but sql interprets it as user

