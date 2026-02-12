# Define character classes and their actions

musical_instruments = ['Lute', 'Flute', 'Drum', 'Horn', 'Pan Flute', 'Shawm', 'Viol']
artisans_tools = ['Alchemist\'s Supplies', 'Brewer\'s Supplies', 'Calligrapher\'s Supplies', 'Carpenter\'s Tools', 'Cartographer\'s Tools', 'Cobbler\'s Tools', 'Cook\'s Utensils', 'Glassblower\'s Tools', 'Jeweler\'s Tools', 'Leatherworker\'s Tools', 'Mason\'s Tools', 'Painter\'s Supplies', 'Potter\'s Tools', 'Smith\'s Tools', 'Tinker\'s Tools', 'Weaver\'s Tools', 'Woodcarver\'s Tools']
skill_proficiencies = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival']


def choose_item():
    print("Choose a type of item:")
    print("1. Artisan's Tools")
    print("2. Musical Instrument")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        print("Choose an artisan's tool:")
        for idx, tool in enumerate(artisans_tools, 1):
            print(f"{idx}. {tool}")
        tool_choice = int(input("Enter the number of your choice: "))
        print(f"\n'{artisans_tools[tool_choice - 1]}' has been added to your inventory.")
        item_choice = artisans_tools[tool_choice - 1]
        return item_choice
    elif choice == 2:
        print("Choose a musical instrument:")
    for idx, instrument in enumerate(musical_instruments, 1):
        print(f"{idx}. {instrument}")
    choice = int(input("Enter the number of your choice: "))
    print(f"\nThe '{musical_instruments[choice - 1]}' has been added to your inventory.")
    item_choice = musical_instruments[choice - 1]
    return item_choice

def choose_skill_proficiency(skill_proficiencies, choices):
    num_proficiencies = choices
    skill_choices = []
    for skill in range(num_proficiencies):
        print("\nChoose a skill proficiency:")
        for idx, skill in enumerate(skill_proficiencies, 1):
            print(f"{idx}. {skill}")
        choice = int(input("Enter the number of your choice: "))
        print(f"\n'{skill_proficiencies[choice - 1]}' has been added to your character sheet.")
        skill_choices.append(skill_proficiencies[choice - 1])
    return skill_choices



# Character Classes:

# Barbarian Class:



# Bard Class:

bard = {
    'level': 1,
    'primary_ability': ['Charisma'],
    'hit_die': '1d8',
    'saving_throws': ['Dexterity', 'Charisma'],
    'skill_proficiencies': choose_skill_proficiency(skill_proficiencies, 3),
    'weapon_proficiencies': ['Simple Weapons'],
    'tool_proficiencies': ['Lute', 'Flute', 'Drum', 'Horn', 'Pan Flute', 'Shawm', 'Viol'],
    'armor_training': ['Light Armor'],
    'equipment': {
        'A': [('Leather Armor', 1), 
              ('Dagger', 2), 
              ('Entertainer\'s Pack', 1), 
              ('GP', 19)
        ],
        'B': [('GP', 90)
        ]
    }
}


# Cleric Class:

cleric = {
    'level': 1,
    'primary_ability': ['Wisdom'],
    'hit_die': '1d8',
    'saving_throws': ['Wisdom', 'Charisma'],
    'skill_proficiencies': ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
    'weapon_proficiencies': ['Simple Weapons'],
    'armor_training': ['Light Armor', 'Medium Armor', 'Shields'],
    'weapon_proficiencies': ['Simple Weapons'],
    'armor_training': ['Light Armor', 'Medium Armor', 'Shields'],
    'equipment': {
        'A': [('Chain Shirt', 1),
              ('Shield', 1),
              ('Mace', 1),
              ('Holy Symbol', 1),
              ('Priest\'s Pack', 1),
              ('GP', 7)
        ],
        'B': [('GP', 110)
        ]
    }
}

# Druid Class:

druid = {
    'level': 1,
    'primary_ability': ['Wisdom'],
    'hit_die': '1d8',
    'saving_throws': ['Intelligence', 'Wisdom'],
    'skill_proficiencies': ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'],
    'weapon_proficiencies': ['Simple Weapons'],
    'tool_proficiencies': ['Herbalism Kit'],
    'armor_training': ['Light Armor', 'Shields'],
    'equipment': {
        'A': [('Leather Armor', 1), 
              ('Shield', 1), 
              ('Druidic Focus (Quarterstaff)', 1), 
              ('Explorer\'s Pack', 1),
              ('Herbalism Kit', 1),
              ('GP', 9)
        ],
        'B': [('GP', 50)
        ]
    }
}


# Fighter Class:
    
fighter = {
    'level': 1,
    'primary_ability': ['Strength', 'Dexterity'],
    'hit_die': '1d10',
    'saving_throws': ['Strength', 'Constitution'],
    'skill_proficiencies': ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Persuasion', 'Perception', 'Survival'],
    'weapon_proficiencies': ['Simple Weapons', 'Martial Weapons'],
    'armor_training': ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields'],
    'equipment': {
        'A': [('Chain Mail', 1), 
              ('Greatsword', 1), 
              ('Flail', 1), 
              ('8 Javelins', 8), 
              ('Dungeoneer\'s Pack', 1), 
              ('GP', 4)
        ],
        'B': [('Studded Leather Armor', 1), 
              ('Scimitar', 1), 
              ('Shortsword', 1), 
              ('Longbow', 1), 
              ('20 Arrows', 20), 
              ('Quiver', 1), 
              ('Dungeoneer\'s Pack', 1), 
              ('GP', 11)
        ],
        'C': [('GP', 155)
        ]
    }
}

