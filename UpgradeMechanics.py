import pandas as pd

from DiceRoller import dice_roller


class UpgradeMechanics:
    @staticmethod
    def add_attribute_points(hero, value_increase):
        print(f"Jaki atrybut chcesz podnieść o {value_increase}?")
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
    def add_profession(hero, single_profession):
        if single_profession is True:

            data = pd.read_excel('dataBase\professions.xlsx',"Rodzaje Profesji")
            df = pd.DataFrame(data, columns=['attribute', 'value'])
            profession_type = dice_roller(1, 6)
            hero.professions.append(random_profession)
        else:
            print("Teraz możesz wybrać dwie profesje, lub profesje i możliwość mówienia nowym językiem lub umiejętność "
                  "czytania i pisania w języku którym już umiesz mówić.\n")
            print("Czy chcesz wybrać dodatkowy język zamiast profesji?\n"
                  "1.Tak\n"
                  "2.Nie\n")
            profession_choice = input()

            if profession_choice == "1":
                print("To języki które Twoja postać posiada:")
                print("Mówione:")
                print(hero.languages_spoken)
                print("Czytane i Pisane:")
                print(hero.languages_written)
                print("Chcesz dodać nowy jezyk mówiony, czy nauczyć się czytać i pisać w już posiadanym?")


    @staticmethod
    def add_language(hero, type_of_language, language, user_choice):

        if user_choice is True:

            # dodaj asercję dla tablicy czy język już jest dodany do pól obiektów
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
        else:
            if type_of_language == "verbal":
                hero.languages_spoken.append(language)
            else:
                hero.languages_written.append(language)
        return hero
