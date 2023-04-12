from __future__ import annotations

from abc import ABC


class Hero:
    def __init__(self, book, name, ancestry, strength, dexterity, intelligence, will, perception, health, speed,
                 defence, healing_rate, power, insanity, corruption, damage, languages_verbal, languages_written,
                 character_size, description, religion, professions, quirks):

        self.book = book
        self.name = name
        self.ancestry = ancestry

        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.will = will
        self.perception = perception
        self.health = health
        self.speed = speed
        self.defence = defence
        self.healing_rate = healing_rate
        self.power = power
        self.insanity = insanity
        self.corruption = corruption
        self.damage = damage
        self.languages_verbal = languages_verbal
        self.languages_written = languages_written
        self.character_size = character_size

        self.description = description
        self.religion = religion
        self.professions = professions
        self.quirks = quirks

        self.equipment = None


class HeroBuilder(ABC):

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
        self.languages_verbal = None
        self.languages_written = None
        self.character_size = None

        self.description = None
        self.religion = None
        self.professions = None
        self.quirks = None

        self.equipment = None

    def add_name(self, name):
        self.name = name
        return self

    def add_book(self, book):
        self.book = book

    def add_ancestry(self, ancestry):
        self.ancestry = ancestry
        return self

    def get_hero(self):
        return self.Hero(self.name)
