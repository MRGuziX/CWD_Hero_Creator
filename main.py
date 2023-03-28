import random
import pandas as pd
from allBooks import Books, ancestry_picker
from human_Ancestry import HumanHero


human_hero_instance = HumanHero()
ancestry_instance = Books()


def book_pick():
    print("Z jakich książek chcesz skorzystać?\n\n"
          "Wybierz numer pozycji:\n"
          "1.Cień Władcy Demonów - Podręcznik Główny\n"
          "2.Straszliwe Piękno (N/A)\n")
    book_choice = input()
    return book_choice


class CharacterCreationQuestions:
    book_choice = book_pick()
    ancestry_picker(book_choice)



    # human_hero_instance.personality_picker()
    #
    #
    # print("Wybierz jeden z atrybutów i podnieś go o 1:\n\n"
    #       "1.Siła\n"
    #       "2.Zręczność\n"
    #       "3.Inteligencja\n"
    #       "4.Wola")
    #
    # choice = input()
    # statistic_to_increase = FinalCharacter(choice)
    # FinalCharacter.statistic_increment(statistic_to_increase)
    #
    # print("Wybierz swój rozmiar:\n\n"
    #       "1. 'Jeden' (1)\n"
    #       "2. 'Pół' (1/2)")
    # picked_size = input()
    # FinalCharacter.size_increment(picked_size)

#
# def backstory_picker():
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Przeszłość')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#     dice_roll = random.randint(1, 20)
#     print(df.iloc[dice_roll, 1])
#
#
# def character_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Osobowość')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     if dice_rolls == 3:
#         print(df.iloc[0, 1])
#     elif dice_rolls == 4:
#         print(df.iloc[1, 1])
#     elif 5 <= dice_rolls <= 6:
#         print(df.iloc[2, 1])
#     elif 7 <= dice_rolls <= 8:
#         print(df.iloc[3, 1])
#     elif 9 <= dice_rolls <= 12:
#         print(df.iloc[4, 1])
#     elif 13 <= dice_rolls <= 14:
#         print(df.iloc[5, 1])
#     elif 15 <= dice_rolls <= 16:
#         print(df.iloc[6, 1])
#     elif dice_rolls == 17:
#         print(df.iloc[7, 1])
#     else:
#         print(df.iloc[8, 1])
#
#
# def religion_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Religia')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     if dice_rolls == 3:
#         print(df.iloc[0, 1])
#     elif dice_rolls == 4:
#         print(df.iloc[1, 1])
#     elif 5 <= dice_rolls <= 6:
#         print(df.iloc[2, 1])
#     elif 7 <= dice_rolls <= 10:
#         print(df.iloc[3, 1])
#     elif 11 <= dice_rolls <= 15:
#         print(df.iloc[4, 1])
#     else:
#         print(df.iloc[5, 1])
#
#
# def age_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wiek')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     if dice_rolls == 3:
#         print(df.iloc[0, 1])
#     elif 4 <= dice_rolls <= 7:
#         print(df.iloc[1, 1])
#     elif 8 <= dice_rolls <= 12:
#         print(df.iloc[2, 1])
#     elif 13 <= dice_rolls <= 15:
#         print(df.iloc[3, 1])
#     elif 16 <= dice_rolls <= 17:
#         print(df.iloc[4, 1])
#     else:
#         print(df.iloc[5, 1])
#
#
# def body_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Budowa Ciała')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     if dice_rolls == 3:
#         print(df.iloc[0, 1])
#     elif dice_rolls == 4:
#         print(df.iloc[1, 1])
#     elif dice_rolls == 5 or dice_rolls == 6:
#         print(df.iloc[2, 1])
#     elif dice_rolls == 7 or dice_rolls == 8:
#         print(df.iloc[3, 1])
#     elif 9 <= dice_rolls <= 12:
#         print(df.iloc[4, 1])
#     elif 13 <= dice_rolls <= 14:
#         print(df.iloc[5, 1])
#     elif dice_rolls == 15 or dice_rolls == 16:
#         print(df.iloc[6, 1])
#     elif dice_rolls == 17:
#         print(df.iloc[7, 1])
#     else:
#         print(df.iloc[8, 1])
#
#
# def appearance_picker(dice_rolls):
#     dice_roller(3, 6)
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wygląd')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     if dice_rolls == 3:
#         print(df.iloc[0, 1])
#     elif dice_rolls == 4:
#         print(df.iloc[1, 1])
#     elif dice_rolls == 5 or dice_rolls == 6:
#         print(df.iloc[2, 1])
#     elif dice_rolls == 7 or dice_rolls == 8:
#         print(df.iloc[3, 1])
#     elif 9 <= dice_rolls <= 12:
#         print(df.iloc[4, 1])
#     elif 13 <= dice_rolls <= 14:
#         print(df.iloc[5, 1])
#     elif dice_rolls == 15 or dice_rolls == 16:
#         print(df.iloc[6, 1])
#     elif dice_rolls == 17:
#         print(df.iloc[7, 1])
#     else:
#         print(df.iloc[8, 1])
#
#
# def profession_picker(languages_verbal, languages_written):
#     dice_roller(3, 6)
#     # wybierz diwe profesje lub zrezygnuj z jednej w zamian za mówienie w jednym nowym jezyku, lub czytanie i pisanie w tym który juz znasz
#     print(
#         "Teraz możesz wybrać dwie profesje, lub profesje i możliwość mówienia nowym językiem lub umiejętność czytania i pisania w języku którym już umiesz mówić.")
#     print("Czy chcesz wybrać dodatkowy język zamiast profesji?\n\n"
#           "1.Tak\n"
#           "2.Nie")
#
#     profession_choice = input()
#
#     if profession_choice == 1:
#         data = pd.read_excel('dataBase\utilities.xlsx', 'Języki')
#         df = pd.DataFrame(data, columns=['value', 'result'])
#
#         print("To języki które Twoja postać posiada:")
#         print("Mówione:")
#         print(languages_verbal)
#         print("Czytanie i Pisanie:")
#         print(languages_written)
#         print("Chcesz dodać nowy jezyk mówiony, czy nauczyć się czytać i pisać w już posiadanym?")
#         learned_new_language = input("")
