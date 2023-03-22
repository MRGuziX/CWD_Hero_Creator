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
    if ancestry_name == "1":
        strength = 10
        dexterity = 10
        intelligence = 10
        will = 10
        perception = intelligence
        health = strength
        speed = 10

        print("Wybrałeś Człowieka. To są jego statystyki:\n\n"
              "Siła: " + str(strength) + "\n"
              "Zręczność: " + str(dexterity) + "\n"
              "Inteligencja: " + str(intelligence) + "\n"
              "Wola: " + str(will) + "\n"
              "Percepcja: " + str(perception) + "\n"
              "Zdrowie: " + str(health) + "\n"
              "Prędkość: " + str(speed) + "\n")

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
        elif increase_attribute == "3":
            intelligence += 1
        else:
            will += 1

        print("Oto nowe statystyki:\n\n"
            "Siła: " + str(strength) + "\n"
              "Zręczność: " + str(dexterity) + "\n"
              "Inteligencja: " + str(intelligence) + "\n"
              "Wola: " + str(will) + "\n"
              "Zdrowie: " + str(health) + "\n")




class CreateAHero:
    books_pick_up()
