import pandas as pd

from DiceRoller import dice_roller, DiceRoller
from FinalCharacter import FinalCharacter

dice_roller_instance = DiceRoller()
final_character = FinalCharacter()


class AllAncestries:
    @staticmethod
    def ancestry_investigator(chosen_ancestry):

        match chosen_ancestry:
            case "człowiek":
                database_name = "humanAncestry"
                return AllAncestries.attribute_show(database_name)
            case "automaton":
                database_name = "automatonAncestry"
                return AllAncestries.attribute_show(database_name)
            case "goblin":
                database_name = "goblinAncestry"
                return AllAncestries.attribute_show(database_name)
            case "krasnolud":
                database_name = "krasnoludAncestry"
                return AllAncestries.attribute_show(database_name)
            case "odmieniec":
                database_name = "odmieniecAncestry"
                return AllAncestries.attribute_show(database_name)
            case "ork":
                database_name = "orkAncestry"
                return AllAncestries.attribute_show(database_name)  # Zwróci zwrócenie z Atribute show

    @staticmethod
    def attribute_show(database_name):

        data = pd.read_excel(f'dataBase\{database_name}.xlsx', f'{database_name}')
        df = pd.DataFrame(data, columns=['attribute', 'value'])

        final_character.strength = df.iloc[1, 1]
        final_character.dexterity = df.iloc[2, 1]
        final_character.intelligence = df.iloc[3, 1]
        final_character.will = df.iloc[4, 1]
        final_character.perception = df.iloc[3, 1]
        final_character.health = df.iloc[1, 1]
        final_character.speed = df.iloc[7, 1]
        final_character.defence = df.iloc[8, 1]
        final_character.healing_rate = df.iloc[9, 1]
        final_character.power = df.iloc[10, 1]
        final_character.insanity = df.iloc[11, 1]
        final_character.corruption = df.iloc[12, 1]
        final_character.damage = df.iloc[13, 1]
        final_character.languages_verbal = [df.iloc[14, 1]]
        final_character.languages_written = [df.iloc[15, 1]]
        final_character.character_size = None

        print('Statystyki:\n\n')
        print(final_character.name)

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
