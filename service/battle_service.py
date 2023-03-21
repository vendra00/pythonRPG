from typing import Union

from colorama import Fore, Style

from model import ability_pool
from model.character import Character
from model.format_factory import separator
from model.game_enums import DecisionEnum, EffectTypeEnum
from service.character_service import is_alive, award_experience, calculate_physical_dmg, print_attack_log


def battle(attacker: Character, defender: Character) -> Union[Character, None]:
    """
        Simulates a battle between two characters and prints the results of each round.
        The battle continues until one of the characters is no longer alive.

        :param attacker: The first character participating in the battle.
        :type attacker: Character
        :param defender: The second character participating in the battle.
        :type defender: Character
        :return: The winning character, or None if both characters are still alive after the loop.
        :rtype: Union[Character, None]
    """
    round_number: int = round_init()

    # Check if characters are alive and print result
    while is_alive(attacker) and is_alive(defender):
        # Print round number
        print_rounds(round_number)

        # Check if character is alive and attack
        check_if_character_is_alive_and_perform_action(attacker, defender)

        # Print health remaining from characters
        print_health_mana_stamina_remaining(attacker, defender)

        # Add next round
        round_number: int = add_round(round_number)

    # Check if characters are alive and print result
    if is_alive(attacker) and is_alive(defender):
        # Print result
        print_battle_result_draw()
        return None
    else:
        # Check who is alive and award experience
        winner = check_character_is_alive(attacker, defender)
        # Award experience
        award_experience(winner)
        # Print winner
        print_battle_winner(winner)

        return winner


def check_character_is_alive(attacker: Character, defender: Character) -> Character:
    """
        Determines which of the two characters is still alive and returns the alive character.

        :param attacker: The first character participating in the battle.
        :type attacker: Character
        :param defender: The second character participating in the battle.
        :type defender: Character
        :return: The character that is still alive, or None if both characters are dead.
        :rtype: Character
    """
    return attacker if is_alive(attacker) else defender


def round_init() -> int:
    """
        Initialize the round number for a battle.

        :return: The initial round number.
    """
    round_number = 1
    return round_number


def add_round(round_number: int) -> int:
    """
        Increment the round number in a battle.

        :param round_number: The current round number.
        :return: The incremented round number.
    """
    round_number += 1
    return round_number


def print_battle_winner(winner: Character) -> None:
    """
        Print the winner of the battle.

        :param winner: The winning Character instance.
    """
    print(f"{separator}\n{Style.BRIGHT}Battle ends!{Style.RESET_ALL}\n{Style.BRIGHT}{Fore.GREEN}{winner.name}"
          f"{Style.RESET_ALL} {Style.BRIGHT}wins!{Style.RESET_ALL}{separator}")


def print_battle_result_draw() -> None:
    """
        Print the result of a battle when it is a draw.
    """
    print(f"{separator}\nBattle ends!\nThe battle is a draw!")


def print_rounds(round_number: int) -> None:
    """
        Print the current round number with a separator before it.

        :param round_number: The current round number in the battle.
    """
    print(f"{separator}\n{Style.BRIGHT}Round {Fore.CYAN}{round_number}{Style.RESET_ALL}:")


def print_health_mana_stamina_remaining(attacker: Character, defender: Character) -> None:
    """
        Prints the health, mana, and stamina remaining for the attacker and defender characters.

        :param attacker: The first character participating in the battle.
        :type attacker: Character
        :param defender: The second character participating in the battle.
        :type defender: Character
        :return: None
    """
    print_character(attacker)
    print_character(defender)


def print_character(character: Character) -> None:
    """
        Prints the current health, stamina, and mana of a given character.

        :param character: The character whose attributes will be printed.
        :type character: Character
        :return: None
    """
    print(f"{separator}\n{Style.BRIGHT + Fore.GREEN}{character.name}{Style.RESET_ALL} has {Style.BRIGHT + Fore.RED}"
          f"{int(character.health)}{Style.RESET_ALL}/{Style.BRIGHT + Fore.RED}{int(character.max_health)}"
          f"{Style.RESET_ALL} health, {Style.BRIGHT + Fore.GREEN}{int(character.stamina)}"
          f"{Style.RESET_ALL}/{Style.BRIGHT + Fore.GREEN}{int(character.max_stamina)}{Style.RESET_ALL} stamina and "
          f"{Style.BRIGHT + Fore.BLUE}{int(character.mana)}{Style.RESET_ALL}/{Style.BRIGHT + Fore.BLUE}"
          f"{int(character.max_mana)}{Style.RESET_ALL} mana remaining.{separator}")


