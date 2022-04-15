from creator.models import Character
import json
import random
import requests

def roll_stats():
    """
    This method uses dice rolls to generate ability scores.
    """
    Stat_array = []
    for x in range(6):
        total = 0
        Dielist = [0, 0, 0, 0]
        for item in range(len(Dielist)):
            roll = 0
            while roll <= 1:
                roll = random.randint(1, 6)
            Dielist[item] = roll
        Dielist.sort(reverse=True)
        Dielist.pop(3)
        for result in Dielist:
            total = total + result
        Stat_array.append(total)
    return Stat_array

def get_class_features(character_id):
    character = Character.query.get(character_id)
    char_class = character.heroic_class.lower()
    response = requests.get('https://www.dnd5eapi.co/api/classes/' + char_class + '/levels')
    json_feat = json.loads(response.text)
    api_list = []
    feat_dict = {}
    for x in range(character.level):
        for k, v in json_feat[x].items():
            if k == 'features':
                for element in v:
                    for key, value in element.items():
                        if key == 'url':
                            api_list.append(value)
    for x in api_list:
        feat_resp = requests.get('https://www.dnd5eapi.co' + x)
        feat_json = json.loads(feat_resp.text)
        feat_dict[feat_json['name']] = feat_json['desc']
    return feat_dict

def get_char_traits(character_id):
    character = Character.query.get(character_id)
    char_ancestry = character.ancestry.lower()
    response = requests.get('https://www.dnd5eapi.co/api/races/' + char_ancestry)
    json_traits = json.loads(response.text)
    api_list = []
    trait_dict = {}
    for k, v in json_traits.items():
        if k == 'traits':
            for element in v:
                for key, value in element.items():
                    if key == 'url':
                        api_list.append(value)
    for x in api_list:
        trait_resp = requests.get('https://www.dnd5eapi.co' + x)
        trait_json = json.loads(trait_resp.text)
        trait_dict[trait_json['name']] = trait_json['desc']
    return trait_dict
