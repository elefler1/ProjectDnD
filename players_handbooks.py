# This module defines the core traits, features, and progression tables for the classes in Dungeons & Dragons 5th Edition.
# The data is organized in a way that allows for easy access and reference when creating and leveling up characters.
# The module can be expanded to include additional classes, subclasses, and features as needed.


# Functions for choosing starting equipment and skill proficiencies for multiple classes.
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


# Define the classes and their traits, features, and progression tables.


classes = {
    'barbarian': {

        # Barbarian Core Traits:
        'core_traits': {
            'level': 1,
            'primary_ability': ['Strength'],
            'hit_die': '1d12',
            'saving_throws': ['Strength', 'Constitution'],
            'skill_proficiencies': ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'],
            'weapon_proficiencies': ['Simple Weapons', 'Martial Weapons'],
            'armor_training': ['Light Armor', 'Medium Armor', 'Shields'],
            'equipment': {
                'A': [('Greataxe', 1), 
                    ('Handaxes', 4), 
                    ('Explorer\'s Pack', 1), 
                    ('GP', 15)
                ],
                'B': [('GP', 75)
                ]
            }
        },

        # Barbarian Feature Table:
        'feature_tables': {
            1: {
                'proficiency_bonus': 2,
                'features': ['Rage', 'Unarmored Defense', 'Weapon Mastery'],
                'rages': 2,
                'rage_damage': 2,
                'weapon_mastery': 2
                },
            2: {
                'proficiency_bonus': 2,
                'features': ['Reckless Attack', 'Danger Sense'],
                'rages': 2,
                'rage_damage': 2,
                'weapon_mastery': 2
            },
            3: {
                'proficiency_bonus': 2,
                'features': ['Primal Knowledge', 'barbarian Subclass'],
                'rages': 3,
                'rage_damage': 2,
                'weapon_mastery': 2
            },
            4: {
                'proficiency_bonus': 2,
                'features': ['Ability Score Improvement'],
                'rages': 3,
                'rage_damage': 2,
                'weapon_mastery': 2
            },
            5: {
                'proficiency_bonus': 3,
                'features': ['Subclass Feature'],
                'rages': 3,
                'rage_damage': 2,
                'weapon_mastery': 3
            },
            6: {
                'proficiency_bonus': 3,
                'features': ['Subclass Feature'],
                'rages': 4,
                'rage_damage': 2,
                'weapon_mastery': 3
            },
            7: {
                'proficiency_bonus': 3,
                'features': ['Feral Instinct'],
                'rages': 4,
                'rage_damage': 2,
                'weapon_mastery': 3
            },
            8: {
                'proficiency_bonus': 3,
                'features': ['Ability Score Improvement'],
                'rages': 4,
                'rage_damage': 2,
                'weapon_mastery': 3
            },
            9: {
                'proficiency_bonus': 4,
                'features': ['Brutal Critical (1 die)'],
                'rages': 4,
                'rage_damage': 3,
                'weapon_mastery': 3
            },
            10: {
                'proficiency_bonus': 4,
                'features': ['Intimidating Presence'],
                'rages': 4,
                'rage_damage': 3,
                'weapon_mastery': 4
            },
            11: {
                'proficiency_bonus': 4,
                'features': ['Relentless Rage'],
                'rages': 4,
                'rage_damage': 3,
                'weapon_mastery': 4
            },
            12: {
                'proficiency_bonus': 4,
                'features': ['Ability Score Improvement'],
                'rages': 4,
                'rage_damage': 3,
                'weapon_mastery': 4
            },
            13: {
                'proficiency_bonus': 5,
                'features': ['Brutal Critical (2 dice)'],
                'rages': 5,
                'rage_damage': 3,
                'weapon_mastery': 4
            },
            14: {
                'proficiency_bonus': 5,
                'features': ['Retaliation'],
                'rages': 5,
                'rage_damage': 3,
                'weapon_mastery': 4
            },
            15: {
                'proficiency_bonus': 5,
                'features': ['Persistent Rage'],
                'rages': 5,
                'rage_damage': 4,
                'weapon_mastery': 4
            },
            16: {
                'proficiency_bonus': 5,
                'features': ['Ability Score Improvement'],
                'rages': 5,
                'rage_damage': 4,
                'weapon_mastery': 4
            },
            17: {
                'proficiency_bonus': 6,
                'features': ['Brutal Critical (3 dice)'],
                'rages': 6,
                'rage_damage': 4,
                'weapon_mastery': 4
            },
            18: {
                'proficiency_bonus': 6,
                'features': ['Indomitable Might'],
                'rages': 6,
                'rage_damage': 4,
                'weapon_mastery': 4
            },
            19: {
                'proficiency_bonus': 6,
                'features': ['Ability Score Improvement'],
                'rages': 6,
                'rage_damage': 4,
                'weapon_mastery': 4
            },
            20: {
                'proficiency_bonus': 6,
                'features': ['Primal Champion'],
                'rages': 6,
                'rage_damage': 4,
                'weapon_mastery': 4
            }
        }
    },

    'bard': {
        'core_traits': {
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
        },

        'feature_tables': {
            1: {
    }
}