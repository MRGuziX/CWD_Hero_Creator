from AllAncestries import AllAncestries
from AllBooks import AllBooks
from Builder_CWD_Hero import *
from UpgradeMechanics import UpgradeMechanics

hero = Characters()
book_instance = AllBooks()
ancestry_instance = AllAncestries()
mechanic_instance = UpgradeMechanics()


name = input("Podaj imię bohatera:")
hero.name = name
book_choice = book_instance.book_pick()
hero.book = book_choice
ancestry_choice = book_instance.ancestry_pick(book_choice)
hero.ancestry = ancestry_choice
hero = ancestry_instance.attribute_picker(hero)

if ancestry_choice == "Człowiek":
    hero = mechanic_instance.statistic_increment(hero)
    hero = mechanic_instance.size_increment(hero)

#
#
# hero.book = book_pick()
# hero.ancestry = AllBooks.ancestry_pick(hero.book)
# chosen_ancestry = AllAncestries.ancestry_investigator(hero.ancestry)
#
#
# def increase_attr():
#     choice = input("Wybierz numer statystyki do podniesienia o 1\n\n""1.Siła\n"
#                    "2.Zręczność\n"
#                    "3.Inteligencja\n"
#                    "4.Wola\n").lower()
#
#     match choice:
#         case "1":
#             "Siła"
#         case "2":
#             "Zręczność"
#         case "3":
#             "Inteligencja"
#         case "4":
#             "Wola"
#         case _:
#             "Błąd"
#     return mechanics.statistic_increment(choice)
#
#
# increase_attr()
#
#
# class CharacterCreationQuestions:
#     pass
#
#
#     print("Wybierz swój rozmiar:\n\n"
#           "1. 'Jeden' (1)\n"
#           "2. 'Pół' (1/2)")
#     picked_size = input()
#     FinalCharacter.size_increment(picked_size)
#
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
#     match dice_rolls:
#         case 3:
#             print(df.iloc[0, 1])
#         case 4:
#             print(df.iloc[1, 1])
#         case 5 | 6:
#             print(df.iloc[2, 1])
#         case 7 | 8:
#             print(df.iloc[3, 1])
#         case 9 | 10 | 11 | 12:
#             print(df.iloc[4, 1])
#         case 13 | 14:
#             print(df.iloc[5, 1])
#         case 15 | 16:
#             print(df.iloc[6, 1])
#         case 17:
#             print(df.iloc[7, 1])
#         case _:
#             print(df.iloc[8, 1])
#
#
# def religion_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Religia')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     match dice_rolls:
#         case 3:
#             print(df.iloc[0, 1])
#         case 4:
#             print(df.iloc[1, 1])
#         case 5 | 6:
#             print(df.iloc[2, 1])
#         case 7 | 8 | 9 | 10:
#             print(df.iloc[3, 1])
#         case 11 | 12 | 13 | 14 | 15:
#             print(df.iloc[4, 1])
#         case _:
#             print(df.iloc[5, 1])
#
#
# def age_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wiek')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     match dice_rolls:
#         case 3:
#             print(df.iloc[0, 1])
#         case 4 | 5 | 6 | 7:
#             print(df.iloc[1, 1])
#         case 8 | 9 | 10 | 11 | 12:
#             print(df.iloc[2, 1])
#         case 13 | 14 | 15:
#             print(df.iloc[3, 1])
#         case 16 | 17:
#             print(df.iloc[4, 1])
#         case _:
#             print(df.iloc[5, 1])
#
#
# def body_picker(dice_rolls):
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Budowa Ciała')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     match dice_rolls:
#         case 3:
#             print(df.iloc[0, 1])
#         case 4:
#             print(df.iloc[1, 1])
#         case 5 | 6:
#             print(df.iloc[2, 1])
#         case 7 | 8:
#             print(df.iloc[3, 1])
#         case 9 | 10 | 11 | 12:
#             print(df.iloc[4, 1])
#         case 13 | 14:
#             print(df.iloc[5, 1])
#         case 15 | 16:
#             print(df.iloc[6, 1])
#         case 17:
#             print(df.iloc[7, 1])
#         case _:
#             print(df.iloc[8, 1])
#
#
# def appearance_picker(dice_rolls):
#     dice_roller(3, 6)
#     data = pd.read_excel('dataBase\humanAncestry.xlsx', 'Wygląd')
#     df = pd.DataFrame(data, columns=['value', 'result'])
#
#     match dice_rolls:
#         case 3:
#             print(df.iloc[0, 1])
#         case 4:
#             print(df.iloc[1, 1])
#         case 5, 6:
#             print(df.iloc[2, 1])
#         case 7, 8:
#             print(df.iloc[3, 1])
#         case 9, 10, 11, 12:
#             print(df.iloc[4, 1])
#         case 13, 14:
#             print(df.iloc[5, 1])
#         case 15, 16:
#             print(df.iloc[6, 1])
#         case 17:
#             print(df.iloc[7, 1])
#         case _:
#             print(df.iloc[8, 1])
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
