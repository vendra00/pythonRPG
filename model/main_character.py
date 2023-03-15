from model.character import Character


class MainCharacter(Character):
    def __init__(self, name, health, attack, defense, level, attributes, race, experience=0):
        super().__init__(name, health, attack, defense, level, attributes, race)
        self.experience = experience

    def gain_experience(self, exp_points):
        self.experience += exp_points
        print(f"{self.name} gained {exp_points} experience points!")

    # Add more methods specific to the main character

    # Optionally, you can override the __str__ method to include the main character's experience points
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}\nExperience: {self.experience}"
