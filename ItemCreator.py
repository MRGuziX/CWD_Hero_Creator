from __future__ import annotations

import pandas as pd

from PDFCreator import PDFCreator

pdf_creator_instance = PDFCreator()


class Items:

    def __init__(self):
        self.weapon_name = ""
        self.weapon_type = ""

        self.weapon_grip = ""
        self.weapon_damage = ""
        self.weapon_feature = ""

        self.shield = ""
        self.shield_damage = ""
        self.shield_feature = ""

        self.armor = ""
        self.armor_value = ""
        self.armor_feature = ""

    @staticmethod
    def add_item(item_name):
        item = Items()
        item_data_sheet = pd.read_excel('dataBase/items.xlsx', sheet_name="Weapons")
        match item_name:
            case "Pałka":
                item.weapon_name = item_data_sheet.iloc[0, 0]
                item.weapon_damage = item_data_sheet.iloc[0, 1]
                item.weapon_grip = item_data_sheet.iloc[0, 2]
                item.weapon_feature = item_data_sheet.iloc[0, 3]
                item.weapon_type = "zwarcie"
            case "Proca":
                item.weapon_name = item_data_sheet.iloc[1, 0]
                item.weapon_damage = item_data_sheet.iloc[1, 1]
                item.weapon_grip = item_data_sheet.iloc[1, 2]
                item.weapon_feature = item_data_sheet.iloc[1, 3]
                item.weapon_type = "zasięgowa"
            case "Kostur":
                item.weapon_name = item_data_sheet.iloc[2, 0]
                item.weapon_damage = item_data_sheet.iloc[2, 1]
                item.weapon_grip = item_data_sheet.iloc[2, 2]
                item.weapon_feature = item_data_sheet.iloc[2, 3]
                item.weapon_type = "zwarcie"
            case "Sztylet":
                item.weapon_name = item_data_sheet.iloc[3, 0]
                item.weapon_damage = item_data_sheet.iloc[3, 1]
                item.weapon_grip = item_data_sheet.iloc[3, 2]
                item.weapon_feature = item_data_sheet.iloc[3, 3]
                item.weapon_type = "zwarcie"
            case "Miecz":
                item.weapon_name = item_data_sheet.iloc[4, 0]
                item.weapon_damage = item_data_sheet.iloc[4, 1]
                item.weapon_grip = item_data_sheet.iloc[4, 2]
                item.weapon_feature = item_data_sheet.iloc[4, 3]
                item.weapon_type = "zwarcie"

        return item
