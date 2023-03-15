from model.attribute import Attributes
from model.character_classes import class_data
from model.races import race_data
from service.character_service import create_character, attack_enemy, level_up, character_str, is_alive, take_damage

hero_name = "Gandalf"
enemy_name = "Sauron"

enemy_attributes = Attributes(8, 8, 8)
hero_attributes = Attributes(10, 10, 10)

# Create characters
hero = create_character(hero_name, 100, 10, 5, 1, hero_attributes, "Elf", "Wizard", race_data, class_data)
enemy = create_character(enemy_name, 50, 8, 3, 1, enemy_attributes, "Human", "Warrior", race_data, class_data)

# Use service functions
attack_enemy(hero, enemy)
level_up(hero)

take_damage(enemy, 10)
alive = is_alive(hero)
print(f"{hero.name} is {'alive' if alive else 'dead'}")

# Print character info
print(character_str(hero))
