class CharacterClass:
    """
        A class representing a character class in a game.

        :param name: The name of the character class.
        :param modifiers: A dictionary containing attribute modifiers for this character class.
        :param abilities: A list of abilities associated with this character class.
    """
    def __init__(self, name, modifiers, abilities):
        self.name = name
        self.modifiers = modifiers
        self.abilities = abilities
