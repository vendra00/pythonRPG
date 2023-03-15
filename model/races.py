from model.race import Race

elf_attribute_bonuses = {
    "intelligence": 2,
    "dexterity": 2,
    "strength": -1
}

human_attribute_bonuses = {
    "intelligence": 1,
    "dexterity": 1,
    "strength": 1
}

orc_attribute_bonuses = {
    "intelligence": -6,
    "dexterity": 2,
    "strength": 3
}

dwarf_attribute_bonuses = {
    "intelligence": -2,
    "dexterity": -2,
    "strength": 3
}

# Add more races as needed


race_data = {
    "Elf": Race("Elf", elf_attribute_bonuses),
    "Human": Race("Human", human_attribute_bonuses),
    "Orc": Race("Orc", orc_attribute_bonuses),
    "Dwarf": Race("Dwarf", dwarf_attribute_bonuses),
}