
class AllBooks:
    @staticmethod
    def ancestry_pick(book_choice):
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
        ancestry_choice = input().lower()

        match ancestry_choice:
            case  "1":
                return "człowiek"
            case  "2":
                return "Automaton"
            case  "3":
                return "Goblin"
            case  "4":
                return "Krasnolud"
            case  "5":
                return "Odmieniec"
            case  "6":
                return "Ork"
            case  "7":
                return "Losowe"
        return ancestry_choice

