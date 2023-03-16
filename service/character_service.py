from model.attribute import Attributes
from model.calculated_attribute import CalculatedAttributes
from model.character import Character


def create_character(name, attack, defense, level, attributes, race_name, class_name, race_data, class_data, experience,
                     health=None, stamina=None, mana=None):
    race = race_data[race_name]
    character_class = class_data[class_name]

    # Apply race attribute bonuses
    adjusted_attributes = apply_race_attribute_bonuses(attributes, race)

    # Calculate max values based on attributes
    max_health = calculate_max_health(attributes)
    max_stamina = calculate_max_stamina(attributes)
    max_mana = calculate_max_mana(attributes)

    # Set health to max_health if not provided
    if health is None:
        health = max_health

    if stamina is None:
        stamina = max_stamina

    if mana is None:
        mana = max_mana

    # Ensure the character's health doesn't exceed max_health
    health = min(health, max_health)
    stamina = min(stamina, max_stamina)
    mana = min(mana, max_mana)

    # Calculate derived attributes
    initiative = calculate_initiative(adjusted_attributes)
    status_resistence = calculate_status_resistence(adjusted_attributes)
    magic_resistence = calculate_magic_resistence(adjusted_attributes)
    physical_resistence = calculate_physical_resistence(adjusted_attributes)
    magic_power = calculate_magic_power(adjusted_attributes)
    physical_power = calculate_physical_power(adjusted_attributes)

    calculated_attrs = CalculatedAttributes(initiative, status_resistence,
                                            magic_resistence, physical_resistence, magic_power,
                                            physical_power)

    character = Character(name, health, max_health, stamina, max_stamina, mana, max_mana, attack, defense, level,
                          adjusted_attributes, calculated_attrs, race, character_class, experience)

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
    character.stamina += 5
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


def calculate_initiative(attributes):
    return (attributes.dexterity + attributes.intelligence) / 2


def calculate_max_mana(attributes):
    return attributes.intelligence + (attributes.dexterity * 2)


def calculate_max_stamina(attributes):
    return attributes.strength + (attributes.dexterity * 2)


def calculate_max_health(attributes):
    return attributes.strength * 10 + 25


def calculate_status_resistence(attributes):
    return (attributes.dexterity + attributes.intelligence + attributes.strength) / 3


def calculate_magic_resistence(attributes):
    return (attributes.dexterity + attributes.intelligence) / 2


def calculate_physical_resistence(attributes):
    return (attributes.dexterity + attributes.strength) / 2


def calculate_magic_power(attributes):
    return (attributes.dexterity + attributes.intelligence) * 2


def calculate_physical_power(attributes):
    return (attributes.dexterity + attributes.strength) * 2


def character_str(character):
    attribute_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in character.attributes.__dict__.items()])
    abilities_str = ", ".join(character.character_class.abilities)

    return (
        f"Name: {character.name}\n"
        f"Class: {character.character_class.name}\n"
        f"Race: {character.race.name}\n"
        f"Level: {character.level}\n"
        f"Current Health: {character.health}/{character.max_health}\n"
        f"Current stamina: {character.stamina}/{character.max_stamina}\n"
        f"Attack: {character.attack}\n"
        f"Defense: {character.defense}\n"
        f"Attributes:\n{attribute_str}\n"
        f"Abilities: {abilities_str}\n"
        f"Experience: {character.experience}"
    )

# Add more functions for character operations as needed
