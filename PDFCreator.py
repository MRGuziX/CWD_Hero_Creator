from pypdf import PdfReader, PdfWriter

reader = PdfReader("utilities/CWD_karta.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)


class PDFCreator:
    @staticmethod
    def hero_pdf_creator(hero):
        writer.update_page_form_field_values(writer.pages[0], {"imie": hero.name})
        writer.update_page_form_field_values(writer.pages[0], {"pochodzenie": hero.ancestry})
        writer.update_page_form_field_values(writer.pages[0], {"sila": hero.strength})
        writer.update_page_form_field_values(writer.pages[0], {"wola": hero.will})
        writer.update_page_form_field_values(writer.pages[0], {"zrecznosc": hero.dexterity})
        writer.update_page_form_field_values(writer.pages[0], {"intelekt": hero.intelligence})
        writer.update_page_form_field_values(writer.pages[0], {"percepcja": hero.perception})
        writer.update_page_form_field_values(writer.pages[0], {"zdrowie": hero.health})
        writer.update_page_form_field_values(writer.pages[0], {"predkosc": hero.speed})
        writer.update_page_form_field_values(writer.pages[0], {"obrona": hero.defence})
        writer.update_page_form_field_values(writer.pages[0], {"predkosc_zdrowienia": hero.healing_rate})
        writer.update_page_form_field_values(writer.pages[0], {"moc": hero.power})
        writer.update_page_form_field_values(writer.pages[0], {"szalenstwo": hero.insanity})
        writer.update_page_form_field_values(writer.pages[0], {"splugawienie": hero.corruption})
        writer.update_page_form_field_values(writer.pages[0], {"jezyki_pisane": hero.languages_written})
        writer.update_page_form_field_values(writer.pages[0], {"jezyki_mowione": hero.languages_spoken})
        writer.update_page_form_field_values(writer.pages[0], {"rozmiar": hero.character_size})

        writer.update_page_form_field_values(writer.pages[0], {"wiek": hero.age})
        writer.update_page_form_field_values(writer.pages[0], {"wyglad": hero.appearance})
        writer.update_page_form_field_values(writer.pages[0], {"przeszlosc": hero.backstory})
        writer.update_page_form_field_values(writer.pages[0], {"budowa_ciala": hero.body})
        writer.update_page_form_field_values(writer.pages[0], {"religia": hero.religion})
        writer.update_page_form_field_values(writer.pages[0], {"osobowosc": hero.character})
        writer.update_page_form_field_values(writer.pages[0], {"dziwactwa": hero.quirks})

        writer.update_page_form_field_values(writer.pages[0], {"kuriozum": hero.oddity})
        writer.update_page_form_field_values(writer.pages[0], {"sprzet": hero.equipment})

        writer.update_page_form_field_values(writer.pages[0], {"profesje": hero.professions})
        writer.update_page_form_field_values(writer.pages[0], {"zamoznosc": hero.wealth})
        writer.update_page_form_field_values(writer.pages[0], {"zlote_korony": hero.gold_coins})
        writer.update_page_form_field_values(writer.pages[0], {"srebrniki": hero.silver_coins})
        writer.update_page_form_field_values(writer.pages[0], {"miedziaki": hero.copper_coins})
        writer.update_page_form_field_values(writer.pages[0], {"okrawki": hero.pieces_coins})

        with open("output/filled-out.pdf", "wb") as output_stream:
            writer.write(output_stream)

    @staticmethod
    def item_pdf_creator(hero):
        # tablice wielowymiarowe hero otwiera plecak o nazwie items i patrzy w pierwszą przegrodę gdzie
        # przetrzymywane są armory, a potem wubiera pierwsza armor

        def assign_first_weapon():
            writer.update_page_form_field_values(writer.pages[0], {"bron1": hero.items[0][0].weapon_name})
            writer.update_page_form_field_values(writer.pages[0], {"bron1_chwyt": hero.items[0][0].weapon_grip})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron1_obrazenia": hero.items[0][0].weapon_damage})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron1_wlasciwosci": hero.items[0][0].weapon_feature})

        def assign_second_weapon():
            writer.update_page_form_field_values(writer.pages[0], {"bron2": hero.items[0][1].weapon_name})
            writer.update_page_form_field_values(writer.pages[0], {"bron2_Chwyt": hero.items[0][1].weapon_grip})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron2_Obrazenia": hero.items[0][1].weapon_damage})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron2_wlasciwosci": hero.items[0][1].weapon_feature})

        def assign_ranged_weapon():
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron_dystansowa": hero.items[1][0].weapon_name})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron_dystansowa_chwyt": hero.items[1][
                                                     0].weapon_grip})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron_dystansowa_obrazenia": hero.items[1][
                                                     0].weapon_damage})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"bron_dystansowa_wlasciwosci": hero.items[1][
                                                     0].weapon_feature})

        def assign_armor():
            writer.update_page_form_field_values(writer.pages[0], {"pancerz": hero.items[2][0].armor})
            writer.update_page_form_field_values(writer.pages[0], {"pancerz_obrona": hero.items[2][0].armor_value})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"pancerz_wlasciwosci": hero.items[2][0].armor_feature})

        def assign_shield():
            writer.update_page_form_field_values(writer.pages[0], {"tarcza": hero.items[3][0].shield})
            writer.update_page_form_field_values(writer.pages[0], {"tarcza_obrazenia": hero.items[3][0].shield_damage})
            writer.update_page_form_field_values(writer.pages[0],
                                                 {"tarcza_wlasciwosci": hero.items[3][0].shield_feature})

        number_of_melee_weapons = len(hero.items[0])
        number_of_ranged_weapons = len(hero.items[1])
        number_of_armors = len(hero.items[2])
        number_of_shields = len(hero.items[3])

        if number_of_melee_weapons == 1:
            assign_first_weapon()
        elif number_of_melee_weapons == 2:
            assign_first_weapon()
            assign_second_weapon()

        if number_of_ranged_weapons == 1:
            assign_ranged_weapon()

        if number_of_shields == 1:
            assign_shield()

        if number_of_armors == 1:
            assign_armor()

        # write "output" to PyPDF2-output.pdf
        with open("output/filled-out.pdf", "wb") as output_stream:
            writer.write(output_stream)
