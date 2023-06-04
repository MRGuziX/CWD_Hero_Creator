from AllAncestries import AllAncestries
from AllBooks import AllBooks
from BackstoryCreator import BackstoryCreator
from HeroCreator import *
from PDFCreator import PDFCreator
from UpgradeMechanics import UpgradeMechanics

hero = Characters()
book_instance = AllBooks()
ancestry_instance = AllAncestries()
mechanic_instance = UpgradeMechanics()
backstory_instance = BackstoryCreator()
pdf_creator_instance = PDFCreator()

name = input("Podaj imię bohatera:")
hero.name = name
book_choice = book_instance.book_pick()
hero.book = book_choice
ancestry_choice = book_instance.ancestry_pick(book_choice)
hero.ancestry = ancestry_choice
hero = ancestry_instance.attribute_picker(hero)

"""Sprawdzenie tego jakiego pochodzenia jest postać i na tej
 podstawie wybranie dodatkowych upgrejdów oraz backstory"""

match ancestry_choice:
    case "Człowiek":
        hero = backstory_instance.database_picker(hero)
        hero = mechanic_instance.add_attribute_points(hero, 1)
        hero = mechanic_instance.add_size(hero)
        hero = mechanic_instance.add_language(hero, "verbal", "Wspólny", False)
        profession_or_language = input("Chcesz dodatkowy język mówiony czy profesję?\n"
                                       "1. Język\n"
                                       "2. Profesja")
        if profession_or_language == "1":
            hero = mechanic_instance.add_language(hero, "verbal", None, True)
        else:
            mechanic_instance.add_profession(hero)
        hero = pdf_creator_instance.pdf_creator(hero)

    case "Automaton":
        hero = backstory_instance.database_picker(hero)

        #dodanie ifnromacji o formie obiektu na kartę postaci
        hero = pdf_creator_instance.pdf_creator(hero)

    case "Goblin":
        hero = backstory_instance.database_picker(hero)
        hero = mechanic_instance.add_language(hero, "verbal", "Wspólny", False)
        hero = mechanic_instance.add_language(hero, "verbal", "Elficki", False)

        hero = pdf_creator_instance.pdf_creator(hero)

    case "Krasnolud":
        hero = backstory_instance.database_picker(hero)
        hero = pdf_creator_instance.pdf_creator(hero)

    case "Odmieniec":
        hero = backstory_instance.database_picker(hero)
        hero = pdf_creator_instance.pdf_creator(hero)

    case "Ork":
        hero = backstory_instance.database_picker(hero)
        hero = pdf_creator_instance.pdf_creator(hero)


# """Po backstory wybieramy sobie profesje czy 2 profesje czy jedna profesja i język.
# musimy pokazać graczowi jakie języki już zna. Zwrócić listę języków"""

# dodanie do wyborów z backstory modyfikacji equ i statów i języków
#


