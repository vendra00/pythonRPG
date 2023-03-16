from typing import Tuple, Optional

from model.character_class import CharacterClass
from model.race import Race
from model.attribute import Attributes
from model.calculated_attribute import CalculatedAttributes
from model.character import Character


def create_character(name, attack, defense, level, attributes, race_name, class_name, race_data, class_data, experience,
                     health=None, stamina=None, mana=None):
    # Set character bio
    character_class, race = set_character_bio(class_data, class_name, race_data, race_name)

    # Apply race attribute bonuses
    adjusted_attributes = apply_race_attribute_bonuses(attributes, race)

    # Calculate max values based on attributes
    max_health, max_mana, max_stamina = calculate_max_values(attributes)

    # Set mana, health, stamina max values if not provided
    health, mana, stamina = set_max_values(health, mana, max_health, max_mana, max_stamina, stamina)

    # Ensure the character's health doesn't exceed max_health
    health, mana, stamina = check_max_values(health, mana, max_health, max_mana, max_stamina, stamina)

    # Calculate derived attributes
    character = calculate_derived_attributes(adjusted_attributes, attack, character_class, defense, experience, health,
                                             level, mana, max_health, max_mana, max_stamina, name, race, stamina)

    return character


def set_character_bio(class_data: dict, class_name: str, race_data: dict,
                      race_name: str) -> Tuple[CharacterClass, Race]:
    """
    Set the character's race and class based on the given data and names.

    :param class_data: A dictionary containing the character's class data.
    :param class_name: The name of the character's class.
    :param race_data: A dictionary containing the character's race data.
    :param race_name: The name of the character's race.
    :return: A tuple containing the character's class and race data.
    """
    race = race_data[race_name]
    character_class = class_data[class_name]
    return character_class, race


def check_max_values(health: int, mana: int, max_health: int,
                     max_mana: int, max_stamina: int, stamina: int) -> Tuple[int, int, int]:
    """
    Ensure the character's health, stamina, and mana values do not exceed their respective maximums.

    :param health: The character's current health.
    :param mana: The character's current mana.
    :param max_health: The character's maximum health.
    :param max_mana: The character's maximum mana.
    :param max_stamina: The character's maximum stamina.
    :param stamina: The character's current stamina.
    :return: A tuple containing the clamped health, mana, and stamina values.
    """
    health = min(health, max_health)
    stamina = min(stamina, max_stamina)
    mana = min(mana, max_mana)
    return health, mana, stamina


def calculate_derived_attributes(adjusted_attributes: Attributes, attack: int, character_class: CharacterClass,
                                 defense: int, experience: int, health: int, level: int, mana: int,
                                 max_health: int, max_mana: int, max_stamina: int, name: str, race: Race,
                                 stamina: int) -> Character:
    """
    Calculate the derived attributes of a character and create a new Character instance with the calculated values.

    :param adjusted_attributes: The character's adjusted attributes after race bonuses are applied.
    :param attack: The character's base attack value.
    :param character_class: The character's class as an instance of the CharacterClass class.
    :param defense: The character's base defense value.
    :param experience: The character's experience points.
    :param health: The character's current health.
    :param level: The character's level.
    :param mana: The character's current mana.
    :param max_health: The character's maximum health.
    :param max_mana: The character's maximum mana.
    :param max_stamina: The character's maximum stamina.
    :param name: The character's name.
    :param race: The character's race as an instance of the Race class.
    :param stamina: The character's current stamina.
    :return: A new Character instance with the calculated derived attributes.
    """
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


def calculate_max_values(attributes: Attributes) -> Tuple[int, int, int]:
    """
    Calculate the max health, max mana, and max stamina values for a character based on their attributes.

    :param attributes: The character's attributes as an instance of the Attributes class.
    :return: A tuple containing the max health, max mana, and max stamina values.
    """
    max_health = calculate_max_health(attributes)
    max_stamina = calculate_max_stamina(attributes)
    max_mana = calculate_max_mana(attributes)
    return max_health, max_mana, max_stamina


def set_max_values(health: Optional[int], mana: Optional[int], max_health: int, max_mana: int,
                   max_stamina: int, stamina: Optional[int]) -> Tuple[int, int, int]:
    """
    Set the character's health, stamina, and mana to their maximum values if not provided.

    :param health: The character's current health value, or None if not provided.
    :param mana: The character's current mana value, or None if not provided.
    :param max_health: The character's maximum health value.
    :param max_mana: The character's maximum mana value.
    :param max_stamina: The character's maximum stamina value.
    :param stamina: The character's current stamina value, or None if not provided.
    :return: A tuple containing the character's health, mana, and stamina values.
    """
    if health is None:
        health = max_health
    if stamina is None:
        stamina = max_stamina
    if mana is None:
        mana = max_mana
    return health, mana, stamina


def apply_race_attribute_bonuses(attributes: Attributes, race: Race) -> Attributes:
    """
    Apply the attribute bonuses from the character's race to their base attributes.

    :param attributes: The character's base attributes as an instance of the Attributes class.
    :param race: The character's race as an instance of the Race class.
    :return: A new instance of the Attributes class with the adjusted attributes.
    """
    adjusted_attributes = Attributes(
        intelligence=attributes.intelligence + race.attribute_bonuses["intelligence"],
        dexterity=attributes.dexterity + race.attribute_bonuses["dexterity"],
        strength=attributes.strength + race.attribute_bonuses["strength"],
    )
    return adjusted_attributes


