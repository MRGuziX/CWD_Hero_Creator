from pypdf import PdfReader, PdfWriter

reader = PdfReader("utilities/CWD_karta.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)


class PDFCreator:
    @staticmethod
    def pdf_creator(hero, item):
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

        writer.update_page_form_field_values(writer.pages[0], {"pancerz": item.armor})
        writer.update_page_form_field_values(writer.pages[0], {"pancerz_obrona": item.armor_value})
        writer.update_page_form_field_values(writer.pages[0], {"pancerz_wlasciwosci": item.armor_feature})

        writer.update_page_form_field_values(writer.pages[0], {"bron1": item.weapon_melee})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_chwyt": item.weapon_melee_grip})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_obrazenia": item.weapon_melee_damage})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_wlasciwosci": item.weapon_melee_feature})

        writer.update_page_form_field_values(writer.pages[0], {"bron1": item.shield})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_chwyt": item.weapon_melee_grip})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_obrazenia": item.weapon_melee_damage})
        writer.update_page_form_field_values(writer.pages[0], {"bron_1_wlasciwosci": item.weapon_melee_feature})

        writer.update_page_form_field_values(writer.pages[0], {"bron2": item.weapon_melee2})
        writer.update_page_form_field_values(writer.pages[0], {"bron_2_chwyt": item.weapon_melee2_grip})
        writer.update_page_form_field_values(writer.pages[0], {"bron_2_obrazenia": item.weapon_melee2_damage})
        writer.update_page_form_field_values(writer.pages[0], {"bron_2_wlasciwosci": item.weapon_melee2_feature})

        writer.update_page_form_field_values(writer.pages[0], {"bron_dystansowa": item.weapon_ranged})
        writer.update_page_form_field_values(writer.pages[0], {"bron_dystansowa_chwyt": item.weapon_ranged_grip})
        writer.update_page_form_field_values(writer.pages[0], {"bron_dystansowa_obrazenia": item.weapon_ranged_damage})
        writer.update_page_form_field_values(writer.pages[0], {"bron_dystansowa_wlasciwosci": item.weapon_ranged_feature})

        writer.update_page_form_field_values(writer.pages[0], {"profesje": hero.professions})
        writer.update_page_form_field_values(writer.pages[0], {"zamoznosc": hero.wealth})
        writer.update_page_form_field_values(writer.pages[0], {"zlote_korony": hero.gold_coins})
        writer.update_page_form_field_values(writer.pages[0], {"srebrniki": hero.silver_coins})
        writer.update_page_form_field_values(writer.pages[0], {"miedziaki": hero.copper_coins})
        writer.update_page_form_field_values(writer.pages[0], {"okrawki": hero.pieces_coins})

        # write "output" to PyPDF2-output.pdf
        with open("output/filled-out.pdf", "wb") as output_stream:
            writer.write(output_stream)
