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

    def pointbuy(self):
        numberofskills = 6
        roundvalue = 0

        while numberofskills != 0:
            if numberofskills == 5:
                roundvalue = 4

            elif numberofskills == 3:
                roundvalue = 2
        
            else:
                roundvalue = numberofskills

            choice = raw_input('What is the most important skill for Your character?')

            if choice == "STR" or choice == "str" or choice == "Strength" or choice == "strength" or choice == "STRENGTH":
                self.str += roundvalue
                numberofskills -= 1
                
            elif choice == 'DEX' or choice == 'dex' or choice == 'Dexterity' or choice == 'dexterity' or choice == 'DEXTERITY':
                self.dex += roundvalue
                numberofskills -= 1
                
            elif choice == 'CON' or choice == 'con' or choice == 'Constitution' or choice == 'constitution' or choice == 'Constitution':
                self.con += roundvalue
                numberofskills -= 1
                
            elif choice == 'INT' or choice == 'int' or choice == 'Intelligence' or choice == 'intelligence' or choice == 'INTELLIGENCE':
                self.int += roundvalue
                numberofskills -= 1
                
            elif choice == 'WIS' or choice == 'wis' or choice == 'Wisdom' or choice == 'wisdom' or choice == 'WISDOM':
                self.wis += roundvalue
                numberofskills -= 1
                
            elif choice == 'CHA' or choice == 'cha' or choice == 'Charisma' or choice == 'charisma' or choice == 'CHARISMA':
                self.cha += roundvalue
                numberofskills -= 1
                
            else:
                "Sorry, I don't recognize '" + choice + "', maybe try the three-letter-code? (STR, DEX, CON, INT, WIS, CHA)"

    def selectclass(self):
        correct = False
        while correct == False:
            choice = raw_input("What class is Your character going to be?  ")
            
            if choice == "Fighter" or choice == "fighter" or choice == "FIGHTER":
                self.Class = "Fighter"
                correct = True
        

mycharacter = Character(10, 1, 25)



mycharacter.pointbuy()
mycharacter.selectclass()

print mycharacter.str
print mycharacter.dex
print mycharacter.con
print mycharacter.int
print mycharacter.wis
print mycharacter.cha
print mycharacter.level
print mycharacter.points
print mycharacter.Class
