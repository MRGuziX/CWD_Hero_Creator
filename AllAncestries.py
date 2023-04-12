import pandas as pd

from Builder_CWD_Hero import HeroBuilder
from DiceRoller import dice_roller, DiceRoller

dice_roller_instance = DiceRoller()
hero = HeroBuilder()


class AllAncestries:
    @staticmethod
    def database_picker(ancestry_choice):

        match ancestry_choice:
            case "Człowiek":
                database_name = "humanAncestry"
                return AllAncestries.attribute_picker(database_name)
            case "automaton":
                database_name = "automatonAncestry"
                return AllAncestries.attribute_picker(database_name)
            case "Goblin":
                database_name = "goblinAncestry"
                return AllAncestries.attribute_picker(database_name)
            case "Krasnolud":
                database_name = "krasnoludAncestry"
                return AllAncestries.attribute_picker(database_name)
            case "Odmieniec":
                database_name = "odmieniecAncestry"
                return AllAncestries.attribute_picker(database_name)
            case "Ork":
                database_name = "orkAncestry"
                return AllAncestries.attribute_picker(database_name)

    @staticmethod
    def attribute_picker(database_name):

        data = pd.read_excel(f'dataBase\{database_name}.xlsx', f'{database_name}')
        df = pd.DataFrame(data, columns=['attribute', 'value'])

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

        print("Siła Z bazy przypisana do zmiennej")
        print(strength)

        hero.strength = strength

        print("Siła przypisana do pola str obiektu hero")
        print(hero.strength)

        hero.dexterity = dexterity
        hero.intelligence = intelligence
        hero.will = will
        hero.perception = perception
        hero.health = health
        hero.speed = speed
        hero.defence = defence
        hero.healing_rate = healing_rate
        hero.power = power
        hero.insanity = insanity
        hero.corruption = corruption
        hero.damage = damage
        hero.languages_verbal = languages_verbal
        hero.languages_written = languages_written
        hero.character_size = character_size

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
