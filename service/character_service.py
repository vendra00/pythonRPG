from typing import Tuple, Optional

from colorama import init, Style, Fore

from model.character_class import CharacterClass
from model.race import Race
from model.attribute import Attributes
from model.calculated_attribute import CalculatedAttributes
from model.character import Character

init(autoreset=True)  # Automatically resets the color after each print statement


def create_character(name, attack, defense, level, attributes, race_name, class_name, race_data, class_data, experience,
                     health=None, stamina=None, mana=None):
    """
    Create a character with the given parameters.

    :param name: The name of the character.
    :param attack: The base attack value of the character.
    :param defense: The base defense value of the character.
    :param level: The character's level.
    :param attributes: An Attributes object containing the character's base attributes (strength, intelligence, agility).
    :param race_name: The name of the character's race.
    :param class_name: The name of the character's class.
    :param race_data: A dictionary containing race data.
    :param class_data: A dictionary containing class data.
    :param experience: The character's experience points.
    :param health: The character's current health (optional). If not provided, it will be set to max_health.
    :param stamina: The character's current stamina (optional). If not provided, it will be set to max_stamina.
    :param mana: The character's current mana (optional). If not provided, it will be set to max_mana.

    :return: A dictionary representing the character with the given parameters and calculated derived attributes.
    :rtype: dict
    :raises ValueError: if race_name or class_name are not in the respective data dictionaries.
    :raises TypeError: if attributes is not an instance of the Attributes class.
    """
    # Set character bio
    character_class, race = set_character_bio(class_data, class_name, race_data, race_name)

    # Apply race attribute bonuses
    adjusted_attributes = apply_attributes_adjustments(attributes, character_class, race)

    # Calculate max values based on attributes
    max_health, max_mana, max_stamina = calculate_max_values(adjusted_attributes)

    # Set mana, health, stamina max values if not provided
    health, mana, stamina = set_max_values(health, mana, max_health, max_mana, max_stamina, stamina)

    # Ensure the character's health doesn't exceed max_health
    health, mana, stamina = check_max_values(health, mana, max_health, max_mana, max_stamina, stamina)

    # Calculate derived attributes
    character = calculate_derived_attributes(adjusted_attributes, attack, character_class, defense, experience, health,
                                             level, mana, max_health, max_mana, max_stamina, name, race, stamina)

    return character


def apply_attributes_adjustments(attributes: Attributes, character_class: CharacterClass, race: Race) -> Attributes:
    """
    Applies attribute adjustments to a character based on their chosen class and race.

    Args:
        attributes (dict): A dictionary containing the initial attribute values for the character.
        character_class (str): The chosen character class.
        race (str): The chosen character race.

    Returns:
        dict: A dictionary containing the adjusted attribute values for the character.
    """
    adjusted_attributes_race = apply_race_attribute_bonuses(attributes, race)
    adjusted_attributes = apply_class_attribute_bonuses(adjusted_attributes_race, character_class)
    return adjusted_attributes


def exp_to_next_level(current_level):
    """
    Calculate the experience points required for the character to reach the next level.

    :param current_level: The current level of the character.
    :return: Experience points required to reach the next level.
    """
    return (current_level ** 2) * 100


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


