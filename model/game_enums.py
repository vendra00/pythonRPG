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
    MAGE_HAND = "Mage hand"
    CHARM_PERSON = "Charm person"
    IDENTIFY = "Identify"
    SLEEP = "Sleep"
    LEVITATE = "Levitate"


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
    COMMON = "Common"


class EffectStatusEnum(Enum):
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
    INANIMATE = "inanimate"
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
    NONE = "none"


class AbilityDescriptionEnum(Enum):
    FIREBALL_DESCRIPTION = "Hurl a fiery ball of flame that explodes on impact, damaging all creatures in a small area."
    MAGIC_MISSILE_DESCRIPTION = "Unleash a flurry of magical darts that strike your enemies unerringly."
    SHIELD_DESCRIPTION = "Create a magical shield that blocks incoming attacks, providing temporary hit points."
    MAGE_ARMOR_DESCRIPTION = "Create a magical suit of armor that increases your armor class for the duration of the " \
                             "spell."
    THUNDERWAVE_DESCRIPTION = "Unleash a powerful blast of thunderous energy that damages enemies and pushes them back."
    MAGE_HAND_DESCRIPTION = "Create an invisible hand that can manipulate objects at a distance."
    CHARM_PERSON_DESCRIPTION = "Temporarily charm a humanoid creature, making them friendly towards you."
    INDENTIFY_DESCRIPTION = "Learn the magical properties of a single item or creature."
    SLEEP_DESCRIPTION = "Cause creatures within an area to fall into a magical slumber, rendering them unconscious."
    LEVITATE_DESCRIPTION = "Cause a creature or object to levitate in the air, allowing it to move freely."


class AbilityStructureEnum(Enum):
    TITLE = "title"
    ABILITY_TYPE = "ability_type"
    ABILITY_TARGET = "ability_target"
    MANA_COST = "mana_cost"
    STAMINA_COST = "stamina_cost"
    TYPE = "type"
    TARGET = "target"
    EFFECT_TYPE = "effect_type"
    EFFECT_STATUS = "effect_status"
    EFFECT_VALUE = "effect_value"
    DESCRIPTION = "description"
