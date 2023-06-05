from pypdf import PdfReader, PdfWriter

reader = PdfReader("utilities/BG_SHEET.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)


class PDFCreator:
    @staticmethod
    def pdf_creator(hero):
        writer.update_page_form_field_values(writer.pages[0], {"Imie": hero.name})
        writer.update_page_form_field_values(writer.pages[0], {"Pochodzenie": hero.ancestry})

        writer.update_page_form_field_values(writer.pages[0], {"Siła": hero.strength})
        writer.update_page_form_field_values(writer.pages[0], {"Wola": hero.will})
        writer.update_page_form_field_values(writer.pages[0], {"Zręczność": hero.dexterity})
        writer.update_page_form_field_values(writer.pages[0], {"Intelekt": hero.intelligence})
        writer.update_page_form_field_values(writer.pages[0], {"Percepcja": hero.perception})
        writer.update_page_form_field_values(writer.pages[0], {"Zdrowie": hero.health})
        writer.update_page_form_field_values(writer.pages[0], {"Prędkość": hero.speed})
        writer.update_page_form_field_values(writer.pages[0], {"Obrona": hero.defence})
        writer.update_page_form_field_values(writer.pages[0], {"Predkosc zdrowienia": hero.healing_rate})
        writer.update_page_form_field_values(writer.pages[0], {"Moc": hero.power})
        writer.update_page_form_field_values(writer.pages[0], {"Szaleństwo": hero.insanity})
        writer.update_page_form_field_values(writer.pages[0], {"Splugawienie": hero.corruption})
        writer.update_page_form_field_values(writer.pages[0], {"Języki Pisane": hero.languages_written})
        writer.update_page_form_field_values(writer.pages[0], {"Języki Mówione": hero.languages_spoken})
        writer.update_page_form_field_values(writer.pages[0], {"Rozmiar": hero.character_size})

        writer.update_page_form_field_values(writer.pages[0], {"Wiek": hero.age})
        writer.update_page_form_field_values(writer.pages[0], {"Wygląd": hero.appearance})
        writer.update_page_form_field_values(writer.pages[0], {"Przeszlosc": hero.backstory})
        writer.update_page_form_field_values(writer.pages[0], {"Budowa Ciała": hero.body})
        writer.update_page_form_field_values(writer.pages[0], {"Religia": hero.religion})
        writer.update_page_form_field_values(writer.pages[0], {"Osobowość": hero.character})
        writer.update_page_form_field_values(writer.pages[0], {"Dziwactwa": hero.quirks})

        writer.update_page_form_field_values(writer.pages[0], {"Profesje": hero.professions})
        writer.update_page_form_field_values(writer.pages[0], {"Miedziaki": hero.copper_coins})

        # write "output" to PyPDF2-output.pdf
        with open("output/filled-out.pdf", "wb") as output_stream:
            writer.write(output_stream)
