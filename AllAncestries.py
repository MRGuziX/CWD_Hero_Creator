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

        data = pd.read_excel(f'dataBase\{database_name}.xlsx', f'{database_name}')
        df = pd.DataFrame(data, columns=['attribute', 'value'])

        hero.strength = (df.iloc[1, 1])
        hero.dexterity = df.iloc[2, 1]
        hero.intelligence = df.iloc[3, 1]
        hero.will = df.iloc[4, 1]
        hero.perception = hero.intelligence
        hero.health = hero.strength
        hero.speed = df.iloc[7, 1]
        hero.defence = df.iloc[8, 1]
        hero.healing_rate = df.iloc[9, 1]
        hero.power = df.iloc[10, 1]
        hero.insanity = df.iloc[11, 1]
        hero.corruption = df.iloc[12, 1]
        hero.damage = df.iloc[13, 1]
        hero.character_size = None
        return hero

