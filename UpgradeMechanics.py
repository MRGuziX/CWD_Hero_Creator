from FinalCharacter import FinalCharacter

character = FinalCharacter()


class UpgradeMechanics:
    @staticmethod
    def statistic_increment(statistic_to_increase):

        print("siła przekazana")
        print(character.strength)

        match statistic_to_increase:
            case "Siła":
                print(character.strength)
                character.strength += 1
                character.health += 1
                print(character.strength)
            case "Zręczność":
                character.dexterity += 1
                character.defence += 1
            case "Inteligencja":
                character.intelligence += 1
                character.perception += 1
            case "Wola":
                character.will += 1
            case _:
                 "Błąd"

    def size_increment(self, picked_size):
        if picked_size == "1":
            character.character_size = "1"
        else:
            character.character_size = "0.5"
