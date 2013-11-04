class Character:
    """A Simple Class to make storing the character details easier"""
    def __init__(self, stats, level, points):
        self.str = stats
        self.dex = stats
        self.con = stats
        self.int = stats
        self.wis = stats
        self.cha = stats
        self.level = level
        self.points = points


mycharacter = Character(10, 1, 25)

print mycharacter.str
print mycharacter.dex
print mycharacter.con
print mycharacter.int
print mycharacter.wis
print mycharacter.cha
print mycharacter.level
print mycharacter.points
