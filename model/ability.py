class Ability:
    def __init__(self, title, mana_cost, type, target, effect_type, effect_status, effect_value, description):
        self.title = title
        self.mana_cost = mana_cost
        self.type = type
        self.target = target
        self.effect_type = effect_type
        self.effect_status = effect_status
        self.effect_value = effect_value
        self.description = description
