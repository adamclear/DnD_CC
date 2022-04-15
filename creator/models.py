#!/usr/bin/python3
"""
This module contains the classes for the creator program.
"""
#from characters.utils import roll_stats
from creator import db, login_manager
from datetime import datetime
from flask_login import UserMixin
import random

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.String(8), primary_key=True, autoincrement=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    characters = db.relationship('Character', backref='player', lazy=True)


class Character(db.Model):
    id = db.Column(db.String(8), primary_key=True, autoincrement=False)
    name = db.Column(db.String(30), nullable=False)
    stat1 = db.Column(db.Integer, nullable=False)
    stat2 = db.Column(db.Integer, nullable=False)
    stat3 = db.Column(db.Integer, nullable=False)
    stat4 = db.Column(db.Integer, nullable=False)
    stat5 = db.Column(db.Integer, nullable=False)
    stat6 = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    ancestry = db.Column(db.String(20), nullable=False)
    heroic_class = db.Column(db.String(20), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=1)
    hp1 = db.Column(db.Integer, nullable=False, default=0)
    hp2 = db.Column(db.Integer, nullable=False, default=0)
    hp3 = db.Column(db.Integer, nullable=False, default=0)
    hp4 = db.Column(db.Integer, nullable=False, default=0)
    hp5 = db.Column(db.Integer, nullable=False, default=0)
    hp6 = db.Column(db.Integer, nullable=False, default=0)
    hp7 = db.Column(db.Integer, nullable=False, default=0)
    hp8 = db.Column(db.Integer, nullable=False, default=0)
    hp9 = db.Column(db.Integer, nullable=False, default=0)
    hp10 = db.Column(db.Integer, nullable=False, default=0)
    hp11 = db.Column(db.Integer, nullable=False, default=0)
    hp12 = db.Column(db.Integer, nullable=False, default=0)
    hp13 = db.Column(db.Integer, nullable=False, default=0)
    hp14 = db.Column(db.Integer, nullable=False, default=0)
    hp15 = db.Column(db.Integer, nullable=False, default=0)
    hp16 = db.Column(db.Integer, nullable=False, default=0)
    hp17 = db.Column(db.Integer, nullable=False, default=0)
    hp18 = db.Column(db.Integer, nullable=False, default=0)
    hp19 = db.Column(db.Integer, nullable=False, default=0)
    hp20 = db.Column(db.Integer, nullable=False, default=0)
    weapon = db.Column(db.String(20))
    armor = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.name} - Level {self.level} {self.heroic_class} - ID: {self.id}"

    def roll_hp(self):
        hp_die_table = {
            'Rogue': 6,
            'Fighter': 10,
            'Barbarian': 12
        }
        die_size = hp_die_table[self.heroic_class]
        roll = 0
        while roll <= 1:
            roll = random.randint(1, die_size)
        return roll

    def calc_hp(self):
        hp_rolls = [
            self.hp1,
            self.hp2,
            self.hp3,
            self.hp4,
            self.hp5,
            self.hp6,
            self.hp7,
            self.hp8,
            self.hp9,
            self.hp10,
            self.hp11,
            self.hp12,
            self.hp13,
            self.hp14,
            self.hp15,
            self.hp16,
            self.hp17,
            self.hp18,
            self.hp19,
            self.hp20
        ]
        sub_total = sum(hp_rolls)
        modifier = self.calc_mod(self.constitution)
        total = sub_total + (modifier * self.level)
        return total

    def calc_mod(self, number):
        diff = number - 10
        if diff > 1:
            modifier = diff / 2
        elif diff < -1:
            diff = diff * -1
            modifier = (diff / 2) * -1
        else:
            modifier = 0
        return int(modifier)

    def calc_ac(self):
        dex_mod = self.calc_mod(self.dexterity)
        if self.armor == 'Leather':
            ac = 11 + dex_mod
        elif self.armor == 'Hide':
            if dex_mod >= 2:
                ac = 12 + 2
            else:
                ac = 12 + dex_mod
        elif self.armor == 'Plate':
            ac = 18
        return ac
