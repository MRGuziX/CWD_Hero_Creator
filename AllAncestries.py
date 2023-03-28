import pandas as pd

from DiceRoller import dice_roller, DiceRoller

dice_roller_instance = DiceRoller()


class AllAncestries:
    @staticmethod
    def ancestry_investigator(chosen_ancestry):
        if chosen_ancestry == "człowiek":
            database_name = "humanAncestry.xlsx"
            return AllAncestries.attribute_show(database_name) #Zwróci zwrócenie z Atribute show

    @staticmethod
    def attribute_show(database_name):

        data = pd.read_excel(f'dataBase\{database_name}', 'Ludzie')
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

        print("Wybrałeś Człowieka. To są jego statystyki:\n\n")
        print(df.to_csv(index=False))




    def personality_picker(self):
        dice_result = dice_roller(3, 6)
        print(dice_result)
        data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Osobowość')
        df = pd.DataFrame(data, columns=['result', 'value'])

        if dice_result == 3:
            print(df.iloc[0, 1])
        elif dice_result == 4:
            print(df.iloc[1, 1])
        elif 5 <= dice_result <= 6:
            print(df.iloc[2, 1])
        elif 7 <= dice_result <= 8:
            print(df.iloc[3, 1])
        elif 9 <= dice_result <= 12:
            print(df.iloc[4, 1])
        elif 13 <= dice_result <= 14:
            print(df.iloc[5, 1])
        elif 15 <= dice_result <= 16:
            print(df.iloc[6, 1])
        elif dice_result == 17:
            print(df.iloc[7, 1])
        else:
            print(df.iloc[8, 1])
