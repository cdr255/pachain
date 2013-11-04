class Character:
    """A Simple Class to make storing the character details easier"""
    def __init__(self, stats, level, points):
        self.str = stats
        self.dex = stats
        self.con = stats
        self.int = stats
        self.wis = stats
        self.cha = stats
        self.strmod = 0
        self.dexmod = 0
        self.conmod = 0
        self.intmod = 0
        self.wismod = 0
        self.chamod = 0
        self.level = level
        self.points = points
        self.featpoints = 0
        self.skillpoints = 0
        self.lang = ""
        self.speed = 0
        self.size = ""
        self.hitdie = 0
        self.hd = ""
        
        

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
                
        self.strmod = (self.str - 10) // 2
        self.dexmod = (self.dex - 10) // 2
        self.conmod = (self.con - 10) // 2
        self.intmod = (self.int - 10) // 2
        self.wismod = (self.wis - 10) // 2
        self.chamod = (self.cha - 10) // 2

    def selectclass(self):
        correct = False
        while correct == False:
            choice = raw_input("What class is Your character going to be? ")
            
            if choice == "Fighter" or choice == "fighter" or choice == "FIGHTER":
                self.Class = "Fighter"
                correct = True
                self.skillpoints += (self.intmod + 2) * self.level
                self.hitdie = 10
                self.hd = "d10"
                

    def selectrace(self):
        correct = False
        while correct == False:
            choice = raw_input("What race is Your character going to be? ")

            if choice == "Human" or choice == "human" or choice == "HUMAN":
                self.Race = "Human"
                correct = True
                fcorrect = False
                while fcorrect == False:
                    
                    favored = raw_input("Humans get to choose one Ability to boost by 2. What is Your Favored Ability?")
                    
                    if favored == "STR" or favored == "str" or favored == "Strength" or favored == "strength" or favored == "STRENGTH":
                        self.str += 2
                        fcorrect = True
                        
                    elif favored == 'DEX' or favored == 'dex' or favored == 'Dexterity' or favored == 'dexterity' or favored == 'DEXTERITY':
                        self.dex += 2
                        fcorrect = True
                        
                    elif favored == 'CON' or favored == 'con' or favored == 'Constitution' or favored == 'constitution' or favored == 'Constitution':
                        self.con += 2
                        fcorrect = True
                        
                    elif favored == 'INT' or favored == 'int' or favored == 'Intelligence' or favored == 'intelligence' or favored == 'INTELLIGENCE':
                        self.int += 2
                        fcorrect = True
                        
                    elif favored == 'WIS' or favored == 'wis' or favored == 'Wisdom' or favored == 'wisdom' or favored == 'WISDOM':
                        self.wis += 2
                        fcorrect = True
                        
                    elif favored == 'CHA' or favored == 'cha' or favored == 'Charisma' or favored == 'charisma' or favored == 'CHARISMA':
                        self.cha += 2
                        fcorrect = True
                        
                    else:
                        "Sorry, I don't recognize '" + favored + "', maybe try the three-letter-code? (STR, DEX, CON, INT, WIS, CHA)"
              
                self.size = "Medium"
                self.speed = 30
                self.featpoints += 1
                self.skillpoints +=  self.level
                self.lang += "Common"

level = int(raw_input("What Level Character are You trying to make?"))

mycharacter = Character(10, level, 25)



mycharacter.pointbuy()
mycharacter.selectrace()
mycharacter.selectclass()

print "Strength: ", mycharacter.str
print "Dexterity: ", mycharacter.dex
print "Constitution: ", mycharacter.con
print "Intelligence: ", mycharacter.int
print "Wisdom: ", mycharacter.wis
print "Charisma: ", mycharacter.cha
print "Level: ", mycharacter.level
print "Point Buy: ", mycharacter.points
print "Class: ", mycharacter.Class
print "Size: ", mycharacter.size
print "Speed: ", mycharacter.speed, " ft/rnd"
print "Number of Feats: ", mycharacter.featpoints
print "Total Skill Points: ", mycharacter.skillpoints
print "Languages Known: ", mycharacter.lang
