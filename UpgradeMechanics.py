from Builder_CWD_Hero import HeroBuilder

hero = HeroBuilder()


class UpgradeMechanics:
    @staticmethod
    def statistic_increment():
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

    @staticmethod
    def size_increment( picked_size):
        if picked_size == "1":
            hero.character_size = "1"
        else:
            hero.character_size = "0.5"
