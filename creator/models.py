#!/usr/bin/python3
"""
This module contains the classes for the creator program.
"""
#from characters.utils import roll_stats
from creator import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #characters = db.relationship('Character', backref='Player', lazy=True)


# class Character(db.Model):
#     id = db.Column(db.String(8), primary_key=True, default=str(uuid.uuid4)[:8])
#     name = db.Column(db.String(30), nullable=False)
#     starting_stats = db.Column(db.ARRAY, nullable=False, default=roll_stats())
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     strength = db.Column(db.Integer, nullable=False)
#     dexterity = db.Column(db.Integer, nullable=False)
#     constitution = db.Column(db.Integer, nullable=False)
#     intelligence = db.Column(db.Integer, nullable=False)
#     wisdom = db.Column(db.Integer, nullable=False)
#     charisma = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
