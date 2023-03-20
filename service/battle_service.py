from typing import Union

from colorama import Fore, Style

from model import ability_pool
from model.character import Character
from model.format_factory import separator
from model.game_enums import DecisionEnum, EffectTypeEnum
from service.character_service import is_alive, attack_enemy, award_experience


def battle(character1: Character, character2: Character) -> Union[Character, None]:
    """
        Simulates a battle between two characters and prints the results of each round.
        The battle continues until one of the characters is no longer alive.

        :param character1: The first character participating in the battle.
        :param character2: The second character participating in the battle.
        :return: The winning character, or None if both characters are still alive after the loop.
    """
    round_number: int = round_init()

    # Check if characters are alive and print result
    while is_alive(character1) and is_alive(character2):
        # Print round number
        print_rounds(round_number)

        # Check if character is alive and attack
        check_if_character_is_alive_and_attack(character1, character2)

        # Print health remaining from characters
        print_health_mana_remaining(character1, character2)

        # Add next round
        round_number: int = add_round(round_number)

    # Check if characters are alive and print result
    if is_alive(character1) and is_alive(character2):
        # Print result
        print_battle_result()
        return None
    else:
        # Check who is alive and award experience
        winner = check_character_is_alive(character1, character2)
        # Award experience
        award_experience(winner)
        # Print winner
        print_battle_winner(winner)

        return winner


def check_character_is_alive(character1: Character, character2: Character) -> Character:
    """
        Checks which of the two characters is alive and returns the alive character.

        :param character1: The first character participating in the battle.
        :param character2: The second character participating in the battle.
        :return: The character that is still alive.
    """
    return character1 if is_alive(character1) else character2


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


def print_battle_result():
    """
        Print the result of a battle when it is a draw.
    """
    print(f"{separator}\nBattle ends!\nThe battle is a draw!")


def print_rounds(round_number: int):
    """
        Print the current round number with a separator before it.

        :param round_number: The current round number in the battle.
    """
    print(f"{separator}\n{Style.BRIGHT}Round {Fore.CYAN}{round_number}{Style.RESET_ALL}:")


def print_health_mana_remaining(character1: Character, character2: Character):
    """
        Print the remaining health of two characters in a color-coded format based on their health percentages.

        :param character1: The first character object.
        :param character2: The second character object.
    """
    print(f"{separator}\n{Style.BRIGHT}{Fore.GREEN}{character1.name}{Style.RESET_ALL} has {Style.BRIGHT}"
          f"{health_color(character1)}{int(character1.health)}"
          f"{Style.RESET_ALL} health and {Style.BRIGHT}{Fore.BLUE}{int(character1.mana)}{Style.RESET_ALL}"
          f" mana remaining.{separator}")
    print(f"{separator}\n{Style.BRIGHT}{Fore.RED}{character2.name}{Style.RESET_ALL} has {Style.BRIGHT}"
          f"{health_color(character2)}{int(character2.health)}"
          f"{Style.RESET_ALL} health and {Style.BRIGHT}{Fore.BLUE}{int(character2.mana)}{Style.RESET_ALL} "
          f"mana remaining.{separator}")


def check_if_character_is_alive_and_attack(character1: Character, character2: Character) -> None:
    """
        Check if characters are alive and perform their decisions in a battle.

        :param character1: The first character participating in the battle.
        :param character2: The second character participating in the battle.
        :return: None
    """
    decision1: tuple = get_decision(character1)
    decision2: tuple = get_decision(character2)

    if is_alive(character1):
        perform_decision(character1, character2, decision1)
    if is_alive(character2):
        perform_decision(character2, character1, decision2)


def health_color(character: Character):
    """
       Determine the appropriate color for the character's health display based on their health percentage.

       :param character: The character object.
       :return: The color code (as a string) for the character's health display.
    """
    health_percentage = (character.health / character.max_health) * 100
    if health_percentage > 70:
        return Fore.GREEN
    if 30 <= health_percentage <= 70:
        return Fore.YELLOW
    else:
        return Fore.RED


