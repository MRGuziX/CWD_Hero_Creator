from pypdf import PdfReader, PdfWriter

reader = PdfReader("utilities/poprawiona_karta2_CWD.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)


class PDFCreator:
    @staticmethod
    def pdf_creator(hero):
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

        writer.update_page_form_field_values(writer.pages[0], {"profesje": hero.professions})
        writer.update_page_form_field_values(writer.pages[0], {"miedziaki": hero.copper_coins})

        # write "output" to PyPDF2-output.pdf
        with open("output/filled-out.pdf", "wb") as output_stream:
            writer.write(output_stream)
