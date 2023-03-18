class Race:
    """
        Represents a race in the game, with its name and attribute bonuses.

        Attributes:
            name (str): The name of the race.
            attribute_bonuses (dict): A dictionary containing bonuses for specific attributes.
        """
    def __init__(self, name, attribute_bonuses):
        self.name = name
        self.attribute_bonuses = attribute_bonuses  # A dictionary containing bonuses for specific attributes