def check_if_character_is_alive_and_perform_action(attacker: Character, defender: Character) -> None:
    """
        Checks if the attacker and defender characters are still alive and performs their actions in a battle.

        :param attacker: The first character participating in the battle.
        :type attacker: Character
        :param defender: The second character participating in the battle.
        :type defender: Character
        :return: None
    """
    attacker_decision: tuple = get_decision(attacker)
    defender_decision: tuple = get_decision(defender)

    if is_alive(attacker):
        perform_decision(attacker, defender, attacker_decision)
    if is_alive(defender):
        perform_decision(defender, attacker, defender_decision)


def health_color(character: Character):
    """
        Determines the appropriate color for the character's health display based on their current health percentage.

        :param character: The character object.
        :type character: Character
        :return: The color code (as a string) for the character's health display.
        :rtype: str
    """
    # Calculate the character's health percentage.
    health_percentage = health_percentage_formula(character)

    if health_percentage > 70:
        return Fore.LIGHTGREEN_EX
    if 30 <= health_percentage <= 70:
        return Fore.LIGHTYELLOW_EX
    else:
        return Fore.LIGHTRED_EX


def health_percentage_formula(character: Character) -> float:
    """
        Calculates the percentage of a character's health remaining.

        :param character: The character whose health percentage will be calculated.
        :type character: Character
        :return: The percentage of the character's health remaining.
        :rtype: float
    """
    return (character.health / character.max_health) * 100


def get_decision(character: Character) -> tuple:
    """
        Gets the character's decision for the current battle round.

        :param character: The character object.
        :type character: Character
        :return: A tuple with the decision type ('attack', 'ability', 'item', or 'flee') and the associated decision data.
        :rtype: tuple
    """
    # This is a simple example. You can replace this with a more sophisticated decision-making process.
    decision_type: str = input_action(character)
    decision_data = None

    if decision_type == DecisionEnum.ABILITY.value:
        # Get ability input, for example, "fireball"
        decision_data = input_ability()
    elif decision_type == DecisionEnum.ITEM.value:
        # Get item input, for example, "potion"
        decision_data = input_item()

    return decision_type, decision_data


def input_item() -> str:
    """
        Prompts the user to enter the name of an item to use in battle.

        :return: The name of the item entered by the user.
        :rtype: str
    """
    return input("Enter the item you want to use: ").lower()


def input_ability() -> str:
    """
        Prompts the user to enter the name of an ability to use in battle.

        :return: The name of the ability entered by the user.
        :rtype: str
    """
    return input("Enter the ability you want to use: ").capitalize()


def input_action(character: Character) -> str:
    """
        Prompts the user to enter an action for the given character to take in battle.

        :param character: The character whose action will be chosen.
        :type character: Character
        :return: The action chosen by the user, as a string.
        :rtype: str
    """
    return input(f"{character.name}, choose your action: attack, ability, item, or flee: ").lower()


def use_ability(attacker: Character, defender: Character, ability: dict) -> None:
    """
        Allows a character to use an ability against an enemy.

        :param attacker: The character object representing the character using the ability.
        :type attacker: Character
        :param defender: The character object representing the enemy being targeted by the ability.
        :type defender: Character
        :param ability: A dictionary containing the ability's data, including its name, mana and stamina cost, and effect.
        :type ability: dict
        :return: None
    """

    # Get the ability's name
    ability_name = get_ability_name(ability)

    if ability is None:
        print_unknow_ability(ability_name, attacker)
        return

    if attacker.mana < ability['mana_cost']:
        print_not_enought_mana(ability_name, attacker)
        return

    if attacker.stamina < ability['stamina_cost']:
        print_not_enought_stamina(ability_name, attacker)
        return

    # Deduct the mana and stamina cost
    deduct_mana_stamina_cost(ability, attacker)

    # Apply the ability's effect
    apply_ability_effect(attacker, defender, ability)


