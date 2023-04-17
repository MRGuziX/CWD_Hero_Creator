from AllAncestries import AllAncestries
from AllBooks import AllBooks
from BackstoryCreator import BackstoryCreator
from HeroCreator import *
from UpgradeMechanics import UpgradeMechanics

hero = Characters()
book_instance = AllBooks()
ancestry_instance = AllAncestries()
mechanic_instance = UpgradeMechanics()
backstory_instance = BackstoryCreator()

name = input("Podaj imię bohatera:")
hero.name = name
book_choice = book_instance.book_pick()
hero.book = book_choice
ancestry_choice = book_instance.ancestry_pick(book_choice)
hero.ancestry = ancestry_choice
hero = ancestry_instance.attribute_picker(hero)

"""Sprawdzenie tego jakiego pochodzenia jest postać i na tej
 podstawie wybranie dodatkowych upgrejdów oraz backstory"""
if ancestry_choice == "Człowiek":
    hero = backstory_instance.database_picker(hero)

    hero = mechanic_instance.add_attribute_points(hero)
    hero = mechanic_instance.add_size(hero)

    print("siła:", hero.strength)
    print("HP:", hero.health)
    print("Przeszłość:", hero.backstory)
    print("Wiek:", hero.age)
    print("Osobowość:", hero.character)
    print("Budowa Ciała:", hero.body)
    print("Wygląd:", hero.appearance)
    print("Rozmiar:", hero.character_size)

"""Po backstory wybieramy sobie profesje czy 2 profesje czy jedna profesja i język.
musimy pokazać graczowi jakie języki już zna. Zwrócić listę języków"""
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
