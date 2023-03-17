from colorama import Fore, Style

from service.character_service import is_alive, attack_enemy, award_experience


def battle(character1, character2):
    separator = "\n" + "=" * 40
    round_number = 1

    while is_alive(character1) and is_alive(character2):
        print(f"{separator}\n{Style.BRIGHT}Round {Fore.CYAN}{round_number}{Style.RESET_ALL}:")

        # Attack round
        if is_alive(character1):
            attack_enemy(character1, character2)
        if is_alive(character2):
            attack_enemy(character2, character1)

        print(f"{character1.name} has {Style.BRIGHT}{health_color(character1)}{character1.health}{Style.RESET_ALL} "
              f"health remaining.")
        print(f"{character2.name} has {Style.BRIGHT}{health_color(character2)}{character2.health}{Style.RESET_ALL} "
              f"health remaining.")

        round_number += 1

    if is_alive(character1) and is_alive(character2):
        print(f"{separator}\nBattle ends!\nThe battle is a draw!")
        return None
    else:
        winner = character1 if is_alive(character1) else character2
        award_experience(winner, 100)  # Award experience points to the winner
        print(f"{separator}\n{Style.BRIGHT}Battle ends!{Style.RESET_ALL}\n{Style.BRIGHT}{Fore.GREEN}{winner.name}"
              f"{Style.RESET_ALL} {Style.BRIGHT}wins!{Style.RESET_ALL}")

        return winner


def health_color(character):
    health_percentage = (character.health / character.max_health) * 100
    if health_percentage > 70:
        return Fore.GREEN
    if 30 <= health_percentage <= 70:
        return Fore.YELLOW
    else:
        return Fore.RED
