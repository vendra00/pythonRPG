from model.game_enums import AbilityTypeEnum, SpellTitleEnum, AbilityTargetTypeEnum, EffectTypeEnum, AbilityTargetEnum, \
    SpellTypeEnum, EffectStatus, AbilityDescriptionEnum

barbarian = {
    "Reckless Attack": {
        "title": "Reckless Attack",
        "description": "When you make your first attack on your turn, you can decide to attack recklessly. Doing so "
                       "gives you advantage on melee weapon attack rolls using Strength during this turn, but attack "
                       "rolls against you have advantage until your next turn."
    },
    "Frenzy": {
        "title": "Frenzy",
        "description": "As a bonus action on your turn, you can enter a frenzy, giving you one additional attack on "
                       "each of your turns until the rage ends. When the rage ends, you suffer one level of exhaustion."
    },
    "Brutal Critical": {
        "title": "Brutal Critical",
        "description": "Beginning at 9th level, you can roll one additional weapon damage die when determining the "
                       "extra damage for a critical hit with a melee attack."
    },
    "Mindless Rage": {
        "title": "Mindless Rage",
        "description": "You can't be charmed or frightened while raging."
    },
    "Intimidating Presence": {
        "title": "Intimidating Presence",
        "description": "You can use your action to frighten someone with your menacing presence, forcing them to make "
                       "a Wisdom saving throw or become frightened of you until the end of your next turn."
    },
    "Danger Sense": {
        "title": "Danger Sense",
        "description": "You have advantage on Dexterity saving throws against effects that you can see, such as traps "
                       "and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated."
    },
    "Fast Movement": {
        "title": "Fast Movement",
        "description": "Your speed increases by 10 feet while you aren't wearing heavy armor."
    },
    "Rage Beyond Death": {
        "title": "Rage Beyond Death",
        "description": "When you are reduced to 0 hit points while raging and don't die outright, you can make a DC "
                       "10 Constitution saving throw. If you succeed, you drop to 1 hit point instead."
    },
    "Retaliation": {
        "title": "Retaliation",
        "description": "When you take damage from a creature within 5 feet of you, you can use your reaction to make "
                       "a melee weapon attack against that creature."
    },
    "Spirit Shield": {
        "title": "Spirit Shield",
        "description": "While raging, you can use your reaction to reduce the damage you or an ally within 30 feet of "
                       "you takes by 2d6."
    },
    # Add more abilities as needed
}

bard = {
    "Vicious Mockery": {
        "title": "Vicious Mockery",
        "description": "A bard can use witty insults to deal psychic damage to an opponent."
    },
    "Cutting Words": {
        "title": "Cutting Words",
        "description": "A bard can use their words to distract or demean an opponent, making them less effective in "
                       "combat."
    },
    "Bardic Inspiration": {
        "title": "Bardic Inspiration",
        "description": "A bard can inspire an ally, granting them a boost to their abilities for a short time."
    },
    "Countercharm": {
        "title": "Countercharm",
        "description": "A bard can use their music to protect allies from being charmed or frightened by enemies."
    },
    "Magical Secrets": {
        "title": "Magical Secrets",
        "description": "A bard can learn spells from any class, allowing them to fill in gaps in their own "
                       "spell casting abilities."
    },
    "Song of Rest": {
        "title": "Song of Rest",
        "description": "A bard can use a soothing melody to help allies recover from their wounds during a short rest."
    },
    "Expertise": {
        "title": "Expertise",
        "description": "A bard can become exceptionally skilled in a certain area, gaining double proficiency "
                       "in a skill or tool."
    },
    "College of Lore": {
        "title": "College of Lore",
        "description": "A bard can specialize in ancient knowledge and secrets, gaining access to unique spells and "
                       "abilities."
    },
    "Counter Spell": {
        "title": "Counter Spell",
        "description": "A bard can use their magical knowledge to counter an enemy spell."
    },
    "Dissonant Whispers": {
        "title": "Dissonant Whispers",
        "description": "A bard can use a haunting melody to deal psychic damage and force an opponent to flee."
    },
    # Add more abilities as needed
}