def print_not_enought_stamina(ability_name: str, attacker: Character) -> None:
    """
        Prints a message indicating that the attacker does not have enough stamina to use the specified ability.

        :param ability_name: The name of the ability that the attacker is trying to use.
        :type ability_name: str
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    print(f"{attacker.name} does not have enough stamina to use {ability_name}")


def print_not_enought_mana(ability_name: str, attacker: Character) -> None:
    """
        Prints a message indicating that the attacker does not have enough mana to use the specified ability.

        :param ability_name: The name of the ability that the attacker is trying to use.
        :type ability_name: str
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    print(f"{attacker.name} does not have enough mana to use {ability_name}")


def print_unknow_ability(ability_name: str, attacker: Character) -> None:
    """
        Prints a message indicating that the attacker tried to use an unknown ability.

        :param ability_name: The name of the unknown ability.
        :type ability_name: str
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    print(f"{attacker.name} tried to use an unknown ability: {ability_name}")


def get_ability_name(decision_data: dict) -> str:
    """
        Retrieves the name of an ability from the ability's data dictionary.

        :param decision_data: The dictionary containing the ability's data, including its name.
        :type decision_data: dict
        :return: The name of the ability.
        :rtype: str
    """
    return decision_data['title']


def deduct_mana_stamina_cost(ability: dict, attacker: Character) -> None:
    """
        Deducts the mana and stamina cost of using an ability from the attacker's mana and stamina.

        :param ability: A dictionary containing the ability's data, including its mana and stamina cost.
        :type ability: dict
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    mana_deduct(ability, attacker)
    stamina_deduct(ability, attacker)


