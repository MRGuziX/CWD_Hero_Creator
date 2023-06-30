from AllAncestries import AllAncestries
from AllBooks import AllBooks
from BackstoryCreator import BackstoryCreator
from HeroCreator import *
from ItemCreator import Items
from PDFCreator import PDFCreator

from UpgradeMechanics import UpgradeMechanics

hero = Characters()
item = Items()
book_instance = AllBooks()
ancestry_instance = AllAncestries()
mechanic_instance = UpgradeMechanics()
backstory_instance = BackstoryCreator()
pdf_creator_instance = PDFCreator()

hero.name = str(input("Podaj imię bohatera:"))
book_choice = book_instance.book_pick()
hero.book = book_choice
ancestry_choice = book_instance.ancestry_pick(book_choice)
hero.ancestry = ancestry_choice
hero = ancestry_instance.attribute_picker(hero)

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
            hero = mechanic_instance.add_profession(hero, True)

    case "Automaton":
        hero = backstory_instance.database_picker(hero)

        # dodanie ifnromacji o formie obiektu na kartę postaci
    case "Goblin":
        hero = backstory_instance.database_picker(hero)
        hero = mechanic_instance.add_language(hero, "verbal", "Wspólny", False)
        hero = mechanic_instance.add_language(hero, "verbal", "Elficki", False)

    case "Krasnolud":
        hero = backstory_instance.database_picker(hero)

    case "Odmieniec":
        hero = backstory_instance.database_picker(hero)

    case "Ork":
        hero = backstory_instance.database_picker(hero)

print("Możesz wybrać: \n"
      "1. Dwie dodatkowe profesje\n"
      "2. Profesja ORAZ umiejętnosć czytania i pisania w języku w którym umiesz mówić.\n"
      "3. Profesja ORAZ umiejętnosć mówienia w dodatkowym języku")
profession_choice = int(input())
match profession_choice:
    case 1:
        hero = mechanic_instance.add_profession(hero, True)
        hero = mechanic_instance.add_profession(hero, True)

    case 2:
        hero = mechanic_instance.add_profession(hero, True)
        hero = mechanic_instance.language_compare_add(hero, "written")

    case 3:
        hero = mechanic_instance.add_profession(hero, True)
        hero = mechanic_instance.language_compare_add(hero, "verbal")

hero = mechanic_instance.add_wealth(hero)
pdf_creator_instance.pdf_creator(hero, item)
