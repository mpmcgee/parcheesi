'''
objects for parcheesi game
'''
import random

#Initialize player class
class Player(object):
  def __init__(self, name, indicator, position, danger, wins):
    self.position = position
    self.indicator = indicator
    self.name = name
    self.danger = danger
    self.wins = wins

  #method to print gameboard for each player
  def printBoard(self):
      board=""
      for i in range(69):
          if i < 63 and i != self.position and i%5 != 0:
            board +="."

          elif i != self.position and i%5 == 0:
            board +="-"

          elif i == self.position:
             board += str(self.indicator)

          else: board += "-"


      print("{}" .format(board))

  #method to update danger status depending on position on the board
  def checkDanger(self):
      if self.position < 63 and self.position % 5 == 0:
          self.danger = "safe"
      elif self.position < 63 and self.position % 5 != 0:
          self.danger = "danger"
      elif self.position >= 63:
          self.danger = "safe"

#Initialize computer player subclass
class Computer(Player):
 def __init__(self, name, indicator, position, danger, wins):
      self.position = position
      self.indicator = indicator
      self.name = name
      self.danger = danger
      self.wins = wins

 #calls appropriate dice rolling method depending on player position
 def autoRoll(self):
     if self.position == 0:
         self.autoRollJail()

     elif self.position > 0 and self.position < 63:
         self.autoDiceRoll()

     elif self.position >= 63:
         self.autoDieRoll()

 #roll for doubles to get out of jail (spot 0)
 def autoRollJail(self):
        i=1
        while i <= 3:

            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("{}({}) rolled a {} and a {}" .format(self.name, self.indicator, die1, die2))
            if die1 == die2:
                self.position = 1
                i=4
                print("{}({}) is out of jail" .format(self.name, self.indicator))
                self.autoDiceRoll()
            else:
                self.position = 0
                i=i+1

 #roll 2 dice and advance
 def autoDiceRoll(self):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1+die2
    checkRoll = self.position + roll
    if checkRoll > 69:
        print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
        self.position = self.position
    else:
        self.position = checkRoll
    print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))

    if die1 == die2:
        self.autoReroll()

 #roll 1 die and advance
 def autoDieRoll(self):
     die1 = random.randint(1,6)
     rollCheck = self.position + die1
     if rollCheck > 69:
         self.position = self.position
         print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))

     elif self.position <= 69:
         print("{}({}) rolled a {}" .format (self.name, self.indicator, die1))
         self.position = rollCheck

 #reroll 2 dice when a player rolls doubles and keep doing so
 def autoReroll(self):
    print("{}({})rolled doubles, roll again." .format(self.name, self.indicator))
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1+die2
    rollCheck = self.position + roll
    if rollCheck > 69:
        self.position = self.position
        print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
    else:
        self.position = rollCheck
        print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))

    while die1 == die2:
        print("{}({})rolled doubles, roll again." .format(self.name, self.indicator))
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = die1+die2
        rollCheck = self.position + roll
        if rollCheck > 69:
            self.position = self.position
            print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
        else:
            print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))
            self.position = rollCheck

 #choose a random name from list and make computer player's name
 def autoGetName(self):
     compName = ("Geronimo", "Ernest", "Genevive", "Rufus", "Pascuala", "Reiner", "Dannica", "Gianna")
     self.name = random.choice(compName)







# initialize human player subclass
class Human(Player):
 def __init__(self, name, indicator, position, danger, wins):
      self.position = position
      self.indicator = indicator
      self.name = name
      self.danger = danger
      self.wins = wins

 #calls appropriate dice rolling method depending on player position
 def roll(self):
     if self.position == 0:
         self.rollJail()

     elif self.position > 0 and self.position < 63:
         self.diceRoll()

     elif self.position >= 63:
         self.dieRoll()

 #roll for doubles to get out of jail (spot 0)
 def rollJail(self):
        i=1
        while i <= 3:
            enter = input("Player {} Press enter to Roll for doubles" .format(self.name))
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("{}({}) rolled a {} and a {}" .format(self.name, self.indicator, die1, die2))
            if die1 == die2:
                self.position = 1
                i=4
                print("{}({}) is out of jail" .format(self.name, self.indicator))
                self.diceRoll()
            else:
                self.position = 0
                i=i+1

 #roll two dice and advance
 def diceRoll(self):
    enter = input("{}({}) Press enter to Roll 2 dice" .format(self.name, self.indicator))
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1+die2
    checkRoll = self.position + roll
    if checkRoll > 69:
        print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
        self.position = self.position
    else:
        self.position = checkRoll
    print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))

    if die1 == die2:
        self.reroll()

 #roll 1 die and advance
 def dieRoll(self):
     enter = input("{}({}) Press enter to Roll 1 die" .format(self.name, self.indicator))
     die1 = random.randint(1,6)
     rollCheck = self.position + die1
     if rollCheck > 69:
         self.position = self.position
         print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))

     elif self.position <= 69:
         print("{}({}) rolled a {}" .format (self.name, self.indicator, die1))
         self.position = rollCheck

 #reroll if a player rolls doubles and continue to do so
 def reroll(self):
    print("{}({})rolled doubles, roll again." .format(self.name, self.indicator))
    enter = input("{}({}) Press enter to Roll 2 dice" .format(self.name, self.indicator))
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1+die2
    rollCheck = self.position + roll
    if rollCheck > 69:
        self.position = self.position
        print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
    else:
        self.position = rollCheck
        print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))

    while die1 == die2:
        print("{}({})rolled doubles, roll again." .format(self.name, self.indicator))
        enter = input("{}({}) Press enter to Roll 2 dice" .format(self.name, self.indicator))
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = die1+die2
        rollCheck = self.position + roll
        if rollCheck > 69:
            self.position = self.position
            print("{}({}) overrolled and does not advance" .format (self.name, self.indicator))
        else:
            print("{}({})rolled a(n) {}" .format(self.name, self.indicator, roll))
            self.position = rollCheck

 #set player name with input
 def getName(self):
     self.name = input("Player {} please enter your name: " .format(self.indicator))