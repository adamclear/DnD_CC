#!/usr/bin/python3
"""
This module contains the classes for the creator program.
"""
#from characters.utils import roll_stats
from creator import db, login_manager
from datetime import datetime
from flask_login import UserMixin
import uuid


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


# class Character():
#     """
#     This class is the basis for each character object.
#     """
#     def __init__(self, name):
#         """
#         Initialization method.
#         """
#         # Generating basic info #
#         name = name
#         id = str(uuid.uuid4())[:8]
#         created_at = datetime.now
#         starting_stats = roll_stats()
