import classes

def calculate_hp(character_level, hit_die_max, hit_die_avg, con_modifier):
    if character_level == 1:
        return hit_die_max + con_modifier
    else:
        # Level 1 HP + (levels after 1st * average per level)
        return (hit_die_max + con_modifier) + ((character_level - 1) * (hit_die_avg + con_modifier))
