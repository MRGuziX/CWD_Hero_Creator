import random

from DiceRoller import dice_roller
import pandas as pd


def human_backstory_picker(hero, database_name):
    data = pd.read_excel(f'dataBase\{database_name}.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    hero.backstory = (df.iloc[dice_roll, 0])


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

    match dice_roller(3, 6):
        case 3 | 4 | 5 | 6 | 7 | 8:
            hero.quirks = (df.iloc[0, 1])
        case 9 | 10 | 11 | 12:
            hero.quirks = (df.iloc[1, 1])
        case 13 | 14 | 15:
            hero.quirks = (df.iloc[2, 1])
        case 16 | 17:
            hero.quirks = (df.iloc[3, 1])
        case 18:
            hero.quirks = (df.iloc[4, 1])


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
        case 4 | 5:
            hero.body = (df.iloc[1, 1])
        case 6 | 7 | 8 | 9:
            hero.body = (df.iloc[2, 1])
        case 10 | 11 | 12 | 13 | 14 | 15:
            hero.body = (df.iloc[3, 1])
        case 16 | 17:
            hero.body = (df.iloc[4, 1])
        case 14:
            hero.body = (df.iloc[5, 1])
        case 15:
            hero.body = (df.iloc[6, 1])
        case 16 | 17:
            hero.body = (df.iloc[7, 1])
        case 18:
            hero.body = (df.iloc[8, 1])


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

            case "Goblin":
                database_name = "goblinAncestry"
                human_backstory_picker(hero, database_name)
            case "Krasnolud":
                database_name = "krasnoludAncestry"
                human_backstory_picker(hero, database_name)
            case "Odmieniec":
                database_name = "odmieniecAncestry"
                human_backstory_picker(hero, database_name)
            case "Ork":
                database_name = "orkAncestry"
                human_backstory_picker(hero, database_name)
            case _:
                return "Błąd"
        return hero

    """
    IF który będzie wybierał metody które zbudują nasze backstory
    """
