class CalculatedAttributes:
    """
        A class representing the calculated attributes of a character in a game.

        :param initiative: The character's initiative value.
        :param status_resistence: The character's resistance to status effects.
        :param magic_resistence: The character's resistance to magic attacks.
        :param physical_resistence: The character's resistance to physical attacks.
        :param magic_power: The character's power in magic attacks.
        :param physical_power: The character's power in physical attacks.
    """

    def __init__(self, initiative, status_resistence, magic_resistence, physical_resistence, magic_power,
                 physical_power):
        self.initiative = initiative
        self.status_resistence = status_resistence
        self.magic_resistence = magic_resistence
        self.physical_resistence = physical_resistence
        self.magic_power = magic_power
        self.physical_power = physical_power
