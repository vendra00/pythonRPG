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
        print(f"{separator}\nBattle ends!\nThe battle is a draw!")
        return None
    else:
        winner = character1 if is_alive(character1) else character2
        award_experience(winner, 100)  # Award experience points to the winner
        print(f"{separator}\n{Style.BRIGHT}Battle ends!{Style.RESET_ALL}\n{Style.BRIGHT}{Fore.GREEN}{winner.name}"
              f"{Style.RESET_ALL} {Style.BRIGHT}wins!{Style.RESET_ALL}{separator}")

        return winner


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
    print(f"{character1.name} has {Style.BRIGHT}{health_color(character1)}{character1.health}{Style.RESET_ALL} "
          f"health remaining.")
    print(f"{character2.name} has {Style.BRIGHT}{health_color(character2)}{character2.health}{Style.RESET_ALL} "
          f"health remaining.")


def check_if_character_is_alive_and_attack(character1, character2):
    """
        Check if both characters are alive and perform an attack round.

        :param character1: The first character object.
        :param character2: The second character object.
    """
    if is_alive(character1):
        attack_enemy(character1, character2)
    if is_alive(character2):
        attack_enemy(character2, character1)


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