def attack_enemy(attacker: Character, defender: Character) -> None:
    """
    Calculate the damage dealt by the attacker to the defender, apply the damage, and print the result.

    :param attacker: The attacking Character instance.
    :param defender: The defending Character instance.
    """
    damage_dealt = max(0, attacker.attack - defender.defense)
    take_damage(defender, damage_dealt)  # Use the take_damage function instead of the method
    print(f"{attacker.name} attacks {defender.name} for {damage_dealt} damage!")


def level_up(character: Character) -> None:
    """
    Increase the character's level and update the associated attributes.

    :param character: The Character instance to level up.
    """
    character.level += 1
    character.health += 10
    character.stamina += 5
    character.attack += 2
    character.defense += 2
    print(f"{character.name} has leveled up to level {character.level}!")


def take_damage(character: Character, damage: int) -> None:
    """
    Inflict damage to a character, reducing their health.

    :param character: The Character instance to take damage.
    :param damage: The amount of damage to be inflicted.
    """
    character.health -= damage


def is_alive(character: Character) -> bool:
    """
    Check if a character is alive based on their health.

    :param character: The Character instance to check.
    :return: True if the character's health is greater than 0, False otherwise.
    """
    return character.health > 0


def award_experience(character: Character, experience_points: int) -> None:
    """
    Award experience points to a character and display a message.

    :param character: The Character instance to award experience points to.
    :param experience_points: The number of experience points to award.
    """
    character.experience += experience_points
    print(f"{character.name} gained {experience_points} experience points!")


def calculate_initiative(attributes: Attributes) -> float:
    """
    Calculate the initiative of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's intelligence and dexterity values.
    :return: The calculated initiative as a float.
    """
    return (attributes.dexterity + attributes.intelligence) / 2


def calculate_max_mana(attributes: Attributes) -> int:
    """
    Calculate the maximum mana of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's intelligence and dexterity values.
    :return: The calculated maximum mana as an integer.
    """
    return attributes.intelligence + (attributes.dexterity * 2)


def calculate_max_stamina(attributes: Attributes) -> int:
    """
    Calculate the maximum stamina of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength and dexterity values.
    :return: The calculated maximum stamina as an integer.
    """
    return attributes.strength + (attributes.dexterity * 2)


def calculate_max_health(attributes: Attributes) -> int:
    """
    Calculate the maximum health of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength value.
    :return: The calculated maximum health as an integer.
    """
    return attributes.strength * 10 + 25


def calculate_status_resistence(attributes: Attributes) -> float:
    """
    Calculate the status resistance of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength, dexterity, and intelligence values.
    :return: The calculated status resistance as a float.
    """
    return (attributes.dexterity + attributes.intelligence + attributes.strength) / 3


def calculate_magic_resistence(attributes: Attributes) -> float:
    """
    Calculate the magic resistance of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength, dexterity, and intelligence values.
    :return: The calculated magic resistance as a float.
    """
    return (attributes.dexterity + attributes.intelligence) / 2


def calculate_physical_resistence(attributes: Attributes) -> float:
    """
    Calculate the physical resistance of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength, dexterity, and intelligence values.
    :return: The calculated physical resistance as a float.
    """
    return (attributes.dexterity + attributes.strength) / 2


def calculate_magic_power(attributes: Attributes) -> float:
    """
    Calculate the magic power of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength, dexterity, and intelligence values.
    :return: The calculated magic power as a float.
    """
    return (attributes.dexterity + attributes.intelligence) * 2


def calculate_physical_power(attributes: Attributes) -> float:
    """
    Calculate the physical power of a character based on their attributes.

    :param attributes: The Attributes instance containing a character's strength, dexterity, and intelligence values.
    :return: The calculated physical power as a float.
    """
    return (attributes.dexterity + attributes.strength) * 2


def character_str(character: Character) -> str:
    """
    Generate a string representation of a character, displaying all of its attributes.

    :param character: The character object.
    :return: A formatted string containing all the character's attributes.
    """
    attribute_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in character.attributes.__dict__.items()])
    calculated_attr_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in
                                     character.calculated_attributes.__dict__.items()])
    abilities_str = ", ".join(character.character_class.abilities)

    return (
        f"Name: {character.name}\n"
        f"Class: {character.character_class.name}\n"
        f"Race: {character.race.name}\n"
        f"Level: {character.level}\n"
        f"Current Health: {character.health}/{character.max_health}\n"
        f"Current stamina: {character.stamina}/{character.max_stamina}\n"
        f"Current Mana: {character.mana}/{character.max_mana}\n"
        f"Attack: {character.attack}\n"
        f"Defense: {character.defense}\n"
        f"Attributes:\n{attribute_str}\n"
        f"Calculated Attributes:\n{calculated_attr_str}\n"
        f"Abilities: {abilities_str}\n"
        f"Experience: {character.experience}"
    )
