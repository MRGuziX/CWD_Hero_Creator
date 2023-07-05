import pandas as pd

from DiceRoller import DiceRoller

dice_roller_instance = DiceRoller()


class AllAncestries:

    @staticmethod
    def attribute_picker(hero):

        match hero.ancestry:
            case "Człowiek":
                database_name = "humanAncestry"
            case "Automaton":
                database_name = "automatonAncestry"
            case "Goblin":
                database_name = "goblinAncestry"
            case "Krasnolud":
                database_name = "krasnoludAncestry"
            case "Odmieniec":
                database_name = "odmieniecAncestry"
            case "Ork":
                database_name = "orkAncestry"
            case _:
                return "Błąd"

        data = pd.read_excel(f'dataBase/{database_name}.xlsx', f'{database_name}')

        hero.strength = (data.iloc[0, 1])
        hero.dexterity = data.iloc[1, 1]
        hero.intelligence = data.iloc[2, 1]
        hero.will = data.iloc[3, 1]
        hero.perception = hero.intelligence
        hero.health = hero.strength
        hero.speed = data.iloc[6, 1]
        hero.defence = data.iloc[7, 1]
        hero.healing_rate = data.iloc[8, 1]
        hero.power = data.iloc[9, 1]
        hero.insanity = data.iloc[10, 1]
        hero.corruption = data.iloc[11, 1]
        hero.damage = data.iloc[12, 1]
        hero.character_size = data.iloc[15, 1]
        return hero
