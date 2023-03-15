from model.character_class import CharacterClass

wizard_modifiers = {
    "intelligence": 2,
    "dexterity": 0,
    "strength": -2
}
wizard_abilities = ["Fireball", "Teleport"]

warrior_modifiers = {
    "intelligence": -1,
    "dexterity": 0,
    "strength": 2
}
warrior_abilities = ["Cleave", "Charge"]

# Add more character classes as needed

class_data = {
    "Wizard": CharacterClass("Wizard", wizard_modifiers, wizard_abilities),
    "Warrior": CharacterClass("Warrior", warrior_modifiers, warrior_abilities),
    # Add more character classes as needed
}
