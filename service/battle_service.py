from colorama import Fore, Style

from service.character_service import is_alive, attack_enemy, award_experience


def battle(character1, character2):
    separator = "\n" + "=" * 40
    round_number = 1

    while is_alive(character1) and is_alive(character2):
        # Print round number
        print_rounds(round_number, separator)

        # Check if character is alive and attack
        check_if_character_is_alive_and_attack(character1, character2)

        # Print health remaining from characters
        print_health_remaining(character1, character2)

        # Add next round
        round_number += 1

    if is_alive(character1) and is_alive(character2):
        print_battle_result(separator)
        return None
    else:
        winner = character1 if is_alive(character1) else character2
        award_experience(winner, 100)  # Award experience points to the winner
        print_battle_winner(separator, winner)

        return winner


def print_battle_winner(separator, winner):
    """
        Print the winner of the battle.

        :param separator: A separator string to print before the message.
        :param winner: The winning Character instance.
    """
    print(f"{separator}\n{Style.BRIGHT}Battle ends!{Style.RESET_ALL}\n{Style.BRIGHT}{Fore.GREEN}{winner.name}"
          f"{Style.RESET_ALL} {Style.BRIGHT}wins!{Style.RESET_ALL}{separator}")


def print_battle_result(separator):
    """
        Print the result of a battle when it is a draw.

        :param separator: A separator string to be printed before and after the result.
    """
    print(f"{separator}\nBattle ends!\nThe battle is a draw!")


def print_rounds(round_number, separator):
    """
        Print the current round number with a separator before it.

        :param round_number: The current round number in the battle.
        :param separator: A string used as a separator, typically a series of equal signs or other characters.
    """
    print(f"{separator}\n{Style.BRIGHT}Round {Fore.CYAN}{round_number}{Style.RESET_ALL}:")


def print_health_remaining(character1, character2):
    """
        Print the remaining health of two characters in a color-coded format based on their health percentages.

        :param character1: The first character object.
        :param character2: The second character object.
    """
    print(f"{character1.name} has {Style.BRIGHT}{health_color(character1)}{round(character1.health, 2)}"
          f"{Style.RESET_ALL} health remaining.")
    print(f"{character2.name} has {Style.BRIGHT}{health_color(character2)}{round(character2.health, 2)}"
          f"{Style.RESET_ALL} health remaining.")


def check_if_character_is_alive_and_attack(character1, character2):
    """
    Check if both characters are alive and perform an action based on their decision.

    :param character1: The first character object.
    :param character2: The second character object.
    """
    decision1 = get_decision(character1)
    decision2 = get_decision(character2)

    if is_alive(character1):
        perform_decision(character1, character2, decision1)
    if is_alive(character2):
        perform_decision(character2, character1, decision2)


def health_color(character):
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


def get_decision(character):
    """
    Get the character's decision for the current round.

    :param character: The character object.
    :return: A tuple with the decision type ('attack', 'ability', 'item', or 'flee') and the associated decision data.
    """
    # This is a simple example. You can replace this with a more sophisticated decision-making process.
    decision_type = input(f"{character.name}, choose your action: attack, ability, item, or flee: ").lower()
    decision_data = None

    if decision_type == "ability":
        # Get ability input, for example, "fireball"
        decision_data = input("Enter the ability you want to use: ").lower().strip()
    elif decision_type == "item":
        # Get item input, for example, "potion"
        decision_data = input("Enter the item you want to use: ").lower()

    return decision_type, decision_data


def use_ability(character, enemy, decision_data):
    ability_name = decision_data['ability_name']
    ability = character.character_class.abilities.get(ability_name)

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


def apply_ability_effect(character, enemy, ability):
    effect_type = ability['effect_type']
    effect_value = ability['effect_value']

    if effect_type == 'damage':
        enemy.health -= effect_value
        print(f"{character.name} deals {effect_value} damage to {enemy.name} with {ability['title']}!")
    elif effect_type == 'heal':
        character.health += effect_value
        character.health = min(character.health, character.max_health)  # Ensure health doesn't exceed max_health
        print(f"{character.name} heals themselves for {effect_value} with {ability['title']}!")
    # ... other effect types can be added here
    else:
        print(f"Unknown ability effect type: {effect_type}")


def use_item(character, decision_data):
    pass


def flee_attempt(character):
    pass


from model import ability_pool


def perform_decision(character, enemy, decision):
    """
    Perform an action based on the character's decision.

    :param character: The character object.
    :param enemy: The enemy character object.
    :param decision: A tuple with the decision type ('attack', 'ability', 'item', or 'flee') and the associated decision data.
    """
    decision_type, decision_data = decision

    if decision_type == "ability":
        ability_name = decision_data
        # Get the ability data from the ability_pool module for the character's class
        class_abilities = getattr(ability_pool, character.character_class.name.lower(), {})
        ability_data = class_abilities.get(ability_name)
        if ability_data:
            use_ability(character, enemy, ability_data)
        else:
            print(f"{character.name} does not have the ability '{ability_name}'")
    elif decision_type == "attack":
        attack_enemy(character, enemy)
    elif decision_type == "item":
        use_item(character, decision_data)
    elif decision_type == "flee":
        flee_attempt(character)
    else:
        print(f"{character.name}, your decision was invalid. You lose your turn.")