def get_decision(character: Character) -> tuple:
    """
    Get the character's decision for the current round.

    :param character: The character object.
    :return: A tuple with the decision type ('attack', 'ability', 'item', or 'flee') and the associated decision data.
    """
    # This is a simple example. You can replace this with a more sophisticated decision-making process.
    decision_type: str = input(f"{character.name}, choose your action: attack, ability, item, or flee: ").lower()
    decision_data = None

    if decision_type == DecisionEnum.ABILITY.value:
        # Get ability input, for example, "fireball"
        decision_data = input("Enter the ability you want to use: ").capitalize()
    elif decision_type == DecisionEnum.ITEM.value:
        # Get item input, for example, "potion"
        decision_data = input("Enter the item you want to use: ").lower()

    return decision_type, decision_data


def use_ability(character: Character, enemy: Character, decision_data) -> None:
    """
        Allows a character to use an ability against an enemy.

        :param character: The Character object representing the character using the ability.
        :param enemy: The Character object representing the enemy being targeted by the ability.
        :param decision_data: A dictionary containing the ability's data.
        :return: None
    """
    ability_name = decision_data['title']
    ability = decision_data

    if ability is None:
        print(f"{character.name} tried to use an unknown ability: {ability_name}")
        return

    if character.mana < ability['mana_cost']:
        print(f"{character.name} does not have enough mana to use {ability_name}")
        return

    # Deduct the mana cost
    character.mana -= ability['mana_cost']

    # Apply the ability's effect
    apply_ability_effect(character, enemy, ability)


def apply_ability_effect(character: Character, enemy: Character, ability: dict) -> None:
    """
        Applies the effect of an ability used by a character against an enemy or themselves.

        :param character: The Character object representing the character using the ability.
        :param enemy: The Character object representing the enemy being targeted by the ability (can be the same as the
        character using the ability in case of self-targeting effects).
        :param ability: A dictionary containing the ability's data.
        :return: None
    """
    effect_type: str = ability['effect_type']
    effect_value: str = ability['effect_value']

    if effect_type == EffectTypeEnum.DAMAGE.value:
        apply_ability_dmg(effect_value, enemy)
        print_ability_dmg_use(ability, character, effect_value, enemy)
    elif effect_type == EffectTypeEnum.HEAL.value:
        apply_ability_heal(character, effect_value)
        make_sure_heal_does_not_exceed_max_value(character)
        print_ability_heal_use(ability, character, effect_value)
    # ... other effect types can be added here
    else:
        print_ability_unknown(effect_type)


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


def apply_ability_dmg(effect_value: str, enemy: Character) -> None:
    """
        Apply damage effect to the given enemy character.

        :param effect_value: The value of the damage effect.
        :param enemy: The enemy character receiving the damage effect.
        :return: None
    """
    enemy.health -= effect_value


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


def perform_decision(character: Character, enemy: Character, decision: tuple) -> None:
    """
    Perform an action based on the character's decision.

    :param character: The character object.
    :param enemy: The enemy character object.
    :param decision: A tuple with the decision type ('attack', 'ability', 'item', or 'flee')
    and the associated decision data.
    """
    decision_type, decision_data = decision

    if decision_type == DecisionEnum.ABILITY.value:
        ability_name = decision_data
        # Get the ability data from the ability_pool module for the character's class
        class_abilities = getattr(ability_pool, character.character_class.name.lower(), {})
        ability_data = class_abilities.get(ability_name)
        if ability_data:
            use_ability(character, enemy, ability_data)
        else:
            print_charcarter_does_not_have_ability(ability_name, character)
    elif decision_type == DecisionEnum.ATTACK.value:
        attack_enemy(character, enemy)
    elif decision_type == DecisionEnum.ITEM.value:
        use_item(character, decision_data)
    elif decision_type == DecisionEnum.FLEE.value:
        flee_attempt(character)
    else:
        print_invalid_decision(character)


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
