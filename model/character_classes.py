"""
A module containing the data for various character classes in a game.

Each character class has a set of attribute modifiers and abilities.
Character classes can be added or modified as needed.

Attributes:
    wizard_modifiers (dict): A dictionary containing the attribute modifiers for the Wizard class.
    wizard_abilities (list): A list of abilities for the Wizard class.
    class_data (dict): A dictionary containing CharacterClass instances for each class in the game.
"""
from model import ability_pool
from model.character_class import CharacterClass


barbarian_modifiers = {
    "intelligence": -2,
    "dexterity": 1,
    "strength": 3
}
barbarian_abilities = [ability_pool.barbarian["Reckless Attack"]["title"],
                       ability_pool.barbarian["Frenzy"]["title"],
                       ability_pool.barbarian["Brutal Critical"]["title"],
                       ability_pool.barbarian["Mindless Rage"]["title"],
                       ability_pool.barbarian["Intimidating Presence"]["title"],
                       ability_pool.barbarian["Danger Sense"]["title"],
                       ability_pool.barbarian["Fast Movement"]["title"],
                       ability_pool.barbarian["Rage Beyond Death"]["title"],
                       ability_pool.barbarian["Retaliation"]["title"],
                       ability_pool.barbarian["Spirit Shield"]["title"]]

bard_modifiers = {
    "intelligence": 1,
    "dexterity": 2,
    "strength": -2
}
bard_abilities = []

cleric_modifiers = {
    "intelligence": 3,
    "dexterity": 1,
    "strength": 1
}
cleric_abilities = []

druid_modifiers = {
    "intelligence": 3,
    "dexterity": 3,
    "strength": -3
}
druid_abilities = []

fighter_modifiers = {
    "intelligence": -2,
    "dexterity": 2,
    "strength": 2
}
fighter_abilities = ["Action Surge", "Second Wind", "Indomitable", "Extra Attack", "Great Weapon Fighting",
                     "Precision Attack", "Sweeping Attack", "Riposte", "Trip Attack", "Disarming Attack"]

monk_modifiers = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": 1
}
monk_abilities = []

paladin_modifiers = {
    "intelligence": 3,
    "dexterity": 2,
    "strength": 2
}
paladin_abilities = ["Lay on Hands", "Divine Smite", "Aura of Protection", "Cleansing Touch", "Aura of Courage",
                     "Branding Smite", "Crusader's Mantle", "Searing Smite", "Aura of Life", "AFind Steed"]

ranger_modifiers = {
    "intelligence": 0,
    "dexterity": 3,
    "strength": 1
}
ranger_abilities = []

rogue_modifiers = {
    "intelligence": 1,
    "dexterity": 4,
    "strength": -2
}
rogue_abilities = ["Sneak Attack", "Cunning Action", "Evasion ", "Uncanny Dodge", "Expertise", "Thieves' Cant",
                   "Reliable Talent", "Assassinate", "Fast Hands", "Stroke of Luck"]

sorcerer_modifiers = {
    "intelligence": 4,
    "dexterity": 2,
    "strength": 2
}
sorcerer_abilities = []

warlock_modifiers = {
    "intelligence": 3,
    "dexterity": 2,
    "strength": 3
}
warlock_abilities = []

wizard_modifiers = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": -2
}
wizard_abilities = ["Fireball", "Mage Armor", "Magic Missile", "Detect Magic", "Shield", "Sleep", "Identify",
                    "Charm Person", "Counterspell", "Wall of Force"]

# Add more character classes as needed

class_data = {
    "Barbarian": CharacterClass("Barbarian", barbarian_modifiers, barbarian_abilities),
    "Bard": CharacterClass("Bard", bard_modifiers, bard_abilities),
    "Cleric": CharacterClass("Cleric", cleric_modifiers, cleric_abilities),
    "Druid": CharacterClass("Druid", druid_modifiers, druid_abilities),
    "Fighter": CharacterClass("Fighter", fighter_modifiers, fighter_abilities),
    "Monk": CharacterClass("Monk", monk_modifiers, monk_abilities),
    "Paladin": CharacterClass("Paladin", paladin_modifiers, paladin_abilities),
    "Ranger": CharacterClass("Ranger", ranger_modifiers, ranger_abilities),
    "Rogue": CharacterClass("Rogue", rogue_modifiers, rogue_abilities),
    "Sorcerer": CharacterClass("Sorcerer", sorcerer_modifiers, sorcerer_abilities),
    "Warlock": CharacterClass("Warlock", warlock_modifiers, warlock_abilities),
    "Wizard": CharacterClass("Wizard", wizard_modifiers, wizard_abilities),
    # Add more character classes as needed
}
