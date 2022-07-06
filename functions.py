from random import randint

def roll_dice(number = 1, sides = 20):
    # returns a whole number (integer) between 1 and sides, N times
    # where N is the number of dice to roll
    sum_of_rolls = 0

    for i in range(0, number):
        sum_of_rolls += randint(1, sides)

    return sum_of_rolls

def roll_character(character_name):
    # returns a dictionary, keys are stats for my character (STR, WIS, etc.)
    # values will be numbers from 3 to 18 (3d6 - three six sided dice)

    new_character = {"name": character_name}

    new_character["STR"] = roll_dice(3, 6)
    new_character["CON"] = roll_dice(3, 6)
    new_character["DEX"] = roll_dice(3, 6)
    new_character["INT"] = roll_dice(3, 6)
    new_character["WIS"] = roll_dice(3, 6)
    new_character["CHA"] = roll_dice(3, 6)

    return new_character

def roll_character2(character_name):
    # returns a dictionary, keys are stats for my character (STR, WIS, etc.)
    # values will be numbers from 3 to 18 (3d6 - three six sided dice)

    new_character = {"name": character_name}

    stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    for stat in stats:
        new_character[stat] = roll_dice(3, 6)

    return new_character


print(roll_character2("Trogdor III"))