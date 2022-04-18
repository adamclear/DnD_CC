#!/usr/bin/python3
"""
This module contains the classes for the creator program.
"""
from creator import db, login_manager
from datetime import datetime
from flask_login import UserMixin
import json
import random
import requests

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
    name = db.Column(db.String(30))
    stat1 = db.Column(db.Integer)
    stat2 = db.Column(db.Integer)
    stat3 = db.Column(db.Integer)
    stat4 = db.Column(db.Integer)
    stat5 = db.Column(db.Integer)
    stat6 = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    ancestry = db.Column(db.String(20), nullable=False)
    heroic_class = db.Column(db.String(20), nullable=False)
    subclass = db.Column(db.String(20))
    pact_boon = db.Column(db.String(20))
    level = db.Column(db.Integer, nullable=False, default=1)
    hp1 = db.Column(db.Integer)
    hp2 = db.Column(db.Integer)
    hp3 = db.Column(db.Integer)
    hp4 = db.Column(db.Integer)
    hp5 = db.Column(db.Integer)
    hp6 = db.Column(db.Integer)
    hp7 = db.Column(db.Integer)
    hp8 = db.Column(db.Integer)
    hp9 = db.Column(db.Integer)
    hp10 = db.Column(db.Integer)
    hp11 = db.Column(db.Integer)
    hp12 = db.Column(db.Integer)
    hp13 = db.Column(db.Integer)
    hp14 = db.Column(db.Integer)
    hp15 = db.Column(db.Integer)
    hp16 = db.Column(db.Integer)
    hp17 = db.Column(db.Integer)
    hp18 = db.Column(db.Integer)
    hp19 = db.Column(db.Integer)
    hp20 = db.Column(db.Integer)
    weapon = db.Column(db.String(20))
    armor = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.name} - Level {self.level} {self.heroic_class} - ID: {self.id}"

    def roll_hp(self):
        hp_die_table = {
            'Barbarian': 12,
            'Bard': 8,
            'Cleric': 8,
            'Druid': 8,
            'Fighter': 10,
            'Monk': 8,
            'Paladin': 10,
            'Ranger': 10,
            'Rogue': 6,
            'Sorcerer': 6,
            'Warlock': 8,
            'Wizard': 6
        }
        die_size = hp_die_table[self.heroic_class]
        roll = 0
        if self.level == 1:
            roll = die_size
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
        sub_total = 0
        for x in hp_rolls:
            if x != None:
                sub_total += x
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
        if self.armor == 'Unarmored':
            armor_value = 10
        else:
            armor_request = requests.get('https://www.dnd5eapi.co/api/equipment/' + self.armor.lower())
            armor_json = json.loads(armor_request.text)
            armor_value = int(armor_json['armor_class']['base'])
            max_bonus = None
            if armor_json['armor_class']['dex_bonus'] is True:
                for x in armor_json['armor_class']:
                    if x == 'max_bonus':
                        max_bonus = 2
                if max_bonus is None:
                    max_bonus = dex_mod
            if armor_json['armor_class']['dex_bonus'] is False:
                max_bonus = 0
            if dex_mod > max_bonus:
                dex_mod = max_bonus
        return armor_value + dex_mod

    def calc_prof(self):
        prof_bonus = int(self.level / 4) + 2
        return prof_bonus
