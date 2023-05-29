class UpgradeMechanics:
    @staticmethod
    def add_attribute_points(hero, value_increase):
        print("Jaki atrybut chcesz podnieść o 1?")
        statistic_to_increase = input("1. Siła\n"
                                      "2. Zręczność\n"
                                      "3. Inteligencja\n"
                                      "4. Wola\n")

        match statistic_to_increase:
            case "1":
                hero.strength += value_increase
                hero.health += value_increase
            case "2":
                hero.dexterity += value_increase
                hero.defence += value_increase
            case "3":
                hero.intelligence += value_increase
                hero.perception += value_increase
            case "4":
                hero.will += value_increase
            case _:
                "Błąd"
        return hero

    @staticmethod
    def add_size(hero):
        print("Jaki rozmiar chce wybrać?")
        size = input("1. Rozmiar: 1\n"
                     "2. Rozmiar: 1/2\n")

        if size == "1":
            hero.character_size = "1"
        else:
            hero.character_size = "0.5"
        return hero

    @staticmethod
    def add_magic_school(hero):
        pass

    @staticmethod
    def add_spell(hero):
        pass

    @staticmethod
    def add_profession(hero):
        pass

    @staticmethod
    def add_language(hero, type_of_language):
        #dodaj asercję dla tablicy czy język już jest dodany do pól obiektów
        print("Języki do wyboru: \n"
              "1. Wspólny\n"
              "2. Mroczna mowa\n"
              "3. Krasnoludzki\n"
              "4. Elficki\n"
              "5. Wysoki archaik\n"
              "6. Trolli\n"
              "7. Sekretny język\n"
              "8. Martwy język\n")
        if type_of_language == "verbal":
            choice = input("Wybierz numer języka:")
            match choice:
                case "1":
                    hero.languages_spoken.append("Wspólny")
                case "2":
                    hero.languages_spoken.append("Mroczna mowa")
                case "3":
                    hero.languages_spoken.append("Krasnoludzki")
                case "4":
                    hero.languages_spoken.append("Elficki")
                case "5":
                    hero.languages_spoken.append("Wysoki archaik")
                case "6":
                    hero.languages_spoken.append("Trolli")
                case "7":
                    hero.languages_spoken.append("Sekretny język(        )")
                case "8":
                    hero.languages_spoken.append("Martwy język(        )")
        else:
            choice = input("Wybierz numer języka:")
            match choice:
                case "1":
                    hero.languages_written.append("Wspólny")
                case "2":
                    hero.languages_written.append("Mroczna mowa")
                case "3":
                    hero.languages_written.append("Krasnoludzki")
                case "4":
                    hero.languages_written.append("Elficki")
                case "5":
                    hero.languages_written.append("Wysoki archaik")
                case "6":
                    hero.languages_written.append("Trolli")
                case "7":
                    hero.languages_written.append("Sekretny język(        )")
                case "8":
                    hero.languages_written.append("Martwy język(        )")
        return hero

