import random

import pandas as pd


def books_pick_up():
    print("Z jakich książek chcesz skorzystać?\n\n"
          "Wybierz numer pozycji:\n"
          "1.Cień Władcy Demonów - Podręcznik Główny\n"
          "2.Straszliwe Piękno (N/A)\n")
    book_name = input()

    if book_name == "1":
        print("Wybrałeś: 1.Cień Władcy Demonów - Podręcznik Główny")
        all_ancestries_by_books(book_name)
    elif book_name == "2":
        print("2.Straszliwe Piękno (N/A)")
        all_ancestries_by_books(book_name)
    else:
        print("Błąd: Błąd wyboru książki!")


def all_ancestries_by_books(book_name):
    if book_name == "1":
        print("Jakie pochodzenie wybierasz?\n\n"
              "1.Człowiek\n"
              "2.Automaton\n"
              "3.Goblin\n"
              "4.Krasnolud\n"
              "5.Odmieniec\n"
              "6.Ork\n"
              "7.Losowe")
    elif book_name == "2":
        print("Jakie pochodzenie wybierasz?\n\n"
              "1.Chochlik\n"
              "2.Elf\n"
              "3.Hobgoblin\n"
              "4.Losowe")
    else:
        print("Błąd")

    ancestry_name = input()
    raw_data_picker(ancestry_name)


def raw_data_picker(ancestry_name):
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Ludzie')
    df = pd.DataFrame(data, columns=['attribute', 'value'])

    if ancestry_name == "1":
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
        languages_verbal = df.iloc[14, 1]
        languages_written = df.iloc[15, 1]
        character_size = None

        print("Wybrałeś Człowieka. To są jego statystyki:\n\n")
        print(df.to_csv(index=False))

        print("Wybierz jeden z atrybutów i podnieś go o 1:\n\n"
              "1.Siła\n"
              "2.Zręczność\n"
              "3.Inteligencja\n"
              "4.Wola")

        increase_attribute = input()

        if increase_attribute == "1":
            strength += 1
            health += 1
        elif increase_attribute == "2":
            dexterity += 1
            defence += 1
        elif increase_attribute == "3":
            intelligence += 1
            perception += 1
        else:
            will += 1

        print("Wybierz swój rozmiar:\n\n"
              "1. 'Jeden' (1)\n"
              "2. 'Pół' (1/2)")
        picked_size = input()

        if picked_size == "1":
            character_size = "1"
        else:
            character_size = "0.5"


def backstory_picker():
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Przeszłość')
    df = pd.DataFrame(data, columns=['value', 'result'])
    dice_roll = random.randint(1, 20)
    print(df.iloc[dice_roll, 1])


def character_picker(dice_rolls):
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Osobowość')
    df = pd.DataFrame(data, columns=['value', 'result'])

    if dice_rolls == 3:
        print(df.iloc[0, 1])
    elif dice_rolls == 4:
        print(df.iloc[1, 1])
    elif 5 <= dice_rolls <= 6:
        print(df.iloc[2, 1])
    elif 7 <= dice_rolls <= 8:
        print(df.iloc[3, 1])
    elif 9 <= dice_rolls <= 12:
        print(df.iloc[4, 1])
    elif 13 <= dice_rolls <= 14:
        print(df.iloc[5, 1])
    elif 15 <= dice_rolls <= 16:
        print(df.iloc[6, 1])
    elif dice_rolls == 17:
        print(df.iloc[7, 1])
    else:
        print(df.iloc[8, 1])


def religion_picker(dice_rolls):
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Religia')
    df = pd.DataFrame(data, columns=['value', 'result'])

    if dice_rolls == 3:
        print(df.iloc[0, 1])
    elif dice_rolls == 4:
        print(df.iloc[1, 1])
    elif 5 <= dice_rolls <= 6:
        print(df.iloc[2, 1])
    elif 7 <= dice_rolls <= 10:
        print(df.iloc[3, 1])
    elif 11 <= dice_rolls <= 15:
        print(df.iloc[4, 1])
    else:
        print(df.iloc[5, 1])


def age_picker(dice_rolls):
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wiek')
    df = pd.DataFrame(data, columns=['value', 'result'])

    if dice_rolls == 3:
        print(df.iloc[0, 1])
    elif 4 <= dice_rolls <= 7:
        print(df.iloc[1, 1])
    elif 8 <= dice_rolls <= 12:
        print(df.iloc[2, 1])
    elif 13 <= dice_rolls <= 15:
        print(df.iloc[3, 1])
    elif 16 <= dice_rolls <= 17:
        print(df.iloc[4, 1])
    else:
        print(df.iloc[5, 1])

def body_picker(dice_rolls):
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Budowa Ciała')
    df = pd.DataFrame(data, columns=['value', 'result'])

    if dice_rolls == 3:
        print(df.iloc[0, 1])
    elif dice_rolls == 4:
        print(df.iloc[1, 1])
    elif dice_rolls == 5 or dice_rolls == 6:
        print(df.iloc[2, 1])
    elif dice_rolls == 7 or dice_rolls == 8:
        print(df.iloc[3, 1])
    elif 9 <= dice_rolls <= 12:
        print(df.iloc[4, 1])
    elif 13 <= dice_rolls <= 14:
        print(df.iloc[5, 1])
    elif dice_rolls == 15 or dice_rolls == 16:
        print(df.iloc[6, 1])
    elif dice_rolls == 17:
        print(df.iloc[7, 1])
    else:
        print(df.iloc[8, 1])


def appearance_picker(dice_rolls):
    dice_roller(3, 6)
    data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wygląd')
    df = pd.DataFrame(data, columns=['value', 'result'])

    if dice_rolls == 3:
        print(df.iloc[0, 1])
    elif dice_rolls == 4:
        print(df.iloc[1, 1])
    elif dice_rolls == 5 or dice_rolls == 6:
        print(df.iloc[2, 1])
    elif dice_rolls == 7 or dice_rolls == 8:
        print(df.iloc[3, 1])
    elif 9 <= dice_rolls <= 12:
        print(df.iloc[4, 1])
    elif 13 <= dice_rolls <= 14:
        print(df.iloc[5, 1])
    elif dice_rolls == 15 or dice_rolls == 16:
        print(df.iloc[6, 1])
    elif dice_rolls == 17:
        print(df.iloc[7, 1])
    else:
        print(df.iloc[8, 1])


def profession_picker(dice_rolls):
 wybierz diwe profesje lub zrezygnuj z jednej w zamian za mówienie w jednym nowym jezyku, lub czytanie i pisanie w tym który juz znasz


def dice_roller(amount_of_dice, type_of_dice):
    dice_result = [random.randint(1, type_of_dice) for _ in range(amount_of_dice + 1)]
    return sum(dice_result)


class CreateAHero:

