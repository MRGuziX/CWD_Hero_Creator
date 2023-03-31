import pandas as pd

from DiceRoller import dice_roller, DiceRoller
from FinalCharacter import FinalCharacter
from UpgradeMechanics import UpgradeMechanics

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

        # Pobranie statystyk  i przypisanie do zmiennych
        strength = df.iloc[1, 1]
        dexterity = df.iloc[2, 1]
        intelligence = df.iloc[3, 1]
        will = df.iloc[4, 1]
        perception = intelligence
        health = strength
        speed = df.iloc[7, 1]
        defence = df.iloc[8, 1]
        healing_rate = df.iloc[9, 1]
        power = df.iloc[10, 1]
        insanity = df.iloc[11, 1]
        corruption = df.iloc[12, 1]
        damage = df.iloc[13, 1]
        languages_verbal = [df.iloc[14, 1]]
        languages_written = [df.iloc[15, 1]]
        character_size = None

        UpgradeMechanics.statistic_increment()

        # przekazanie statystyk do obiektu bohatera
        final_character.strength = strength
        final_character.dexterity = dexterity
        final_character.intelligence = intelligence
        final_character.will = will
        final_character.perception = perception
        final_character.health = health
        final_character.speed = speed
        final_character.defence = defence
        final_character.healing_rate = healing_rate
        final_character.power = power
        final_character.insanity = insanity
        final_character.corruption = corruption
        final_character.damage = damage
        final_character.languages_verbal = languages_verbal
        final_character.languages_written = languages_written
        final_character.character_size = character_size



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
