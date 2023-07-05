import random
import pandas as pd

from DiceRoller import dice_roller
from ItemCreator import Items

item_instance = Items()


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

                    profession_name = random.randint(0, 19)
                    hero.professions.append(data.iloc[profession_name, 1])
                case 2:
                    data = pd.read_excel('dataBase/professions.xlsx', "Pospolite")

                    profession_name = random.randint(0, 19)
                    hero.professions.append(data.iloc[profession_name, 1])
                case 3:
                    data = pd.read_excel('dataBase/professions.xlsx', "Przestępcze")

                    profession_name = random.randint(0, 19)
                    hero.professions.append(data.iloc[profession_name, 1])
                case 4:
                    data = pd.read_excel('dataBase/professions.xlsx', "Wojenne")

                    profession_name = random.randint(0, 19)
                    hero.professions.append(data.iloc[profession_name, 1])
                case 5:
                    data = pd.read_excel("dataBase/professions.xlsx", "Koczownicze")

                    profession_name = random.randint(0, 19)

                    match profession_name:
                        case 4 | 5:
                            hero.professions.append(data.iloc[4, 1])
                        case 7 | 8:
                            hero.professions.append(data.iloc[6, 1])
                        case 14 | 15:
                            hero.professions.append(data.iloc[12, 1])
                        case _:
                            hero.professions.append(data.iloc[profession_name, 1])

                case 6:
                    data = pd.read_excel('dataBase/professions.xlsx', "Religijne")
                    profession_name = random.randint(0, 19)
                    mechanic_instance = UpgradeMechanics()

                    match profession_name:
                        case 0 | 1:
                            hero.professions.append(data.iloc[0, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 2 | 3:
                            hero.professions.append(data.iloc[1, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 4 | 5:
                            hero.professions.append(data.iloc[2, 1])
                        case 6 | 7:
                            hero.professions.append(data.iloc[3, 1])
                        case 8 | 9:
                            hero.professions.append(data.iloc[4, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 10 | 11:
                            hero.professions.append(data.iloc[5, 1])
                            mechanic_instance.language_compare_add(hero, "written")
                        case 12 | 13:
                            hero.professions.append(data.iloc[6, 1])
                        case 14 | 15:
                            hero.professions.append(data.iloc[7, 1])
                        case 16 | 17:
                            hero.professions.append(data.iloc[8, 1])
                        case 18 | 19:
                            hero.professions.append(data.iloc[9, 1])

            return hero

    @staticmethod
    def add_wealth(hero):
        data = pd.read_excel('dataBase/utilities.xlsx', sheet_name="Zamożność")
        life_standard = dice_roller(3, 6)
        random_item_picker = random.randint(0, 1)

        match life_standard:
            case 3 | 4:
                hero.wealth = data.iloc[0, 1]
                hero.equipment = data.iloc[0, 2]
                hero.pieces_coins += dice_roller(1, 6)
                if random_item_picker == 1:
                    hero.getting_weapons(item_instance.add_item("Pałka"))
                else:
                    hero.getting_weapons(item_instance.add_item("Proca"))
            case 5 | 6 | 7 | 8:
                hero.wealth = data.iloc[1, 1]
                hero.equipment = data.iloc[1, 2]
                hero.pieces_coins += dice_roller(2, 6)
                hero.getting_weapons(item_instance.add_item("Pałka"))
            case 9 | 10 | 11 | 12 | 13:
                hero.wealth = data.iloc[2, 1]
                hero.equipment = data.iloc[3, 2]
                hero.copper_coins += dice_roller(1, 6)
                hero.getting_weapons(item_instance.add_item("Pałka"))
            case 14 | 15 | 16:
                hero.wealth = data.iloc[3, 1]
                hero.equipment = data.iloc[4, 2]
                hero.copper_coins += dice_roller(2, 6)
                hero.getting_weapons(item_instance.add_item("Pałka"))
            case 17:
                hero.wealth = data.iloc[4, 1]
                hero.equipment = data.iloc[5, 2]
                hero.silver_coins += dice_roller(1, 6)
                hero.getting_weapons(item_instance.add_item("Pałka"))
            case 18:
                hero.wealth = data.iloc[5, 1]
                hero.equipment = data.iloc[6, 2]
                hero.silver_coins += dice_roller(2, 6)
                hero.getting_weapons(item_instance.add_item("Pałka"))
        return hero

    @staticmethod
    def add_oddity(hero):

        oddity_table_roller = dice_roller(1, 6)
        oddity_type = random.randint(0, 19)

        match oddity_table_roller:
            case 1:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza A")

                hero.oddity = data.iloc[oddity_type, 1]
            case 2:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza B")

                hero.oddity = data.iloc[oddity_type, 1]
            case 3:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza C")

                hero.oddity = data.iloc[oddity_type, 1]
            case 4:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza D")

                hero.oddity = data.iloc[oddity_type, 1]
            case 5:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza E")

                hero.oddity = data.iloc[oddity_type, 1]
            case 6:
                data = pd.read_excel('dataBase/utilities.xlsx', "Kurioza F")

                hero.oddity = data.iloc[oddity_type, 1]
        return hero
