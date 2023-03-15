from service.character_service import take_damage, is_alive, attack_enemy, award_experience


def battle(character1, character2):
    round_number = 1

    while is_alive(character1) and is_alive(character2):
        print(f"Round {round_number}:")

        if is_alive(character1):
            attack_enemy(character1, character2)
        if is_alive(character2):
            attack_enemy(character2, character1)

        print(f"{character1.name} has {character1.health} health remaining.")
        print(f"{character2.name} has {character2.health} health remaining.")

        round_number += 1

    if is_alive(character1) and is_alive(character2):
        print("\nBattle ends!\nThe battle is a draw!")
        return None
    else:
        winner = character1 if is_alive(character1) else character2
        award_experience(winner, 100)
        print(f"\nBattle ends!\n{winner.name} wins!")

        return winner


def attack_round(attacker, defender):
    damage_dealt = max(0, attacker.attack - defender.defense)
    take_damage(defender, damage_dealt)
    print(
        f"{attacker.name} attacks {defender.name} for {damage_dealt} damage! {defender.name} has {defender.health} health remaining.")
