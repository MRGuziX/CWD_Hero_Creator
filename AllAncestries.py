import pandas as pd

from DiceRoller import dice_roller, DiceRoller

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

        hero.strength = int(df.iloc[1, 1])
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
        hero.languages_verbal = [df.iloc[14, 1]]
        hero.languages_written = [df.iloc[15, 1]]
        hero.character_size = None
        return hero

    def personality_picker(self):
        dice_result = dice_roller(3, 6)
        print(dice_result)
        data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Osobowość')
        df = pd.DataFrame(data, columns=['result', 'value'])

        match dice_result:
            case 3:
                return df.iloc[0, 1]
            case 4:
                return df.iloc[1, 1]
            case 5, 6:
                return df.iloc[2, 1]
            case 7, 8:
                return df.iloc[3, 1]
            case 9, 10, 11, 12:
                return df.iloc[4, 1]
            case 13, 14:
                return df.iloc[5, 1]
            case 15, 16:
                return df.iloc[6, 1]
            case 17:
                return df.iloc[7, 1]
            case 18:
                return df.iloc[8, 1]
