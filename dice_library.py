import random

# Roll a d20 to determine if you hit your target.
def attack_die():
    return random.randint(1, 20)

# Damage dice rolls:

# Roll a d4 to determine the amount of damage dealt with Daggers, Light Crossbows, and Small Spells.
def roll_d4():
    return random.randint(1, 4)
# Roll a d6 to determine the amount of damage dealt with Shortswords, Shortbows, Scimitars, and Fireball.
def roll_d6():
    return random.randint(1, 6)
# Roll a d8 to determine the amount of damage dealt with Longswords, Rapiers, and other medium weapons.
def roll_d8():
    return random.randint(1, 8)
# Roll a d10 to determine the amount of damage dealt with Heavy Crossbows, Glaives, and Fire Bolt.
def roll_d10():
    return random.randint(1, 10)
# Roll a d12 to determine the amount of damage dealt with Greataxes and high damage spells.
def roll_attack_d12(level):
    total = 0
    for _ in range(level):
        total += random.randint(1, 12)
    return total
# Roll a 2d6 to determine the amount of damage dealt with Greatswords and Mauls.
def roll_2d6():
    return random.randint(1, 6) + random.randint(1, 6)

# Skill Checks:
# Roll a d20 and add your character's skill modifier to determine if you succeed in a skill check.
def skill_check(modifier):
    return random.randint(1, 20) + modifier

# Saving Throws:

# Stength Save:
# Roll a d20 and add your character's strength saving throw modifier to determine if you succeed in a strength saving throw.
def strength_save(modifier):
    return random.randint(1, 20) + modifier

# Constitution Save:
# Roll a d20 and add your character's constitution saving throw modifier to determine if you succeed in a constitution saving throw.
def constitution_save(modifier):
    return random.randint(1, 20) + modifier


# Roll a d20 and add your character's saving throw modifier to determine if you succeed in a saving throw.
def saving_throw(modifier):
    return random.randint(1, 20) + modifier

# Initiative Rolls:
# Roll a d20 and add your character's initiative modifier to determine the order of actions in combat.
def initiative_roll(modifier):
    return random.randint(1, 20) + modifier

# Charisma Checks:
# Roll a d20 and add your character's charisma modifier to determine the success of social interactions.
def charisma_check(modifier):
    return random.randint(1, 20) + modifier

# Critical Hits:
# If you roll a natural 20 on an attack die, you score a critical hit, which allows you to roll additional damage dice.
def critical_hit(damage_die_function, modifier=0):
    if attack_die() == 20:
        return damage_die_function() + damage_die_function() + modifier  # Roll the damage die twice for a critical hit and add modifier
    else:
        return damage_die_function()