cleric = {
    "Turn Undead": {
        "title": "Turn Undead",
        "description": "Channel divinity to turn undead creatures within 30 feet of you."
    },
    "Healing Word": {
        "title": "Healing Word",
        "description": "A quick, one-word prayer that heals a nearby ally."
    },
    "Spiritual Weapon": {
        "title": "Spiritual Weapon",
        "description": "Create a weapon made of pure energy that attacks enemies from afar."
    },
    "Bless": {
        "title": "Bless",
        "description": "Confer divine favor upon a group of allies within 30 feet, granting them increased accuracy "
                       "and durability."
    },
    "Shield of Faith": {
        "title": "Shield of Faith",
        "description": "Surround an ally with a protective aura, increasing their armor class."
    },
    "Cure Wounds": {
        "title": "Cure Wounds",
        "description": "Lay your hands on a wounded ally to restore their health."
    },
    "Divine Favor": {
        "title": "Divine Favor",
        "description": "Call upon your deity to grant you divine favor, increasing your chances of hitting with "
                       "weapon attacks."
    },
    "Sacred Flame": {
        "title": "Sacred Flame",
        "description": "A column of radiant flame descends on an enemy within range, dealing damage and ignoring cover."
    },
    "Prayer of Healing": {
        "title": "Prayer of Healing",
        "description": "Recite a prayer that heals a group of allies within 30 feet of you."
    },
    "Guiding Bolt": {
        "title": "Guiding Bolt",
        "description": "A bolt of radiant energy streaks towards a target within range, dealing damage and granting "
                       "advantage to the next attack against the target."
    }
    # Add more abilities as needed
}

druid = {
    "Wild Shape": {
        "title": "Wild Shape",
        "description": "Transform into a variety of beasts and gain their abilities and characteristics."
    },
    "Moonbeam": {
        "title": "Moonbeam",
        "description": "Create a beam of moonlight that damages enemies within its area of effect."
    },
    "Entangle": {
        "title": "Entangle",
        "description": "Cause plants to grow and entangle enemies, restraining them in place."
    },
    "Flame Blade": {
        "title": "Flame Blade",
        "description": "Summon a sword of fire that deals fire damage to enemies."
    },
    "Speak with Animals": {
        "title": "Speak with Animals",
        "description": "Communicate with animals and gain insight into their behavior and motivations."
    },
    "Thunderwave": {
        "title": "Thunderwave",
        "description": "Create a powerful blast of sound that damages enemies and pushes them away."
    },
    "Giant Insect": {
        "title": "Giant Insect",
        "description": "Transform into a giant insect and gain its abilities and characteristics."
    },
    "Goodberry": {
        "title": "Goodberry",
        "description": "Create a handful of magical berries that restore health when eaten."
    },
    "Call Lightning": {
        "title": "Call Lightning",
        "description": "Summon a bolt of lightning to strike enemies within its area of effect."
    },
    "Pass Without Trace": {
        "title": "Pass Without Trace",
        "description": "Mask your presence and the presence of your allies, making it difficult for enemies to track "
                       "you."
    }
    # Add more abilities as needed
}

fighter = {
    "Second Wind": {
        "title": "Second Wind",
        "description": "Use a bonus action to regain some of your lost hit points."
    },
    "Action Surge": {
        "title": "Action Surge",
        "description": "Take an additional action on your turn."
    },
    "Indomitable": {
        "title": "Indomitable",
        "description": "Reroll a failed saving throw."
    },
    "Extra Attack": {
        "title": "Extra Attack",
        "description": "Make an additional attack when you take the Attack action."
    },
    "Martial Archetype": {
        "title": "Martial Archetype",
        "description": "Choose a subclass that specializes in a particular type of combat."
    },
    "Combat Superiority": {
        "title": "Combat Superiority",
        "description": "Gain a pool of dice that you can use to add to your attack or damage rolls."
    },
    "Defensive Duelist": {
        "title": "Defensive Duelist",
        "description": "Use your reaction to increase your armor class against one melee attack."
    },
    "Rally": {
        "title": "Rally",
        "description": "Use a bonus action to inspire an ally, giving them temporary hit points."
    },
    "Riposte": {
        "title": "Riposte",
        "description": "Use your reaction to make an attack against a creature that misses you in melee combat."
    },
    "Whirlwind Attack": {
        "title": "Whirlwind Attack",
        "description": "Make melee attacks against all creatures within 5 feet of you."
    }
    # Add more abilities as needed
}