def stamina_deduct(ability: dict, attacker: Character) -> None:
    """
        Deducts the stamina cost of using an ability from the attacker's stamina.

        :param ability: A dictionary containing the ability's data, including its stamina cost.
        :type ability: dict
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    attacker.stamina -= ability['stamina_cost']


def mana_deduct(ability: dict, attacker: Character) -> None:
    """
        Deducts the mana cost of using an ability from the attacker's mana.

        :param ability: A dictionary containing the ability's data, including its mana cost.
        :type ability: dict
        :param attacker: The character object representing the attacker.
        :type attacker: Character
        :return: None
    """
    attacker.mana -= ability['mana_cost']


def apply_ability_effect(attacker: Character, defender: Character, ability: dict) -> None:
    """
        Applies the effect of an ability used by a character against an enemy or themselves.

        :param attacker: The character object representing the character using the ability.
        :type attacker: Character
        :param defender: The character object representing the enemy being targeted by the ability (can be the same as
        the character using the ability in case of self-targeting effects).
        :type defender: Character
        :param ability: A dictionary containing the ability's data, including its effect type and value.
        :type ability: dict
        :return: None
    """
    # Get the ability's effect type and value
    effect_type: str = get_ability_effect_type(ability)
    effect_value: str = get_ability_effect_value(ability)

    # Apply the effect
    if effect_type == EffectTypeEnum.DAMAGE.value:
        apply_ability_dmg(effect_value, defender)
        print_ability_dmg_use(ability, attacker, effect_value, defender)
    elif effect_type == EffectTypeEnum.HEAL.value:
        apply_ability_heal(attacker, effect_value)
        make_sure_heal_does_not_exceed_max_value(attacker)
        print_ability_heal_use(ability, attacker, effect_value)
    # ... other effect types can be added here
    else:
        print_ability_unknown(effect_type)


def get_ability_effect_value(ability) -> str:
    """
        Retrieves the value of an ability's effect from the ability's data dictionary.

        :param ability: A dictionary containing the ability's data, including its effect value.
        :type ability: dict
        :return: The value of the ability's effect.
        :rtype: str
    """
    return ability['effect_value']


def get_ability_effect_type(ability) -> str:
    """
        Retrieves the type of an ability's effect from the ability's data dictionary.

        :param ability: A dictionary containing the ability's data, including its effect type.
        :type ability: dict
        :return: The type of the ability's effect.
        :rtype: str
    """
    return ability['effect_type']


def print_ability_unknown(effect_type: str) -> None:
    """
        Prints a message indicating that an unknown ability effect type was encountered.

        :param effect_type: The unknown effect type as a string.
        :return: None
    """
    print(f"Unknown ability effect type: {effect_type}")


def apply_ability_heal(character: Character, effect_value: str) -> None:
    """
        Apply healing effect to the given character.

        :param character: The character receiving the healing effect.
        :param effect_value: The value of the healing effect.
        :return: None
    """
    character.health += effect_value


def apply_ability_dmg(effect_value: str, defender: Character) -> None:
    """
        Applies a damage effect to the given enemy character.

        :param effect_value: The value of the damage effect.
        :type effect_value: str
        :param defender: The enemy character receiving the damage effect.
        :type defender: Character
        :return: None
    """
    defender.health -= effect_value


def make_sure_heal_does_not_exceed_max_value(character: Character) -> None:
    """
        Ensure that the character's health does not exceed the maximum health value.

        :param character: The character whose health should be checked.
        :return: None
    """
    character.health = min(character.health, character.max_health)


def print_ability_heal_use(ability: dict, character: Character, effect_value: str) -> None:
    """
        Print a message to indicate the character has used a healing ability.

        :param ability: A dictionary containing the ability's details.
        :param character: The character who used the healing ability.
        :param effect_value: The amount of health restored by the ability.
        :return: None
    """
    print(f"{character.name} heals themselves for {effect_value} with {ability['title']}!")


def print_ability_dmg_use(ability: dict, character: Character, effect_value: str, enemy: Character) -> None:
    """
        Print a message to indicate the character has used a damaging ability.

        :param ability: A dictionary containing the ability's details.
        :param character: The character who used the damaging ability.
        :param effect_value: The amount of damage dealt by the ability.
        :param enemy: The enemy character who received the damage.
        :return: None
    """
    print(f"{character.name} deals {effect_value} damage to {enemy.name} with {ability['title']}!")


def use_item(character: Character, decision_data):
    pass


def flee_attempt(character: Character):
    pass


def perform_decision(attacker: Character, defender: Character, decision: tuple) -> None:
    """
        Performs an action based on the character's decision.

        :param attacker: The character object representing the character performing the action.
        :type attacker: Character
        :param defender: The enemy character object.
        :type defender: Character
        :param decision: A tuple with the decision type ('attack', 'ability', 'item', or 'flee')
        and the associated decision data.
        :type decision: tuple
        :return: None
    """
    decision_type, decision_data = decision

    if decision_type == DecisionEnum.ABILITY.value:
        ability_name = decision_data
        # Get the ability data from the ability_pool module for the character's class
        class_abilities = getattr(ability_pool, attacker.character_class.name.lower(), {})
        ability_data = class_abilities.get(ability_name)
        if ability_data:
            use_ability(attacker, defender, ability_data)
        else:
            print_charcarter_does_not_have_ability(ability_name, attacker)
    elif decision_type == DecisionEnum.ATTACK.value:
        attack_enemy(attacker, defender)
    elif decision_type == DecisionEnum.ITEM.value:
        use_item(attacker, decision_data)
    elif decision_type == DecisionEnum.FLEE.value:
        flee_attempt(attacker)
    else:
        print_invalid_decision(attacker)


def attack_enemy(attacker: Character, defender: Character) -> None:
    """
        Calculate the damage dealt by the attacker to the defender, apply the damage, and print the result.

        :param attacker: The attacking Character instance.
        :param defender: The defending Character instance.
    """
    damage_dealt: float = calculate_physical_dmg(attacker, defender)
    take_damage(defender, damage_dealt)  # Use the take_damage function instead of the method
    print_attack_log(attacker, damage_dealt, defender)


def take_damage(character: Character, damage: float) -> None:
    """
        Inflict damage to a character, reducing their health.

        :param character: The Character instance to take damage.
        :param damage: The amount of damage to be inflicted.
    """
    character.health -= damage


def print_invalid_decision(character: Character) -> None:
    """
        Print a message to indicate that the character has made an invalid decision and loses their turn.

        :param character: The character who made the invalid decision.
        :return: None
    """
    print(f"{character.name}, your decision was invalid. You lose your turn.")


def print_charcarter_does_not_have_ability(ability_name: str, character: Character):
    """
        Print a message to indicate that the character does not have the specified ability.

        :param ability_name: The name of the ability that the character does not have.
        :param character: The character who does not have the specified ability.
        :return: None
    """
    print(f"{character.name} does not have the ability '{ability_name}'")
