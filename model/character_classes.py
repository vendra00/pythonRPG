"""
This module contains data for various character classes in a game.

Attributes:
barbarian_modifiers (dict): A dictionary containing the attribute modifiers for the Barbarian class.
barbarian_abilities (list): A list of abilities for the Barbarian class.
bard_modifiers (dict): A dictionary containing the attribute modifiers for the Bard class.
bard_abilities (list): A list of abilities for the Bard class.
cleric_modifiers (dict): A dictionary containing the attribute modifiers for the Cleric class.
cleric_abilities (list): A list of abilities for the Cleric class.
druid_modifiers (dict): A dictionary containing the attribute modifiers for the Druid class.
druid_abilities (list): A list of abilities for the Druid class.
fighter_modifiers (dict): A dictionary containing the attribute modifiers for the Fighter class.
fighter_abilities (list): A list of abilities for the Fighter class.
monk_modifiers (dict): A dictionary containing the attribute modifiers for the Monk class.
monk_abilities (list): A list of abilities for the Monk class.
paladin_modifiers (dict): A dictionary containing the attribute modifiers for the Paladin class.
paladin_abilities (list): A list of abilities for the Paladin class.
ranger_modifiers (dict): A dictionary containing the attribute modifiers for the Ranger class.
ranger_abilities (list): A list of abilities for the Ranger class.
rogue_modifiers (dict): A dictionary containing the attribute modifiers for the Rogue class.
rogue_abilities (list): A list of abilities for the Rogue class.
sorcerer_modifiers (dict): A dictionary containing the attribute modifiers for the Sorcerer class.
sorcerer_abilities (list): A list of abilities for the Sorcerer class.
warlock_modifiers (dict): A dictionary containing the attribute modifiers for the Warlock class.
warlock_abilities (list): A list of abilities for the Warlock class.
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
bard_abilities = [ability_pool.bard["Vicious Mockery"]["title"],
                  ability_pool.bard["Cutting Words"]["title"],
                  ability_pool.bard["Bardic Inspiration"]["title"],
                  ability_pool.bard["Countercharm"]["title"],
                  ability_pool.bard["Magical Secrets"]["title"],
                  ability_pool.bard["Song of Rest"]["title"],
                  ability_pool.bard["Expertise"]["title"],
                  ability_pool.bard["College of Lore"]["title"],
                  ability_pool.bard["Counter Spell"]["title"],
                  ability_pool.bard["Dissonant Whispers"]["title"]]

cleric_modifiers = {
    "intelligence": 3,
    "dexterity": 1,
    "strength": 1
}
cleric_abilities = [ability_pool.cleric["Turn Undead"]["title"],
                    ability_pool.cleric["Healing Word"]["title"],
                    ability_pool.cleric["Spiritual Weapon"]["title"],
                    ability_pool.cleric["Bless"]["title"],
                    ability_pool.cleric["Shield of Faith"]["title"],
                    ability_pool.cleric["Cure Wounds"]["title"],
                    ability_pool.cleric["Divine Favor"]["title"],
                    ability_pool.cleric["Sacred Flame"]["title"],
                    ability_pool.cleric["Prayer of Healing"]["title"],
                    ability_pool.cleric["Guiding Bolt"]["title"]]

druid_modifiers = {
    "intelligence": 3,
    "dexterity": 3,
    "strength": -3
}
druid_abilities = [ability_pool.druid["Wild Shape"]["title"],
                   ability_pool.druid["Moonbeam"]["title"],
                   ability_pool.druid["Entangle"]["title"],
                   ability_pool.druid["Flame Blade"]["title"],
                   ability_pool.druid["Speak with Animals"]["title"],
                   ability_pool.druid["Thunderwave"]["title"],
                   ability_pool.druid["Giant Insect"]["title"],
                   ability_pool.druid["Goodberry"]["title"],
                   ability_pool.druid["Call Lightning"]["title"],
                   ability_pool.druid["Pass Without Trace"]["title"]]

fighter_modifiers = {
    "intelligence": -2,
    "dexterity": 2,
    "strength": 2
}

fighter_abilities = [ability_pool.fighter["Second Wind"]["title"],
                     ability_pool.fighter["Action Surge"]["title"],
                     ability_pool.fighter["Indomitable"]["title"],
                     ability_pool.fighter["Extra Attack"]["title"],
                     ability_pool.fighter["Martial Archetype"]["title"],
                     ability_pool.fighter["Combat Superiority"]["title"],
                     ability_pool.fighter["Defensive Duelist"]["title"],
                     ability_pool.fighter["Rally"]["title"],
                     ability_pool.fighter["Riposte"]["title"],
                     ability_pool.fighter["Whirlwind Attack"]["title"]]

monk_modifiers = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": 1
}
monk_abilities = [ability_pool.monk["Flurry of Blows"]["title"],
                  ability_pool.monk["Patient Defense"]["title"],
                  ability_pool.monk["Step of the Wind"]["title"],
                  ability_pool.monk["Stunning Strike"]["title"],
                  ability_pool.monk["Deflect Missiles"]["title"],
                  ability_pool.monk["Ki-Empowered Strikes"]["title"],
                  ability_pool.monk["Slow Fall"]["title"],
                  ability_pool.monk["Unarmored Movement"]["title"],
                  ability_pool.monk["Defensive Duelist"]["title"],
                  ability_pool.monk["Evasion"]["title"]]

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
ranger_abilities = [ability_pool.ranger["Favored Enemy"]["title"],
                    ability_pool.ranger["Natural Explorer"]["title"],
                    ability_pool.ranger["Hunter's Mark"]["title"],
                    ability_pool.ranger["Colossus Slayer"]["title"],
                    ability_pool.ranger["Multiattack"]["title"],
                    ability_pool.ranger["Hide in Plain Sight"]["title"],
                    ability_pool.ranger["Whirlwind Attack"]["title"],
                    ability_pool.ranger["Escape the Horde"]["title"],
                    ability_pool.ranger["Volley"]["title"],
                    ability_pool.ranger["Evasion"]["title"]]

rogue_modifiers = {
    "intelligence": 1,
    "dexterity": 4,
    "strength": -2
}
rogue_abilities = [ability_pool.rogue["Sneak Attack"]["title"],
                   ability_pool.rogue["Cunning Action"]["title"],
                   ability_pool.rogue["Uncanny Dodge"]["title"],
                   ability_pool.rogue["Evasion"]["title"],
                   ability_pool.rogue["Thieves' Cant"]["title"],
                   ability_pool.rogue["Sneak Thief"]["title"],
                   ability_pool.rogue["Criminal Contact"]["title"],
                   ability_pool.rogue["Fast Hands"]["title"],
                   ability_pool.rogue["Stroke of Luck"]["title"],
                   ability_pool.rogue["Expertise"]["title"]]

sorcerer_modifiers = {
    "intelligence": 4,
    "dexterity": 2,
    "strength": 2
}
sorcerer_abilities = [ability_pool.sorcerer["Chaos Bolt"]["title"],
                      ability_pool.sorcerer["Charm Person"]["title"],
                      ability_pool.sorcerer["Fireball"]["title"],
                      ability_pool.sorcerer["Magic Missile"]["title"],
                      ability_pool.sorcerer["Thunderwave"]["title"],
                      ability_pool.sorcerer["Fly"]["title"],
                      ability_pool.sorcerer["Invisibility"]["title"],
                      ability_pool.sorcerer["Mage Armor"]["title"],
                      ability_pool.sorcerer["Ray of Frost"]["title"],
                      ability_pool.sorcerer["Shield"]["title"]]

warlock_modifiers = {
    "intelligence": 3,
    "dexterity": 2,
    "strength": 3
}
warlock_abilities = [ability_pool.warlock["Eldritch Blast"]["title"],
                     ability_pool.warlock["Hex"]["title"],
                     ability_pool.warlock["Darkness"]["title"],
                     ability_pool.warlock["Hellish Rebuke"]["title"],
                     ability_pool.warlock["Armor of Agathys"]["title"],
                     ability_pool.warlock["Misty Step"]["title"],
                     ability_pool.warlock["Shadow Blade"]["title"],
                     ability_pool.warlock["Devil's Sight"]["title"],
                     ability_pool.warlock["Summon Lesser Demons"]["title"],
                     ability_pool.warlock["Charm Person"]["title"]]

wizard_modifiers = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": -2
}
wizard_abilities = [ability_pool.wizard["Magic Missile"]["title"],
                    ability_pool.wizard["Fireball"]["title"],
                    ability_pool.wizard["Shield"]["title"],
                    ability_pool.wizard["Mage Armor"]["title"],
                    ability_pool.wizard["Thunderwave"]["title"],
                    ability_pool.wizard["Mage Hand"]["title"],
                    ability_pool.wizard["Charm Person"]["title"],
                    ability_pool.wizard["Identify"]["title"],
                    ability_pool.wizard["Sleep"]["title"],
                    ability_pool.wizard["Levitate"]["title"]]

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