monk = {
    "Flurry of Blows": {
        "title": "Flurry of Blows",
        "description": "Spend a ki point to make two unarmed strikes as a bonus action after taking the Attack action."
    },
    "Patient Defense": {
        "title": "Patient Defense",
        "description": "Spend a ki point to take the Dodge action as a bonus action on your turn."
    },
    "Step of the Wind": {
        "title": "Step of the Wind",
        "description": "Spend a ki point to take the Disengage or Dash action as a bonus action on your turn, and "
                       "your jump distance is doubled for the turn."
    },
    "Stunning Strike": {
        "title": "Stunning Strike",
        "description": "Spend a ki point to attempt to stun a target you hit with a melee weapon attack."
    },
    "Deflect Missiles": {
        "title": "Deflect Missiles",
        "description": "Use your reaction to deflect or catch a missile or thrown weapon when you are hit by a ranged "
                       "weapon attack."
    },
    "Ki-Empowered Strikes": {
        "title": "Ki-Empowered Strikes",
        "description": "Your unarmed strikes count as magical for the purpose of overcoming resistance and immunity "
                       "to nonmagical attacks and damage."
    },
    "Slow Fall": {
        "title": "Slow Fall",
        "description": "Use your reaction when you fall to reduce any falling damage you take by an amount equal to "
                       "five times your monk level."
    },
    "Unarmored Movement": {
        "title": "Unarmored Movement",
        "description": "Your speed increases by 10 feet while you are not wearing armor or wielding a shield."
    },
    "Defensive Duelist": {
        "title": "Defensive Duelist",
        "description": "Use your reaction to increase your armor class against one melee attack that would hit you."
    },
    "Evasion": {
        "title": "Evasion",
        "description": "When you are subjected to an effect that allows you to make a Dexterity saving throw to take "
                       "only half damage, you instead take no damage if you succeed on the saving throw, and only "
                       "half damage if you fail."
    }
    # Add more abilities as needed
}

paladin = {
    "Lay on Hands": {
        "title": "Lay on Hands",
        "description": "Restore hit points equal to your paladin level."
    },
    "Divine Smite": {
        "title": "Divine Smite",
        "description": "When you hit a creature with a melee weapon attack, expend one spell slot to deal "
                       "additional radiant damage to the target, in addition to the weapon's damage."
    },
    "Aura of Protection": {
        "title": "Aura of Protection",
        "description": "You and friendly creatures within 10 feet of you can't be charmed while you are conscious."
    },
    "Cleansing Touch": {
        "title": "Cleansing Touch",
        "description": "As an action, you can end one spell on yourself or on one willing creature within 5 feet that "
                       "you touch."
    },
    "Aura of Courage": {
        "title": "Aura of Courage",
        "description": "You and friendly creatures within 10 feet of you can't be frightened while you are conscious."
    },
    "Branding Smite": {
        "title": "Branding Smite",
        "description": "Attacks deal extra damage and the target sheds light."
    },
    "Crusader's Mantle": {
        "title": "Crusader's Mantle",
        "description": "You can use your action to end one spell on yourself or on one willing creature within 5 feet "
                       "that you touch."
    },
    "Searing Smite": {
        "title": "Searing Smite",
        "description": "Attacks deal extra fire damage and ignite the target."
    },
    "Aura of Life": {
        "title": "Aura of Life",
        "description": "Allies within 30 feet cannot be reduced to 0 hit points."
    },
    "Find Steed": {
        "title": "Find Steed",
        "description": "Summon a spirit mount to serve as a loyal companion."
    }
    # Add more abilities as needed
}

ranger = {
    "Favored Enemy": {
        "title": "Favored Enemy",
        "description": "Choose a type of creature as your favored enemy, gaining bonuses when fighting against them."
    },
    "Natural Explorer": {
        "title": "Natural Explorer",
        "description": "Gain bonuses when exploring the wilderness, including faster travel and better tracking "
                       "ability."
    },
    "Hunter's Mark": {
        "title": "Hunter's Mark",
        "description": "Mark an enemy as your quarry, gaining bonuses when attacking them and better tracking ability."
    },
    "Colossus Slayer": {
        "title": "Colossus Slayer",
        "description": "When you hit a wounded enemy with a weapon attack, deal additional damage."
    },
    "Multiattack": {
        "title": "Multiattack",
        "description": "Make two weapon attacks as part of the same action."
    },
    "Hide in Plain Sight": {
        "title": "Hide in Plain Sight",
        "description": "Become proficient at hiding in natural terrain, even when being observed."
    },
    "Whirlwind Attack": {
        "title": "Whirlwind Attack",
        "description": "Spend an action to make a melee attack against all enemies within 5 feet of you."
    },
    "Escape the Horde": {
        "title": "Escape the Horde",
        "description": "Use your reaction to move up to half your speed without provoking opportunity attacks."
    },
    "Volley": {
        "title": "Volley",
        "description": "Spend an action to make a ranged attack against all enemies within a 10-foot radius."
    },
    "Evasion": {
        "title": "Evasion",
        "description": "Take no damage when succeeding on a Dexterity saving throw against an effect that deals half "
                       "damage on a successful save."
    }
    # Add more abilities as needed
}

