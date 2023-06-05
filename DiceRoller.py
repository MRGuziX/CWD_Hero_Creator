import random


def dice_roller(amount_of_dice, type_of_dice):
    dice_result = [random.randint(1, type_of_dice) for _ in range(amount_of_dice)]
    return sum(dice_result)


class DiceRoller:
    pass
