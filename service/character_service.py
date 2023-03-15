from model.attribute import Attributes
from model.character import Character


def create_character(name, attack, defense, level, attributes, race_name, class_name, race_data, class_data, experience,
                     health=None):
    race = race_data[race_name]
    character_class = class_data[class_name]

    # Apply race attribute bonuses
    adjusted_attributes = apply_race_attribute_bonuses(attributes, race)

    # Calculate max_health based on Strength
    max_health = adjusted_attributes.strength * 10 + 25

    # Set health to max_health if not provided
    if health is None:
        health = max_health

    # Ensure the character's health doesn't exceed max_health
    health = min(health, max_health)

    character = Character(name, health, max_health, attack, defense, level, adjusted_attributes, race, character_class, experience)
    return character


def apply_race_attribute_bonuses(attributes, race):
    adjusted_attributes = Attributes(
        intelligence=attributes.intelligence + race.attribute_bonuses["intelligence"],
        dexterity=attributes.dexterity + race.attribute_bonuses["dexterity"],
        strength=attributes.strength + race.attribute_bonuses["strength"],
    )
    return adjusted_attributes


def attack_enemy(attacker, defender):
    damage_dealt = max(0, attacker.attack - defender.defense)
    take_damage(defender, damage_dealt)  # Use the take_damage function instead of the method
    print(f"{attacker.name} attacks {defender.name} for {damage_dealt} damage!")


def level_up(character):
    character.level += 1
    character.health += 10
    character.attack += 2
    character.defense += 2
    print(f"{character.name} has leveled up to level {character.level}!")


def take_damage(character, damage):
    character.health -= damage


def is_alive(character):
    return character.health > 0


def award_experience(character, experience_points):
    character.experience += experience_points
    print(f"{character.name} gained {experience_points} experience points!")


def character_str(character):
    attribute_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in character.attributes.__dict__.items()])
    abilities_str = ", ".join(character.character_class.abilities)

    return (
        f"Name: {character.name}\n"
        f"Class: {character.character_class.name}\n"
        f"Race: {character.race.name}\n"
        f"Level: {character.level}\n"
        f"Current Health: {character.health}/{character.max_health}\n"
        f"Attack: {character.attack}\n"
        f"Defense: {character.defense}\n"
        f"Attributes:\n{attribute_str}\n"
        f"Abilities: {abilities_str}\n"
        f"Experience: {character.experience}"
    )

# Add more functions for character operations as needed
