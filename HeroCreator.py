from __future__ import annotations


class Characters:

    def __init__(self):
        self.book = None
        self.name = None
        self.ancestry = None

        self.strength = None
        self.dexterity = None
        self.intelligence = None
        self.will = None
        self.perception = None
        self.health = None
        self.speed = None
        self.defence = None
        self.healing_rate = None
        self.power = None
        self.insanity = None
        self.corruption = None
        self.damage = None
        self.character_size = None
        self.languages_spoken = []
        self.languages_written = []
        self.professions = []
        self.race_talents = []

        self.backstory = None
        self.age = None
        self.character = None
        self.body = None
        self.appearance = None
        self.quirks = None
        self.religion = None
        self.changeling = None

        self.equipment = None
        self.oddity = None
        self.gold_coins = 0
        self.silver_coins = 0
        self.copper_coins = 0
        self.pieces_coins = 0
        self.wealth = None

        #tablica wielowymiarowa Items ktora przyjmuje mniejsze tablice jak weapons czy shields
        self.items = []

        self.melee_weapons = []
        self.ranged_weapons = []
        self.armors = []
        self.shields = []

        self.items.append(self.melee_weapons)
        self.items.append(self.ranged_weapons)
        self.items.append(self.armors)
        self.items.append(self.shields)

        # może warto uzyć touple?
    def getting_melee_weapons(self, item):
        self.items[0].append(item)

    def getting_ranged_weapons(self, item):
        self.items[1].append(item)

    def getting_armors(self, item):
        self.items[2].append(item)

    def getting_shields(self, item):
        self.items[3].append(item)


