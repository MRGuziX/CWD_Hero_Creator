import random

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

    @staticmethod
    def language_compare_add(hero, type_of_language_to_add):
        all_language_list = ["Wspólny", "Mroczna mowa", "Krasnoludzki", "Elficki", "Wysoki archaik", "Trolli",
                             "Sekretny język(        )", "Martwy język(        )"]
        print("To języki które Twoja postać posiada:")
        print("Mówione:")
        print(hero.languages_spoken)
        print("Czytane i Pisane:")
        print(hero.languages_written)
        print("Tych języków możesz się nauczyć, co wybierasz?")

        if type_of_language_to_add == "verbal":
            available_languages = list(set(all_language_list) - set(hero.languages_spoken))
            print(available_languages)
            language_choice = int(input())
            hero.languages_spoken.append(available_languages[language_choice])

        else:
            available_languages = list(set(hero.languages_spoken) - set(hero.languages_written))
            print(available_languages)
            language_choice = int(input())
            hero.languages_written.append(available_languages[language_choice])
        return hero

    @staticmethod
    def add_profession(hero, user_profession_choice):
        if user_profession_choice is True:
            profession_type = dice_roller(1, 6)

            match profession_type:
                case 1:
                    data = pd.read_excel('dataBase/professions.xlsx', "Naukowe")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    hero.professions.append(df.iloc[profession_name, 1])
                case 2:
                    data = pd.read_excel('dataBase/professions.xlsx', "Pospolite")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    hero.professions.append(df.iloc[profession_name, 1])
                case 3:
                    data = pd.read_excel('dataBase/professions.xlsx', "Przestępcze")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    hero.professions.append(df.iloc[profession_name, 1])
                case 4:
                    data = pd.read_excel('dataBase/professions.xlsx', "Wojenne")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    hero.professions.append(df.iloc[profession_name, 1])
                case 5:
                    data = pd.read_excel("dataBase/professions.xlsx", "Koczownicze")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    hero.professions.append(df.iloc[profession_name, 1])

                    match profession_name:
                        case 4 | 5:
                            hero.professions.append(df.iloc[4, 1])
                        case 7 | 8:
                            hero.professions.append(df.iloc[6, 1])
                        case 14 | 15:
                            hero.professions.append(df.iloc[12, 1])
                case 6:
                    data = pd.read_excel('dataBase/professions.xlsx', "Religijne")
                    df = pd.DataFrame(data, columns=['value', 'result'])
                    profession_name = random.randint(0, 19)
                    mechanic_instance = UpgradeMechanics()

                    match profession_name:
                        case 0 | 1:
                            hero.professions.append(df.iloc[0, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 2 | 3:
                            hero.professions.append(df.iloc[1, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 4 | 5:
                            hero.professions.append(df.iloc[2, 1])
                        case 6 | 7:
                            hero.professions.append(df.iloc[3, 1])
                        case 8 | 9:
                            hero.professions.append(df.iloc[4, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 10 | 11:
                            hero.professions.append(df.iloc[5, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 12 | 13:
                            hero.professions.append(df.iloc[6, 1])
                        case 14 | 15:
                            hero.professions.append(df.iloc[7, 1])
                        case 16 | 17:
                            hero.professions.append(df.iloc[8, 1])
                        case 18 | 19:
                            hero.professions.append(df.iloc[9, 1])

            return hero
