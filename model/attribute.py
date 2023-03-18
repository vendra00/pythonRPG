class Attributes:
    """
        Represents a character's attributes in the game, including intelligence, dexterity, and strength.

        Attributes:
            intelligence (int): The intelligence attribute of the character.
            dexterity (int): The dexterity attribute of the character.
            strength (int): The strength attribute of the character.
     """
    def __init__(self, intelligence, dexterity, strength):
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.strength = strength
