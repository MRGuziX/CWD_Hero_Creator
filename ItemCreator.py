from __future__ import annotations

import pandas as pd

from PDFCreator import PDFCreator

pdf_creator_instance = PDFCreator()


class Items:

    def __init__(self):
        self.weapon_melee = None
        self.weapon_melee_grip = None
        self.weapon_melee_damage = None
        self.weapon_melee_feature = None

        self.weapon_melee2 = None
        self.weapon_melee2_grip = None
        self.weapon_melee2_damage = None
        self.weapon_melee2_feature = None

        self.weapon_ranged = None
        self.weapon_ranged_grip = None
        self.weapon_ranged_damage = None
        self.weapon_ranged_feature = None

        self.shield = None
        self.shield_grip = None
        self.shield_damage = None
        self.shield_feature = None

        self.armor = None
        self.armor_value = None
        self.armor_feature = None

    @staticmethod
    def add_item(item_name):
        item = Items()
        item_data_sheet = pd.read_excel('dataBase/items.xlsx', sheet_name="Weapons")
        match item_name:
            case "Pałka":
                item.weapon_melee = item_data_sheet.iloc[0, 0]
                item.weapon_melee_damage = item_data_sheet.iloc[0, 1]
                item.weapon_melee_grip = item_data_sheet.iloc[0, 2]
                item.weapon_melee_feature = item_data_sheet.iloc[0, 3]
            case "Proca":
                item.weapon_melee = item_data_sheet.iloc[0, 0]
                item.weapon_melee_damage = item_data_sheet.iloc[0, 1]
                item.weapon_melee_grip = item_data_sheet.iloc[0, 2]
                item.weapon_melee_feature = item_data_sheet.iloc[0, 3]
            case "Miecz":
                print("pałka")
            case "Młot":
                print("pałka")
        return item
