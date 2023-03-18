"""
A module containing the data for various races in a game.

Each race has a set of attribute bonuses.
Races can be added or modified as needed.

Attributes:
    elf_attribute_bonuses (dict): A dictionary containing the attribute bonuses for the Elf race.
    human_attribute_bonuses (dict): A dictionary containing the attribute bonuses for the Human race.
    orc_attribute_bonuses (dict): A dictionary containing the attribute bonuses for the Orc race.
    dwarf_attribute_bonuses (dict): A dictionary containing the attribute bonuses for the Dwarf race.
    race_data (dict): A dictionary containing Race instances for each race in the game.
"""
from model.race import Race

elf_attribute_bonuses = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": -1
}

human_attribute_bonuses = {
    "intelligence": 1,
    "dexterity": 1,
    "strength": 1
}

orc_attribute_bonuses = {
    "intelligence": -6,
    "dexterity": 2,
    "strength": 3
}

dwarf_attribute_bonuses = {
    "intelligence": -2,
    "dexterity": -2,
    "strength": 3
}

# Add more races as needed


race_data = {
    "Elf": Race("Elf", elf_attribute_bonuses),
    "Human": Race("Human", human_attribute_bonuses),
    "Orc": Race("Orc", orc_attribute_bonuses),
    "Dwarf": Race("Dwarf", dwarf_attribute_bonuses),
}
