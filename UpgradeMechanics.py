class UpgradeMechanics:
    @staticmethod
    def add_attribute_points(hero):
        print("Jaki atrybut chcesz podnieść o 1?")
        statistic_to_increase = input("1. Siła\n"
                                      "2. Zręczność\n"
                                      "3. Inteligencja\n"
                                      "4. Wola\n")

        match statistic_to_increase:
            case "1":
                hero.strength += 1
                hero.health += 1
            case "2":
                hero.dexterity += 1
                hero.defence += 1
            case "3":
                hero.intelligence += 1
                hero.perception += 1
            case "4":
                hero.will += 1
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
    def add_language(hero):
        pass