# Monk Class:

monk = {
    'level': 1,
    'primary_ability': ['Dexterity', 'Wisdom'],
    'hit_die': '1d8',
    'saving_throws': ['Strength', 'Dexterity'],
    'skill_proficiencies': ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],
    'weapon_proficiencies': ['Simple Weapons with Light property', 'Martial Weapons with Light property'],
    'tool_proficiencies': ['Artisan\'s Tools (Choose one)', 'Musical Instrument (Choose one)'],
    'armor_training': ['None'],
    'equipment': {
        'A': [('Spear', 1),
              ('Dagger', 5),
              (choose_item(), 1),
              ('Explorer\'s Pack', 1),
              ('GP', 11)
        ],
        'B': [('GP', 50)
        ]
    }
}


# Paladin Class:

paladin = {
    'level': 1,
    'primary_ability': ['Strength', 'Charisma'],
    'hit_die': '1d10',
    'saving_throws': ['Wisdom', 'Charisma'],
    'skill_proficiencies': ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
    'weapon_proficiencies': ['Simple Weapons', 'Martial Weapons'],
    'armor_training': ['Medium Armor', 'Heavy Armor', 'Shields'],
    'equipment': {
        'A': [('Chain Mail', 1), 
              ('Shield', 1), 
              ('Longsword', 1), 
              ('Javelins', 6),
              ('Holy Symbol', 1),
              ('Priest\'s Pack', 1), 
              ('GP', 9)
        ],
        'B': [('GP', 150)
        ]
    }
}

# Ranger Class:

ranger = {
    'level': 1,
    'primary_ability': ['Dexterity', 'Wisdom'],
    'hit_die': '1d10',
    'saving_throws': ['Strength', 'Dexterity'],
    'skill_proficiencies': ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'],
    'weapon_proficiencies': ['Simple Weapons', 'Martial Weapons'],
    'armor_training': ['Light Armor', 'Medium Armor', 'Shields'],
    'equipment': {
        'A': [('Studded Leather Armor', 1),
              ('Scimitar', 1),
              ('Shortsword', 1),
              ('Longbow', 1),
              ('20 Arrows', 20),
              ('Quiver', 1),
              ('Druidic Focus (sprig of mistletoe)', 1),
              ('Explorer\'s Pack', 1),
              ('GP', 7)
        ],
        'B': [('GP', 150)
        ]
    }
}

# Rogue Class:

rogue = {
    'level': 1,
    'primary_ability': ['Dexterity'],
    'hit_die': '1d8',
    'saving_throws': ['Dexterity', 'Intelligence'],
    'skill_proficiencies': [choose_skill_proficiency(skill_proficiencies, 4)],
    'weapon_proficiencies': ['Simple Weapons', 'Martial Weapons with Finesse or Light property'],
    'tool_proficiencies': ['Thieves\' Tools'],
    'armor_training': ['Light Armor'],
    'equipment': {
        'A': [('Leather Armor', 1),
              ('Dagger', 2),
              ('Shortsword', 1),
              ('Shortbow', 1),
              ('20 Arrows', 20),
              ('Quiver', 1),
              ('Burglar\'s Pack', 1),
              ('Thieves\' Tools', 1),
              ('GP', 8)
        ],
        'B': [('GP', 100)
        ]
    }
}

# Sorcerer Class:

sorcerer = {
    'level': 1,
    'primary_ability': ['Charisma'],
    'hit_die': '1d6',
    'saving_throws': ['Constitution', 'Charisma'],
    'skill_proficiencies': [choose_skill_proficiency(skill_proficiencies, 2)],
    'weapon_proficiencies': ['Simple Weapons'],
    'armor_training': ['None'],
    'equipment': {
        'A': [('Spear', 1),
              ('Dagger', 2),
              ('Arcane Focus (Crystal)', 1),
              ('Dungeoneer\'s Pack', 1),
              ('GP', 28)
        ],
        'B': [('GP', 50)
        ]
    }
}

# Warlock Class:

warlock = {
    'level': 1,
    'primary_ability': ['Charisma'],
    'hit_die': '1d8',
    'saving_throws': ['Wisdom', 'Charisma'],
    'skill_proficiencies': [choose_skill_proficiency(skill_proficiencies, 2)],
    'weapon_proficiencies': ['Simple Weapons'],
    'armor_training': ['Light Armor'],
    'equipment': {
        'A': [('Leather Armor', 1),
              ('Sickle', 1),
              ('Dagger', 2),
              ('Arcane Focus (orb)', 1),
              ('Book (occult lore)', 1),
              ('Scholar\'s Pack', 1),
              ('GP', 15)
        ],
        'B': [('GP', 100)
        ]
    }
}

# Wizard Class:

wizard = {
    'level': 1,
    'primary_ability': ['Intelligence'],
    'hit_die': '1d6',
    'saving_throws': ['Intelligence', 'Wisdom'],
    'skill_proficiencies': [choose_skill_proficiency(skill_proficiencies, 2)],
    'weapon_proficiencies': ['Simple Weapons'],
    'armor_training': ['None'],
    'equipment': {
        'A': [('Dagger', 2),
              ('Arcane Focus (Quarterstaff)', 1),
              ('Robe', 1),
              ('Spellbook', 1),
              ('Scholar\'s Pack', 1),
              ('GP', 5)
        ],
        'B': [('GP', 55)
        ]
    }
}