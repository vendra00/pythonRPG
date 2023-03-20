from enum import Enum


class DecisionEnum(Enum):
    ABILITY = "ability"
    ITEM = "item"
    ATTACK = "attack"
    FLEE = "flee"


class EffectTypeEnum(Enum):
    DAMAGE = "damage"
    HEAL = "heal"


class CalculatedAttributesEnum(Enum):
    initiative = "Initiative"
    status_resistence = "Status Resistence"
    magic_resistence = "Magic Resistence"
    physical_resistence = "Physical Resistence"
    magic_power = "Magic Power"
    physical_power = "Physical Power"


class AttributesEnum(Enum):
    strength = "Strength"
    intelligence = "Intelligence"
    dexterity = "Dexterity"