rogue = {
    "Sneak Attack": {
        "title": "Sneak Attack",
        "description": "Deal extra damage when you hit an enemy who has not yet acted in combat, or when you have "
                       "advantage on the attack roll."
    },
    "Cunning Action": {
        "title": "Cunning Action",
        "description": "Use a bonus action to Dash, Disengage, or Hide."
    },
    "Evasion": {
        "title": "Evasion",
        "description": "Take no damage from an area of effect attack if you succeed on a Dexterity saving throw, and "
                       "take half damage if you fail."
    },
    "Uncanny Dodge": {
        "title": "Uncanny Dodge",
        "description": "Halve damage from an attack you can see."
    },
    "Expertise": {
        "title": "Expertise",
        "description": "Double your proficiency bonus on certain ability checks."
    },
    "Thieves' Cant": {
        "title": "Thieves' Cant",
        "description": "A secret language used by rogues to communicate with each other."
    },
    "Sneak Thief": {
        "title": "Sneak Thief",
        "description": "Use a bonus action to attempt to pickpocket a creature within 5 feet of you."
    },
    "Criminal Contact": {
        "title": "Criminal Contact",
        "description": "You have a reliable and trustworthy contact within the criminal underworld."
    },
    "Fast Hands": {
        "title": "Fast Hands",
        "description": "Use a bonus action to use an object, such as picking a lock or disarming a trap."
    },
    "Stroke of Luck": {
        "title": "Stroke of Luck",
        "description": "Change a failed ability check, attack roll, or saving throw to a success."
    }
    # Add more abilities as needed
}

sorcerer = {
    "Chaos Bolt": {
        "title": "Chaos Bolt",
        "description": "Hurl an elemental bolt of chaos at a target, dealing damage of a random elemental type."
    },
    "Charm Person": {
        "title": "Charm Person",
        "description": "Attempt to charm a humanoid creature within range, making them friendly towards you."
    },
    "Fireball": {
        "title": "Fireball",
        "description": "Create a ball of fire that explodes on impact, damaging all creatures in a 20-foot radius."
    },
    "Magic Missile": {
        "title": "Magic Missile",
        "description": "Unleash a volley of magical missiles that seek out targets and deal force damage."
    },
    "Thunderwave": {
        "title": "Thunderwave",
        "description": "Create a wave of thunderous force that damages all creatures within 15 feet of you."
    },
    "Fly": {
        "title": "Fly",
        "description": "Grant yourself or a willing creature the ability to fly for a limited time."
    },
    "Invisibility": {
        "title": "Invisibility",
        "description": "Render yourself or a willing creature invisible for a limited time."
    },
    "Mage Armor": {
        "title": "Mage Armor",
        "description": "Surround yourself with magical energy, granting you extra protection from physical attacks."
    },
    "Ray of Frost": {
        "title": "Ray of Frost",
        "description": "Fire a beam of freezing energy at a target, dealing cold damage and slowing their movement."
    },
    "Shield": {
        "title": "Shield",
        "description": "Summon a magical shield that absorbs incoming attacks, granting you extra protection."
    },
    # Add more abilities as needed
}

warlock = {
    "Eldritch Blast": {
        "title": "Eldritch Blast",
        "description": "A beam of crackling energy that deals damage to a target."
    },
    "Hex": {
        "title": "Hex",
        "description": "Curse a creature to weaken it and deal additional damage to it."
    },
    "Darkness": {
        "title": "Darkness",
        "description": "Magically darken an area, making it difficult for creatures to see and attack."
    },
    "Hellish Rebuke": {
        "title": "Hellish Rebuke",
        "description": "Unleash a fiery blast in retaliation against a creature that has attacked you."
    },
    "Armor of Agathys": {
        "title": "Armor of Agathys",
        "description": "Surround yourself with a protective layer of icy armor that damages attackers."
    },
    "Misty Step": {
        "title": "Misty Step",
        "description": "Teleport up to 30 feet away to a location you can see."
    },
    "Shadow Blade": {
        "title": "Shadow Blade",
        "description": "Create a weapon made of solidified darkness that deals extra damage."
    },
    "Devil's Sight": {
        "title": "Devil's Sight",
        "description": "See perfectly in complete darkness, including magical darkness."
    },
    "Summon Lesser Demons": {
        "title": "Summon Lesser Demons",
        "description": "Summon a horde of lesser demons to do your bidding, but be prepared to face the consequences."
    },
    "Charm Person": {
        "title": "Charm Person",
        "description": "Make a humanoid creature see you as a friendly acquaintance, gaining their trust and "
                       "cooperation."
    }
    # Add more abilities as needed
}

