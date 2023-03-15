from model.attribute import Attributes
from model.character_classes import class_data
from model.races import race_data
from service.battle_service import battle
from service.character_service import create_character, attack_enemy, level_up, character_str, is_alive, take_damage

hero_name = "Gandalf"
enemy_name = "Sauron"

enemy_attributes = Attributes(10, 10, 10)
hero_attributes = Attributes(10, 10, 10)

# Create characters
hero = create_character(hero_name, 10, 5, 1, hero_attributes, "Elf", "Wizard", race_data, class_data, 0)
enemy = create_character(enemy_name, 10, 5, 1, enemy_attributes, "Elf", "Wizard", race_data, class_data, 0)


# Print character info
print(character_str(hero))
print(character_str(enemy))

# Simulate a battle between the characters
battle(hero, enemy)
