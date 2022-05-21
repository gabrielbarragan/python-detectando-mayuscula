from typing import Dict
def find_upper(person: dict, person2: dict):
    """"""


    new_dict={}

    if person['last_name']== person['last_name'].capitalize():
        new_dict[person['last_name'][0]]= person['last_name']

    if person2['last_name']== person2['last_name'].capitalize():
        new_dict[person2['last_name'][0]]= person2['last_name']

    return new_dict