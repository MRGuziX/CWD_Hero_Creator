import random

from DiceRoller import dice_roller
from UpgradeMechanics import UpgradeMechanics
import pandas as pd

mechanic_instance = UpgradeMechanics()


def human_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['result', 'value'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 0])

    match dice_roll:
        case 1:
            hero.insanity += dice_roller(1, 6)
        case 2:
            hero.corruption += 1
        case 4:
            hero.corruption += 1
        case 13:
            mechanic_instance.add_language(hero, "verbal", None, True)
        case 14:
            hero.languages_spoken.append("Wspólny")
            hero.languages_written.append("Wspólny")
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def human_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.age = (df.iloc[0, 1])
        case 4 | 5 | 6 | 7:
            hero.age = (df.iloc[1, 1])
        case 8 | 9 | 10 | 11 | 12:
            hero.age = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[3, 1])
        case 16 | 17:
            hero.age = (df.iloc[4, 1])
        case _:
            hero.age = (df.iloc[5, 1])


def human_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 0])
        case 4:
            hero.character = (df.iloc[1, 0])
        case 5 | 6:
            hero.character = (df.iloc[2, 0])
        case 7 | 8:
            hero.character = (df.iloc[3, 0])
        case 9 | 10 | 11 | 12:
            hero.character = (df.iloc[4, 0])
        case 13 | 14:
            hero.character = (df.iloc[5, 0])
        case 15 | 16:
            hero.character = (df.iloc[6, 0])
        case 17:
            hero.character = (df.iloc[7, 0])
        case _:
            hero.character = (df.iloc[8, 0])


def human_religion_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Religia')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.quirks = (df.iloc[0, 1])
        case 4:
            hero.quirks = (df.iloc[1, 1])
        case 5 | 6:
            hero.quirks = (df.iloc[2, 1])
        case 7 | 8 | 9 | 10:
            hero.quirks = (df.iloc[3, 1])
        case 11 | 12 | 13 | 14 | 15:
            hero.quirks = (df.iloc[4, 1])
        case _:
            hero.quirks = (df.iloc[5, 1])


def human_body_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.body = (df.iloc[0, 1])
        case 4:
            hero.body = (df.iloc[1, 1])
        case 5 | 6:
            hero.body = (df.iloc[2, 1])
        case 7 | 8:
            hero.body = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.body = (df.iloc[4, 1])
        case 13 | 14:
            hero.body = (df.iloc[5, 1])
        case 15 | 16:
            hero.body = (df.iloc[6, 1])
        case 17:
            hero.body = (df.iloc[7, 1])
        case _:
            hero.body = (df.iloc[8, 1])


def human_appearance_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wygląd')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.appearance = (df.iloc[0, 1])
        case 4:
            hero.appearance = (df.iloc[1, 1])
        case 5 | 6:
            hero.appearance = (df.iloc[2, 1])
        case 7 | 8:
            hero.appearance = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.appearance = (df.iloc[4, 1])
        case 13 | 14:
            hero.appearance = (df.iloc[5, 1])
        case 15 | 16:
            hero.appearance = (df.iloc[6, 1])
        case 17:
            hero.appearance = (df.iloc[7, 1])
        case _:
            hero.appearance = (df.iloc[8, 1])


def automaton_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 1])

    match dice_roll:
        case 1:
            hero.corruption += dice_roller(1, 3)
        case 2:
            hero.insanity += dice_roller(1, 6)
            # dodaj profesje
        case 13:
            mechanic_instance.add_language(hero, "verbal", None, True)
        case 14:
            hero.language_spoken.append("Wspólny")
            hero.language_written.append("Wspólny")
        case 19:
            print("dodaj miecz do equ")
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def automaton_appearance_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wygląd')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.appearance = (df.iloc[0, 1])
        case 4:
            hero.appearance = (df.iloc[1, 1])
        case 5 | 6:
            hero.appearance = (df.iloc[2, 1])
        case 7 | 8:
            hero.appearance = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.appearance = (df.iloc[4, 1])
        case 13 | 14:
            hero.appearance = (df.iloc[5, 1])
        case 15 | 16:
            hero.appearance = (df.iloc[6, 1])
        case 17:
            hero.appearance = (df.iloc[7, 1])
        case _:
            hero.appearance = (df.iloc[8, 1])


