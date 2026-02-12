import random
from collections import deque
import dice_library

# Dungeon Dice Game

# In this game, players choose a character class (Warrior, Mage, Ranger, Healer) and perform actions based on dice rolls. Each character class has unique actions and a backpack of items that can be used during the game.

# The game flow is as follows:
# 1. The player chooses a character class.
# 2. The player will choose an action based on their character class.
# 3. The player rolls a six-sided die to determine the outcome of their action.
# 4. The player can choose to use an item from their backpack after performing an action.
# 5. The game continues until the dungeon is cleared or the player decides to quit.

# Define backpacks for each character class
warrior_backpack = deque(['Sword', 'Shield', 'Health Potion'])
mage_backpack = deque(['Spell Book', 'Mana Potion', 'Magic Wand'])
ranger_backpack = deque(['Bow', 'Quiver of Arrows', 'Camouflage Cloak'])
healer_backpack = deque(['Healing Staff', 'Bandages', 'Holy Water'])

# Choose a character class
def choose_character():
    characters = ['Warrior', 'Mage', 'Ranger', 'Healer']
    print("Choose your character:")
    for idx, char in enumerate(characters, 1):
        print(f"{idx}. {char}")
    choice = int(input("Enter the number of your choice: "))
    return characters[choice - 1]

def perform_action(character):
    if character == 'Warrior':
        action = input("Choose an action (Attack, Defend, Berserk): ")
        while action not in warrior_actions:
            print("Invalid action. Please choose from Attack, Defend, or Berserk.")
            action = input("Choose an action (Attack, Defend, Berserk): ")
        if action == 'Attack':
            print("You swing your sword at the enemy!")
        elif action == 'Defend':
            print("You raise your shield to block incoming attacks!")
        elif action == 'Berserk':
            print("Berserk mode activated! You will take more damage but deal more damage.")
        backpack = warrior_backpack

    elif character == 'Mage':
        action = input("Choose an action (Cast Spell, Meditate, Summon): ")
        while action not in mage_actions:
            print("Invalid action. Please choose from Cast Spell, Meditate, or Summon.")
            action = input("Choose an action (Cast Spell, Meditate, Summon): ")
        if action == 'Cast Spell':
            print("You cast a powerful spell at the enemy!")
        elif action == 'Meditate':
            print("You meditate to restore your mana.")
        elif action == 'Summon':
            creature = random.choice(['Fire Elemental', 'Water Elemental', 'Earth Elemental'])
            print(f"You have summoned a {creature} to fight alongside you!")
        backpack = mage_backpack

    elif character == 'Ranger':
        action = input("Choose an action (Shoot Arrow, Set Trap, Dodge): ")
        while action not in ranger_actions:
            print("Invalid action. Please choose from Shoot Arrow, Set Trap, or Dodge.")
            action = input("Choose an action (Shoot Arrow, Set Trap, Dodge): ")
        if action == 'Shoot Arrow':
            print("You shoot an arrow at the enemy!")
        elif action == 'Set Trap':
            print("You set a trap for the enemy!")
        elif action == 'Dodge':
            print("You dodge the enemy's attack!")
        backpack = ranger_backpack

    else:
        action = input("Choose an action (Heal Ally, Protect, Revive): ")
        while action not in healer_actions:
            print("Invalid action. Please choose from Heal Ally, Protect, or Revive.")
            action = input("Choose an action (Heal Ally, Protect, Revive): ")
        if action == 'Heal Ally':
            print("You heal your ally!")
        elif action == 'Protect':
            print("You protect your ally from harm!")
        elif action == 'Revive':
            print("You revive a fallen ally!")
        backpack = healer_backpack
    return action, backpack, creature if character == 'Mage' and action == 'Summon' else None

def manage_backpack(backpack):
    choice = input("Do you want to use an item from your backpack? (y/n): ")
    if choice.lower() == 'y':
        print(f"Backpack items: {list(backpack)}")
        item = input("Enter the name of the item you want to use: ")
        if item in backpack:
            backpack.remove(item)
            print(f"You used {item} from your backpack.")
        else:
            print("Item not found in backpack.")

def main():
    character = choose_character()
    print(f"You have chosen: {character}")
    