#!/usr/bin/python3
"""
This module contains the classes for the creator program.
"""
from characters.utils import roll_stats
from creator import db, login_manager
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
import uuid

class User(db.Model, UserMixin):
    id = db.Column(db.String(8), primary_key=True)

class Character():
    """
    This class is the basis for each character object.
    """
    def __init__(self, name):
        """
        Initialization method.
        """
        # Generating basic info #
        name = name
        id = str(uuid.uuid4())[:8]
        created_at = datetime.now
        starting_stats = roll_stats()