def automaton_function_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Funkcja')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 0])

    match dice_roll:
        case 1 | 2 | 3 | 4:
            choice = input("Chcesz zwiększyć:\n"
                           "1. Siła\n"
                           "2. Zręczność")
            if choice == 1:
                hero.strength += 2
            else:
                hero.dexterity += 2
        case 5 | 6 | 7 | 8:
            hero.strength += 2
        case 9 | 10 | 11 | 12:
            choice = input("Chcesz zwiększyć:\n"
                           "1. Inteligencja\n"
                           "2. Wola")
            if choice == 1:
                hero.intelligence += 2
            else:
                hero.will += 2

        case 13 | 14 | 15 | 16:
            choice = input("Chcesz zwiększyć:\n"
                           "1. Zręczność\n"
                           "2. Intelekt")
            if choice == 1:
                hero.dexterity += 2
            else:
                hero.intelligence += 2
        case 17 | 18 | 19 | 20:
            mechanic_instance.add_attribute_points(hero, 2)


def automaton_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3 | 4 | 5 | 6 | 7 | 8:
            hero.age = (df.iloc[0, 1])
        case 9 | 10 | 11 | 12:
            hero.age = (df.iloc[1, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[2, 1])
        case 16 | 17:
            hero.age = (df.iloc[3, 1])
        case 18:
            hero.age = (df.iloc[4, 1])


def automaton_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 1])
        case 4:
            hero.character = (df.iloc[1, 1])
        case 5 | 6 | 7:
            hero.character = (df.iloc[2, 1])
        case 8:
            hero.character = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12 | 13:
            hero.character = (df.iloc[4, 1])
        case 14:
            hero.character = (df.iloc[5, 1])
        case 15:
            hero.character = (df.iloc[6, 1])
        case 16 | 17:
            hero.character = (df.iloc[7, 1])
        case 18:
            hero.character = (df.iloc[8, 1])


def automaton_form_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Forma')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.body = (df.iloc[0, 1])
            hero.health -= 5
            hero.size = "1/2"
        case 4 | 5:
            hero.body = (df.iloc[1, 1])
            hero.size = "1/2"
        case 6 | 7 | 8 | 9:
            hero.body = (df.iloc[2, 1])
            hero.size = "1/2"
        case 10 | 11 | 12 | 13 | 14 | 15:
            hero.body = (df.iloc[3, 1])
            hero.size = 1
        case 16 | 17:
            hero.body = (df.iloc[4, 1])
            hero.size = 2
            hero.defence -= 2
            hero.speed -= 2
        case 18:
            hero.body = (df.iloc[5, 1])
            hero.size = 2
            hero.speed += 2
            hero.defence -= 3


def goblin_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 1])

    match dice_roll:
        case 1:
            hero.corruption += 1
        case 6:
            hero.insanity += 1
        case 12:
            print("dodaj profesje")
        case 13:
            mechanic_instance.add_language(hero, "verbal", None, True)
        case 14:
            print("dodaj nóż do equ")
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def goblin_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 1])
        case 4:
            hero.character = (df.iloc[1, 1])
        case 5 | 6:
            hero.character = (df.iloc[2, 1])
        case 7 | 8:
            hero.character = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.character = (df.iloc[4, 1])
        case 13 | 14:
            hero.character = (df.iloc[5, 1])
        case 15 | 16:
            hero.character = (df.iloc[6, 1])
        case 17:
            hero.character = (df.iloc[7, 1])
        case 18:
            hero.character = (df.iloc[8, 1])


