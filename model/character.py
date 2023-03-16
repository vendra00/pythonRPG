class Character:
    def __init__(self, name, health, max_health, stamina, max_stamina, mana, max_mana, attack, defense, level,
                 attributes, calculated_attributes, race, character_class, experience):

        self.name = name
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.mana = mana
        self.max_mana = max_mana
        self.attack = attack
        self.defense = defense
        self.level = level
        self.attributes = attributes
        self.calculated_attributes = calculated_attributes
        self.race = race
        self.character_class = character_class
        self.experience = experience