def apply_class_attribute_bonuses(attributes: Attributes, character_class: CharacterClass) -> Attributes:
    """
    Apply the attribute bonuses from the character's class to their base attributes.

    :param character_class: The character's class as an instance of the character_class class.
    :param attributes: The character's base attributes as an instance of the Attributes class.
    :return: A new instance of the Attributes class with the adjusted attributes.
    """
    adjusted_attributes = Attributes(
        intelligence=attributes.intelligence + character_class.modifiers["intelligence"],
        dexterity=attributes.dexterity + character_class.modifiers["dexterity"],
        strength=attributes.strength + character_class.modifiers["strength"],
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
    print(f"{attacker.name} attacks {defender.name} and deals "
          f"{Style.BRIGHT}{Fore.RED}{damage_dealt}{Style.RESET_ALL} damage.")


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


def level_up(character):
    """
    Level up the character, increasing their level, attributes, and other properties.

    :param character: The character to level up.
    :return: The updated character.
    """

    # Save the character's old values
    old_level, old_level_dexterity, old_level_intelligence, old_level_strength, old_max_health, old_max_mana, \
        old_max_stamina = hold_old_lvl_stats(character)

    # Increase the character's level by 1
    character.level += 1

    # Update the character's attributes
    attributes_updater(character)

    # Recalculate derived attributes
    character.max_health, character.max_mana, character.max_stamina = \
        calculate_max_values(character.attributes)

    # Recalculate derived attributes
    character = prepare_character_recalculate(character)

    # Restore health, mana, and stamina to their maximum values
    restore_vitals(character)

    # Print the character's new stats
    print_new_lvl_stats(character, old_level, old_level_dexterity, old_level_intelligence, old_level_strength,
                        old_max_health, old_max_mana, old_max_stamina)

    return character


def restore_vitals(character) -> None:
    """
    Restore the character's health, mana, and stamina to their maximum values.

    :param character: The character whose vitals need to be restored.
    :return: None
    """
    character.health = character.max_health
    character.mana = character.max_mana
    character.stamina = character.max_stamina


def hold_old_lvl_stats(character) -> Tuple[int, int, int, int, int, int, int]:
    """
    Save the character's old values before leveling up.

    :param character: The character whose old values need to be saved.
    :return: A tuple containing the old level, old dexterity, old intelligence, old strength, old max health,
    old max mana, and old max stamina.
    """
    old_level = character.level
    old_level_strength = character.attributes.strength
    old_level_intelligence = character.attributes.intelligence
    old_level_dexterity = character.attributes.dexterity
    old_max_health = character.max_health
    old_max_mana = character.max_mana
    old_max_stamina = character.max_stamina
    return old_level, old_level_dexterity, old_level_intelligence, old_level_strength, old_max_health, old_max_mana, \
        old_max_stamina


def attributes_updater(character) -> None:
    """
    Update the character's attributes upon leveling up.

    :param character: The character whose attributes need to be updated.
    :return: None
    """
    character.attributes.strength += 1
    character.attributes.intelligence += 1
    character.attributes.dexterity += 1


def prepare_character_recalculate(character) -> Character:
    """
    Prepare the character for recalculating derived attributes.

    :param character: The character whose derived attributes need to be recalculated.
    :return: The updated character with recalculated derived attributes.
    """
    character = calculate_derived_attributes(
        adjusted_attributes=character.attributes,
        attack=character.attack,
        character_class=character.character_class,
        defense=character.defense,
        experience=character.experience,
        health=character.health,
        level=character.level,
        mana=character.mana,
        max_health=character.max_health,
        max_mana=character.max_mana,
        max_stamina=character.max_stamina,
        name=character.name,
        race=character.race,
        stamina=character.stamina
    )
    return character


def print_new_lvl_stats(character, old_level, old_level_dexterity, old_level_intelligence, old_level_strength,
                        old_max_health, old_max_mana, old_max_stamina) -> None:
    """
    Print the character's new stats after leveling up.

    :param character: The character whose new stats need to be printed.
    :param old_level: The character's old level before leveling up.
    :param old_level_dexterity: The character's old dexterity before leveling up.
    :param old_level_intelligence: The character's old intelligence before leveling up.
    :param old_level_strength: The character's old strength before leveling up.
    :param old_max_health: The character's old max health before leveling up.
    :param old_max_mana: The character's old max mana before leveling up.
    :param old_max_stamina: The character's old max stamina before leveling up.
    :return: None
    """
    print("\n" + "=" * 40)
    print(f"{Fore.GREEN}{character.name} has leveled up to level {character.level}!\n{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Level{Style.RESET_ALL}        {old_level:>3} -> {Style.BRIGHT}{character.level:<3}"
          f"{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Max Health{Style.RESET_ALL}   {old_max_health:>3} -> {Style.BRIGHT}{Fore.CYAN}"
          f"{character.max_health:<3}"
          f"{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Max Mana{Style.RESET_ALL}     {old_max_mana:>3} -> {Style.BRIGHT}{Fore.CYAN}"
          f"{character.max_mana:<3}"
          f"{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Max Stamina{Style.RESET_ALL}  {old_max_stamina:>3} -> {Style.BRIGHT}{Fore.CYAN}"
          f"{character.max_stamina:<3}"
          f"{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Strength{Style.RESET_ALL}     {old_level_strength:>3} -> {Style.BRIGHT}{Fore.YELLOW}"
          f"{character.attributes.strength:<3}{Style.RESET_ALL}")
    print(
        f"{Style.BRIGHT}Intelligence{Style.RESET_ALL} {old_level_intelligence:>3} -> {Style.BRIGHT}{Fore.YELLOW}"
        f"{character.attributes.intelligence:<3}"
        f"{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Dexterity{Style.RESET_ALL}    {old_level_dexterity:>3} -> {Style.BRIGHT}{Fore.YELLOW}"
          f"{character.attributes.dexterity:<3}"
          f"{Style.RESET_ALL}")
    print("=" * 40 + "\n")


def award_experience(character, experience_points):
    """
    Award experience points to the character and level up the character if necessary.

    :param character: The character to receive the experience points.
    :param experience_points: The amount of experience points to award.
    :return: The updated character.
    """
    # Add experience points to the character's current experience
    character.experience += experience_points

    print(f"{character.name} gained {experience_points} experience points!")

    # Check if the character has enough experience points to level up
    while character.experience >= exp_to_next_level(character.level):
        # Subtract the experience points required to level up
        character.experience -= exp_to_next_level(character.level)

        # Level up the character
        character = level_up(character)

    return character


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
    separator = "\n" + "=" * 40
    attribute_str = "\n".join([f"{key.capitalize()}: {Fore.YELLOW}{value}{Style.RESET_ALL}" for key, value in
                               character.attributes.__dict__.items()])
    calculated_attr_str = "\n".join([f"{key.capitalize()}: {Fore.GREEN}{value}{Style.RESET_ALL}" for key, value in
                                     character.calculated_attributes.__dict__.items()])
    abilities_str = f"{Fore.CYAN}{', '.join(character.character_class.abilities)}{Style.RESET_ALL}"

    return (
        f"{separator}"
        f"{separator}\n"
        f"Name: {Fore.GREEN}{character.name}{Style.RESET_ALL}"
        f"{separator}\n"
        f"Class: {Fore.GREEN}{character.character_class.name}{Style.RESET_ALL}\n"
        f"Race: {Fore.GREEN}{character.race.name}{Style.RESET_ALL}\n"
        f"Level: {Fore.GREEN}{character.level}{Style.RESET_ALL}\n"
        f"Current Health: {Fore.GREEN}{character.health}/{character.max_health}{Style.RESET_ALL}\n"
        f"Current Stamina: {Fore.GREEN}{character.stamina}/{character.max_stamina}{Style.RESET_ALL}\n"
        f"Current Mana: {Fore.GREEN}{character.mana}/{character.max_mana}{Style.RESET_ALL}\n"
        f"Attack: {Fore.GREEN}{character.attack}{Style.RESET_ALL}\n"
        f"Defense: {Fore.GREEN}{character.defense}{Style.RESET_ALL}\n"
        f"Attributes:\n{attribute_str}\n"
        f"Calculated Attributes:\n{calculated_attr_str}\n"
        f"Abilities: {abilities_str}\n"
        f"Experience: {Fore.GREEN}{character.experience}{Style.RESET_ALL}"
        f"{separator}"
    )