def goblin_special_feature_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Cecha Szczególna')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.appearance = (df.iloc[dice_roll, 1])


def goblin_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.age = (df.iloc[0, 1])
        case 4 | 5 | 6 | 7:
            hero.age = (df.iloc[1, 1])
        case 8 | 9 | 10 | 11 | 12:
            hero.age = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[3, 1])
        case 16 | 17:
            hero.age = (df.iloc[4, 1])
        case 18:
            hero.age = (df.iloc[5, 1])


def goblin_body_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.body = (df.iloc[0, 1])
        case 4:
            hero.body = (df.iloc[1, 1])
        case 5 | 6:
            hero.body = (df.iloc[2, 1])
        case 7 | 8:
            hero.body = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.body = (df.iloc[4, 1])
        case 13 | 14:
            hero.body = (df.iloc[5, 1])
        case 15 | 16:
            hero.body = (df.iloc[6, 1])
        case 17:
            hero.body = (df.iloc[7, 1])
        case _:
            hero.body = (df.iloc[8, 1])


def goblin_strange_habit_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Dziwny Nawyk')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.quirks = (df.iloc[dice_roll, 1])


def dwarf_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.age = (df.iloc[0, 1])
        case 4 | 5 | 6 | 7:
            hero.age = (df.iloc[1, 1])
        case 8 | 9 | 10 | 11 | 12:
            hero.age = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[3, 1])
        case 16 | 17:
            hero.age = (df.iloc[4, 1])
        case 18:
            hero.age = (df.iloc[5, 1])


def dwarf_body_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.body = (df.iloc[0, 1])
        case 4 | 5 | 6:
            hero.body = (df.iloc[1, 1])
        case 7 | 8:
            hero.body = (df.iloc[2, 1])
        case 9 | 10 | 11 | 12:
            hero.body = (df.iloc[3, 1])
        case 13 | 14 | 15:
            hero.body = (df.iloc[4, 1])
        case 16 | 17:
            hero.body = (df.iloc[5, 1])
        case 18:
            hero.body = (df.iloc[6, 1])


def dwarf_appearance_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wygląd')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3 | 4:
            hero.appearance = (df.iloc[0, 1])
        case 5 | 6:
            hero.appearance = (df.iloc[1, 1])
        case 7 | 8:
            hero.appearance = (df.iloc[2, 1])
        case 9 | 10 | 11:
            hero.appearance = (df.iloc[3, 1])
        case 12 | 13 | 13 | 14 | 15:
            hero.appearance = (df.iloc[4, 1])
        case 16 | 17 | 18:
            hero.appearance = (df.iloc[5, 1])


def dwarf_hatred_race_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Znienawidzone Stworzenia')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 1 | 2:
            hero.quirks = (df.iloc[0, 1])
        case 3 | 4:
            hero.quirks = (df.iloc[1, 1])
        case 5 | 6:
            hero.quirks = (df.iloc[2, 1])
        case 7 | 8:
            hero.quirks = (df.iloc[3, 1])
        case 9 | 10:
            hero.quirks = (df.iloc[4, 1])
        case 11 | 12:
            hero.quirks = (df.iloc[5, 1])
        case 13 | 14:
            hero.quirks = (df.iloc[6, 1])
        case 15 | 16:
            hero.quirks = (df.iloc[7, 1])
        case 17 | 18:
            hero.quirks = (df.iloc[8, 1])
        case 19 | 20:
            hero.quirks = (df.iloc[9, 1])


def dwarf_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 1])

    match dice_roll:
        case 1:
            hero.corruption += 1
        case 12:
            print("dodaj profesje")
        case 13:
            mechanic_instance.add_language(hero, "verbal", None, True)
        case 14:
            print("dodaj topór lub młot do equ")
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def dwarf_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 1])
        case 4:
            hero.character = (df.iloc[1, 1])
        case 5 | 6:
            hero.character = (df.iloc[2, 1])
        case 7 | 8:
            hero.character = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.character = (df.iloc[4, 1])
        case 13 | 14:
            hero.character = (df.iloc[5, 1])
        case 15 | 16:
            hero.character = (df.iloc[6, 1])
        case 17:
            hero.character = (df.iloc[7, 1])
        case 18:
            hero.character = (df.iloc[8, 1])


