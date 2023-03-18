class Character:
    """
        A class representing a character in a game.

        :param name: The name of the character.
        :param health: The character's current health points.
        :param max_health: The character's maximum health points.
        :param stamina: The character's current stamina points.
        :param max_stamina: The character's maximum stamina points.
        :param mana: The character's current mana points.
        :param max_mana: The character's maximum mana points.
        :param attack: The character's attack value.
        :param defense: The character's defense value.
        :param level: The character's current level.
        :param attributes: The character's attributes (intelligence, dexterity, strength).
        :param calculated_attributes: The character's calculated attributes (e.g. health, mana, stamina).
        :param race: The character's race.
        :param character_class: The character's class.
        :param experience: The character's current experience points.
    """
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
