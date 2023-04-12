
class AllBooks:
    @staticmethod
    def book_pick():
        print("Z jakich książek chcesz skorzystać?\n\n"
              "Wybierz numer pozycji:\n"
              "1.Cień Władcy Demonów - Podręcznik Główny\n"
              "2.Straszliwe Piękno\n"
              "3.Rozkoszna Agonia\n"
              "4.Niepewna Wiara\n"
              "5.Głód w Pustce\n"
              "6.Grobowce Pustkowi\n")
        book_choice = input().lower()

        match book_choice:
            case "1":
                return "Cień Władcy Demonów - Podręcznik Główny"
            case "2":
                return "Straszliwe Piękno"
            case "3":
                return "Rozkoszna Agonia"
            case "4":
                return "Niepewna Wiara"
            case "5":
                return "Głód w Pustce"
            case "6":
                return "Grobowce Pustkowi"
        return book_choice

    @staticmethod
    def ancestry_pick(book_choice):
        if book_choice == "Cień Władcy Demonów - Podręcznik Główny":
            print("Jakie pochodzenie wybierasz?\n\n"
                  "1.Człowiek\n"
                  "2.Automaton\n"
                  "3.Goblin\n"
                  "4.Krasnolud\n"
                  "5.Odmieniec\n"
                  "6.Ork\n"
                  "7.Losowe")
        elif book_choice == "Straszliwe Piękno":
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
                return "Człowiek"
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