def changeling_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.age = (df.iloc[0, 1])
        case 4 | 5 | 6 | 7:
            hero.age = (df.iloc[1, 1])
        case 8 | 9 | 10 | 11 | 12:
            hero.age = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[3, 1])
        case 16 | 17:
            hero.age = (df.iloc[4, 1])
        case 18:
            hero.age = (df.iloc[5, 1])
    return hero


def changeling_body_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(1, 6):
        case 1 | 2 | 3:
            hero.body = (df.iloc[0, 1])
        case 4 | 5 | 6:
            hero.body = (df.iloc[1, 1])
    return hero


def changeling_fake_appearance_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Pozorne Pochodzenie')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3 | 4:
            hero.appearance = (df.iloc[0, 1])
            goblin_age_picker(hero, database_name)
            goblin_body_picker(hero, database_name)
            goblin_special_feature_picker(hero, database_name)
        case 5 | 6 | 7:
            hero.appearance = (df.iloc[1, 1])
            dwarf_age_picker(hero, database_name)
            dwarf_body_picker(hero, database_name)
            dwarf_appearance_picker(hero, database_name)
        case 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
            hero.appearance = (df.iloc[2, 1])
            human_age_picker(hero, database_name)
            human_body_picker(hero, database_name)
            human_appearance_picker(hero, database_name)
        case 16 | 17:
            hero.appearance = (df.iloc[3, 1])
            orc_appearance_picker(hero, database_name)
            orc_body_picker(hero, database_name)
            orc_age_picker(hero, database_name)
        case 18:
            hero.appearance = (df.iloc[4, 1])


def changeling_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 1])

    match dice_roll:
        case 1:
            hero.insanity += 1
        case 3:
            hero.corruption += 1
        case 4:
            hero.corruption += 1
            mechanic_instance.add_language(hero, "verbal", None, True)
        case 14:
            hero.language_spoken.append("Wspólny")
            hero.language_written.append("Wspólny")
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def changeling_strange_habit_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Dziwactwo')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.quirks = (df.iloc[dice_roll, 1])


def changeling_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 1])
        case 4:
            hero.character = (df.iloc[1, 1])
        case 5 | 6:
            hero.character = (df.iloc[2, 1])
        case 7 | 8:
            hero.character = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.character = (df.iloc[4, 1])
        case 13 | 14:
            hero.character = (df.iloc[5, 1])
        case 15 | 16:
            hero.character = (df.iloc[6, 1])
        case 17:
            hero.character = (df.iloc[7, 1])
        case 18:
            hero.character = (df.iloc[8, 1])


def orc_age_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.age = (df.iloc[0, 1])
        case 4 | 5 | 6 | 7:
            hero.age = (df.iloc[1, 1])
        case 8 | 9 | 10 | 11 | 12:
            hero.age = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.age = (df.iloc[3, 1])
        case 16 | 17:
            hero.age = (df.iloc[4, 1])
        case 18:
            hero.age = (df.iloc[5, 1])


def orc_body_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.body = (df.iloc[0, 1])
        case 4:
            hero.body = (df.iloc[1, 1])
        case 5 | 6:
            hero.body = (df.iloc[2, 1])
        case 7 | 8:
            hero.body = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.body = (df.iloc[4, 1])
        case 13 | 14:
            hero.body = (df.iloc[5, 1])
        case 15 | 16:
            hero.body = (df.iloc[6, 1])
        case 17:
            hero.body = (df.iloc[7, 1])
        case 18:
            hero.body = (df.iloc[8, 1])


