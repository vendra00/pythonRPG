from enum import Enum


class DecisionEnum(Enum):
    ABILITY = "ability"
    ITEM = "item"
    ATTACK = "attack"
    FLEE = "flee"


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


class AbilityTypeEnum(Enum):
    SPELL = "spell"
    PHYSICAL = "physical"


class SpellTitleEnum(Enum):
    FIREBALL = "Fireball"
    MAGIC_MISSILE = "Magic missile"
    SHIELD = "Shield"
    MAGE_ARMOR = "Mage armor"
    THUNDERWAVE = "Thunderwave"


class SpellTypeEnum(Enum):
    FIRE = "fire"
    ICE = "ice"
    LIGHTNING = "lightning"
    EARTH = "earth"
    AIR = "air"
    WATER = "water"
    DARK = "dark"
    LIGHT = "light"
    ARCANE = "arcane"
    CHAOS = "chaos"


class EffectStatus(Enum):
    BURN = "burn"
    POISON = "poison"
    FROZEN = "frozen"
    STUN = "stun"
    SLEEP = "sleep"
    CONFUSE = "confuse"
    BLIND = "blind"
    PARALYZE = "paralyze"
    SILENCE = "silence"
    CURSE = "curse"
    DEATH = "death"
    FEAR = "fear"
    DISEASE = "disease"
    BLEED = "bleed"
    BLOODLUST = "bloodlust"
    CHILL = "chill"
    CRIPPLE = "cripple"
    NONE = "none"


class AbilityTargetEnum(Enum):
    SELF = "self"
    ENEMY = "enemy"
    ALLY = "ally"
    ALL = "all"


class AbilityTargetTypeEnum(Enum):
    SINGLE = "single"
    AREA = "area"


class EffectTypeEnum(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    STATUS = "status"
    BUFF = "buff"
    DEBUFF = "debuff"


class AbilityDescriptionEnum(Enum):
    FIREBALL = "Hurl a fiery ball of flame that explodes on impact, damaging all creatures in a small area."
    MAGIC_MISSILE = "Unleash a flurry of magical darts that strike your enemies unerringly."
    SHIELD = "Create a magical shield that blocks incoming attacks, providing temporary hit points."
    MAGE_ARMOR = "Create a magical suit of armor that increases your armor class for the duration of the spell."
    THUNDERWAVE = "Unleash a powerful blast of thunderous energy that damages enemies and pushes them back."
