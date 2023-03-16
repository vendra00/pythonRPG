from model.attribute import Attributes
from model.character_classes import class_data
from model.races import race_data
from service.battle_service import battle
from service.character_service import create_character, character_str

hero_name = "Gandalf"
enemy_name = "Sauron"

hero_race = "Elf"
enemy_race = "Elf"

hero_class = "Wizard"
enemy_class = "Wizard"

hero_attack = 10
enemy_attack = 10

hero_defense = 5
enemy_defense = 5

hero_level = 1
enemy_level = 1

hero_experience = 0
enemy_experience = 0

hero_intelligence = 10
enemy_intelligence = 10

hero_dexterity = 10
enemy_dexterity = 10

hero_strength = 10
enemy_strength = 10

enemy_attributes = Attributes(hero_intelligence, hero_dexterity, hero_strength)
hero_attributes = Attributes(enemy_intelligence, enemy_dexterity, enemy_strength)


# Create characters
hero = create_character(hero_name, hero_attack, hero_defense, hero_level, hero_attributes, hero_race, hero_class, race_data, class_data, hero_experience)
enemy = create_character(enemy_name, enemy_attack, enemy_defense, enemy_level, enemy_attributes, enemy_race, enemy_class, race_data, class_data, enemy_experience)


# Print character info
print(character_str(hero))
print(character_str(enemy))

# Simulate a battle between the characters
battle(hero, enemy)