wizard = {
    SpellTitleEnum.MAGIC_MISSILE.value: {
        "title": SpellTitleEnum.MAGIC_MISSILE.value,
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.ENEMY.value,
        "mana_cost": 10,
        "stamina_cost": 5,
        "type": SpellTypeEnum.ARCANE.value,
        "target": AbilityTargetTypeEnum.SINGLE.value,
        "effect_type": EffectTypeEnum.DAMAGE.value,
        "effect_status": EffectStatus.NONE.value,
        "effect_value": 12,
        "description": AbilityDescriptionEnum.MAGIC_MISSILE.value
    },
    SpellTitleEnum.FIREBALL.value: {
        "title": SpellTitleEnum.FIREBALL.value,
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.ENEMY.value,
        "mana_cost": 20,
        "stamina_cost": 5,
        "type": SpellTypeEnum.FIRE.value,
        "target": AbilityTargetTypeEnum.AREA.value,
        "effect_type": EffectTypeEnum.DAMAGE.value,
        "effect_status": EffectStatus.BURN.value,
        "effect_value": 200,
        "description": AbilityDescriptionEnum.FIREBALL.value
    },
    SpellTitleEnum.SHIELD.value: {
        "title": SpellTitleEnum.SHIELD.value,
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.SELF.value,
        "mana_cost": 10,
        "stamina_cost": 0,
        "type": SpellTypeEnum.ARCANE.value,
        "target": AbilityTargetTypeEnum.SINGLE.value,
        "effect_type": EffectTypeEnum.STATUS.value,
        "effect_status": EffectStatus.NONE.value,
        "effect_value": 30,
        "description": AbilityDescriptionEnum.SHIELD.value
    },
    SpellTitleEnum.MAGE_ARMOR.value: {
        "title": SpellTitleEnum.MAGE_ARMOR.value,
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.SELF.value,
        "mana_cost": 10,
        "stamina_cost": 0,
        "type": SpellTypeEnum.ARCANE.value,
        "target": AbilityTargetTypeEnum.SINGLE.value,
        "effect_type": EffectTypeEnum.STATUS.value,
        "effect_status": EffectStatus.NONE.value,
        "effect_value": 100,
        "description": AbilityDescriptionEnum.MAGE_ARMOR.value
    },
    SpellTitleEnum.THUNDERWAVE.value: {
        "title": SpellTitleEnum.THUNDERWAVE.value,
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.ENEMY.value,
        "mana_cost": 35,
        "stamina_cost": 0,
        "type": SpellTypeEnum.LIGHTNING.value,
        "target": AbilityTargetTypeEnum.AREA.value,
        "effect_type": EffectTypeEnum.DAMAGE.value,
        "effect_status": EffectStatus.PARALYZE.value,
        "effect_value": 40,
        "description": AbilityDescriptionEnum.THUNDERWAVE.value
    },
    "Mage Hand": {
        "title": "Mage Hand",
        "ability_type": AbilityTypeEnum.SPELL.value,
        "ability_target": AbilityTargetEnum.ENEMY.value,
        "mana_cost": 35,
        "stamina_cost": 0,
        "type": SpellTypeEnum.LIGHTNING.value,
        "target": AbilityTargetTypeEnum.AREA.value,
        "effect_type": EffectTypeEnum.DAMAGE.value,
        "effect_status": EffectStatus.PARALYZE.value,
        "effect_value": 40,
        "description": "Create an invisible hand that can manipulate objects at a distance."
    },
    "Charm Person": {
        "title": "Charm Person",
        "mana_cost": 30,
        "description": "Temporarily charm a humanoid creature, making them friendly towards you."
    },
    "Identify": {
        "title": "Identify",
        "mana_cost": 5,
        "description": "Learn the magical properties of a single item or creature."
    },
    "Sleep": {
        "title": "Sleep",
        "mana_cost": 20,
        "description": "Cause creatures within an area to fall into a magical slumber, rendering them unconscious."
    },
    "Levitate": {
        "title": "Levitate",
        "mana_cost": 15,
        "description": "Cause a creature or object to levitate in the air, allowing it to move freely."
    }
}
