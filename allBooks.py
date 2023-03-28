def ancestry_picker(book_choice):
    if book_choice == "1":
        print("Jakie pochodzenie wybierasz?\n\n"
              "1.Człowiek\n"
              "2.Automaton\n"
              "3.Goblin\n"
              "4.Krasnolud\n"
              "5.Odmieniec\n"
              "6.Ork\n"
              "7.Losowe")
    elif book_choice == "2":
        print("Jakie pochodzenie wybierasz?\n\n"
              "1.Chochlik\n"
              "2.Elf\n"
              "3.Hobgoblin\n"
              "4.Losowe")
    else:
        print("Błąd")
    ancestry_choice = input()
    return ancestry_choice


class Books:
    pass