def orc_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 1])

    match dice_roll:
        case 1:
            hero.corruption += 2
        case 2:
            hero.corruption += 1
        case 14:
            hero.language_spoken.append("Wspólny")
            hero.language_written.append("Wspólny")
        case 18:
            print("doddaj miecz do equ")
        case 19:
            hero.corruption += 1
        case 20:
            hero.copper_coins += dice_roller(2, 6)


def orc_character_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3:
            hero.character = (df.iloc[0, 1])
        case 4:
            hero.character = (df.iloc[1, 1])
        case 5 | 6:
            hero.character = (df.iloc[2, 1])
        case 7 | 8:
            hero.character = (df.iloc[3, 1])
        case 9 | 10 | 11 | 12:
            hero.character = (df.iloc[4, 1])
        case 13 | 14:
            hero.character = (df.iloc[5, 1])
        case 15 | 16:
            hero.character = (df.iloc[6, 1])
        case 17:
            hero.character = (df.iloc[7, 1])
        case 18:
            hero.character = (df.iloc[8, 1])


def orc_appearance_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Wygląd')
    df = pd.DataFrame(data, columns=['value', 'result'])

    match dice_roller(3, 6):
        case 3 | 4 | 5:
            hero.appearance = (df.iloc[0, 1])
        case 6 | 7 | 8:
            hero.appearance = (df.iloc[1, 1])
        case 9 | 10 | 11 | 12:
            hero.appearance = (df.iloc[2, 1])
        case 13 | 14 | 15:
            hero.appearance = (df.iloc[3, 1])
        case 16 | 17:
            hero.appearance = (df.iloc[4, 1])
        case 18:
            hero.appearance = (df.iloc[5, 1])


class BackstoryCreator:

    @staticmethod
    def database_picker(hero):
        match hero.ancestry:
            case "Człowiek":
                database_name = "humanAncestry"
                human_backstory_picker(hero, database_name)
                human_character_picker(hero, database_name)
                human_religion_picker(hero, database_name)
                human_age_picker(hero, database_name)
                human_body_picker(hero, database_name)
                human_appearance_picker(hero, database_name)
                return hero

            case "Automaton":
                database_name = "automatonAncestry"
                automaton_age_picker(hero, database_name)
                automaton_appearance_picker(hero, database_name)
                automaton_backstory_picker(hero, database_name)
                automaton_character_picker(hero, database_name)
                automaton_function_picker(hero, database_name)
                automaton_form_picker(hero, database_name)
                return hero

            case "Goblin":
                database_name = "goblinAncestry"
                goblin_age_picker(hero, database_name)
                goblin_body_picker(hero, database_name)
                goblin_backstory_picker(hero, database_name)
                goblin_character_picker(hero, database_name)
                goblin_special_feature_picker(hero, database_name)
                goblin_strange_habit_picker(hero, database_name)
                return hero

            case "Krasnolud":
                database_name = "krasnoludAncestry"
                dwarf_backstory_picker(hero, database_name)
                dwarf_character_picker(hero, database_name)
                dwarf_appearance_picker(hero, database_name)
                dwarf_age_picker(hero, database_name)
                dwarf_hatred_race_picker(hero, database_name)
                dwarf_body_picker(hero, database_name)
                return hero

            case "Odmieniec":
                database_name = "odmieniecAncestry"
                changeling_fake_appearance_picker(hero, database_name)
                changeling_age_picker(hero, database_name)
                changeling_body_picker(hero, database_name)
                changeling_backstory_picker(hero, database_name)
                changeling_character_picker(hero, database_name)
                changeling_strange_habit_picker(hero, database_name)
                return hero

            case "Ork":
                database_name = "orkAncestry"
                orc_age_picker(hero, database_name)
                orc_backstory_picker(hero, database_name)
                orc_character_picker(hero, database_name)
                orc_appearance_picker(hero, database_name)
                orc_body_picker(hero, database_name)
                return hero

            case _:
                return "Błąd"
